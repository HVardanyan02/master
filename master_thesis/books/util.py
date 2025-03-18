import os
import tempfile
import time
import zipfile
from PyPDF2 import PdfReader
from bs4 import BeautifulSoup
import requests
import re
import unicodedata

# ?
heads = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}

def downloading_flib(genre_url: str, klass: str, pages: int = 60) -> None:
    main_url = "https://flibusta.one"
    for i in range(1, pages + 1):
        time.sleep(0.1)
        os.makedirs(f"booky/{klass}/{klass}_books", exist_ok=True)
        r = requests.get(genre_url + f"?page={i}", headers=heads)
        print(genre_url + f"?page={i}", r.status_code)
        soup = BeautifulSoup(r.text, "html.parser")
        books = soup.find_all("a", attrs={"class": "th-in with-mask"})
        for book in books:
            print(main_url + book.get("href"), i)
            time.sleep(0.1)
            try:
                book_page = requests.get(main_url + book.get("href"), headers=heads)
            except requests.exceptions.TooManyRedirects:
                continue
            sup = BeautifulSoup(book_page.text, "html.parser")
            lnk1 = sup.find("span", class_="link pdf")
            try:
                lnk = lnk1.get("data-link")
            except AttributeError:
                continue
            print(lnk + " fglbkflndb")
            time.sleep(0.1)
            with tempfile.TemporaryFile() as file:
                try:
                    while True:
                        try:
                            download_zip = requests.get(lnk, headers=heads, timeout=10)
                        except requests.exceptions.ConnectionError:
                            print("Waiting 2 minutes...")
                            time.sleep(120)
                            continue
                        else:
                            break
                    file.write(download_zip.content)
                    file.seek(0)  # Reset file pointer to the beginning
                    with zipfile.ZipFile(file) as fzip:
                        fzip.extractall(path=f"booky/{klass}/{klass}_books")
                except zipfile.BadZipFile:
                    print(f"BadZipFile error with link: {lnk}")
                    continue


def scanning(path, expected_list):
    mini, maxi = 100, 0
    for genre_folder in os.listdir(path):
        genre_path = os.path.join(path, genre_folder)
        if os.path.isdir(genre_path):
            for file_name in os.listdir(genre_path):
                file_path = os.path.join(genre_path, file_name)
                if file_path.endswith(".pdf"):
                    with open(file_path, "rb") as filehandle:
                        try:
                            pdf = PdfReader(filehandle)
                        except Exception:
                            continue
                        pages = len(pdf.pages)
                        if pages < mini:
                            mini = pages
                        if pages > maxi:
                            maxi = pages

    expected_list.append(mini)
    expected_list.append(maxi)
    expected_list.append((mini+maxi)/2)

def clean_text(text):
    text = unicodedata.normalize("NFKD", text)  # Normalize Unicode characters
    text = re.sub(r'\s+', ' ', text).strip()  # Replace multiple spaces with one
    
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', '', text)
    
    # Remove URLs
    text = re.sub(r'http\S+|www\.\S+', '', text)
    
    # Remove ISBN, УДК, ББК lines
    text = re.sub(r'\b(?:ISBN|УДК|ББК)[^\n]*', '', text, flags=re.IGNORECASE)
    
    text = re.sub(r'[^a-zA-Zа-яА-Я0-9\s]', '', text)
    
    text = text.lower()

    return text


def scanning_text(path, expected_list):
    ident = 0
    for genre_folder in os.listdir(path):
        genre_path = os.path.join(path, genre_folder)
        if os.path.isdir(genre_path):
            for file_name in os.listdir(genre_path):
                file_path = os.path.join(genre_path, file_name)
                if file_path.endswith(".pdf"):
                    print(genre_folder)
                    ident = ident + 1
                    print(f"a number of a BOOK IS {ident} *************************************")
                    with open(file_path, "rb") as filehandle:
                        print(":::::::::::::::::::::::::::::::")
                        try:
                            pdf = PdfReader(filehandle)
                        except Exception:
                            continue
                        pages = len(pdf.pages)
                        pdfs = ""
                        if pages > 100:
                            pages = 100
                        for i in range(pages):
                            page = pdf.pages[i]
                            pdfs += clean_text(page.extract_text().strip())  # Store cleaned text
                        expected_list.append([pdfs, genre_folder])
