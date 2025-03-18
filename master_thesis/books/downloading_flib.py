import os
import tempfile
import time
import zipfile
import requests
from bs4 import BeautifulSoup

# ?
heads = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}

def downloading_flib(genre_url: str, klass: str, pages: int = 60) -> None:
    main_url = "https://digilibraries.com/"
    for i in range(1, pages + 1):
        time.sleep(0.1)
        os.makedirs(f"booky/{klass}/{klass}_books", exist_ok=True)
        r = requests.get(genre_url + f"?page={i}", headers=heads)
        print("Request",r)
        print(genre_url + f"?page={i}", r.status_code)
        soup = BeautifulSoup(r.text, "html.parser")
        print("Soup", soup)
        books = soup.find_all("div", attrs={"class": "col-lg-2 text-center mb-4 mb-lg-0"})
        print("Books", books)
        for book in books:
            print(main_url + book.get("href"), i)
            time.sleep(0.1)
            try:
                book_page = requests.get(main_url + book.get("href"), headers=heads)
            except requests.exceptions.TooManyRedirects:
                continue
            sup = BeautifulSoup(book_page.text, "html.parser")
            print("Soup text", sup)
            print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
            lnk1 = sup.find("td","href")
            try:
                lnk = lnk1.get("href")
            except AttributeError:
                continue
            print(lnk + " fglbkflndb")
            time.sleep(0.1)
            with tempfile.TemporaryFile() as file:
                    while True:
                        try:
                            download = requests.get(lnk, headers=heads, timeout=10)
                        except requests.exceptions.ConnectionError:
                            print("Waiting 2 minutes...")
                            time.sleep(120)
                            continue
                        else:
                            break
                    file.write(download.content)
                    file.seek(0)  # Reset file pointer to the beginning


genre_url = "https://digilibraries.com/category/poetry"
klass = "Poetry"
pages = 2

downloading_flib(genre_url, klass, pages)





















# import os
# import tempfile
# import time
# import zipfile
# import requests
# from bs4 import BeautifulSoup

# # ?
# heads = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
# }

# def downloading_flib(genre_url: str, klass: str, pages: int = 60) -> None:
#     main_url = "https://flibusta.one"
#     for i in range(1, pages + 1):
#         time.sleep(0.1)
#         os.makedirs(f"booky/{klass}/{klass}_books", exist_ok=True)
#         r = requests.get(genre_url + f"?page={i}", headers=heads)
#         print("Request",r)
#         print(genre_url + f"?page={i}", r.status_code)
#         soup = BeautifulSoup(r.text, "html.parser")
#         print("Soup", soup)
#         books = soup.find_all("a", attrs={"class": "th-in with-mask"})
#         print("Books", books)
#         for book in books:
#             print(main_url + book.get("href"), i)
#             time.sleep(0.1)
#             try:
#                 book_page = requests.get(main_url + book.get("href"), headers=heads)
#             except requests.exceptions.TooManyRedirects:
#                 continue
#             sup = BeautifulSoup(book_page.text, "html.parser")
#             print("Soup text", sup)
#             lnk1 = sup.find("span", class_="link pdf")
#             try:
#                 lnk = lnk1.get("data-link")
#             except AttributeError:
#                 continue
#             print(lnk + " fglbkflndb")
#             time.sleep(0.1)
#             with tempfile.TemporaryFile() as file:
#                 try:
#                     while True:
#                         try:
#                             download_zip = requests.get(lnk, headers=heads, timeout=10)
#                         except requests.exceptions.ConnectionError:
#                             print("Waiting 2 minutes...")
#                             time.sleep(120)
#                             continue
#                         else:
#                             break
#                     file.write(download_zip.content)
#                     file.seek(0)  # Reset file pointer to the beginning
#                     with zipfile.ZipFile(file) as fzip:
#                         fzip.extractall(path=f"booky/{klass}/{klass}_books")
#                 except zipfile.BadZipFile:
#                     print(f"BadZipFile error with link: {lnk}")
#                     continue

# genre_url = "https://flibusta.one/books-genres/89-effektivnost-biznesa/"
# klass = "Business"
# pages = 2

# downloading_flib(genre_url, klass, pages)