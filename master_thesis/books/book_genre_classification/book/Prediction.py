import os
# import warnings
import pickle
import pandas as pd
from PyPDF2 import PdfReader
from joblib import load
# warnings.simplefilter("ignore")
# import contextlib

from .ru_genres import ru_genres

def predict():
    folder_path = "./uploads"
    # print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    files = os.listdir(folder_path)
    files_modif = {}
    for file in files:
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):
            mod_files = os.path.getmtime(file_path)
            files_modif[file] = mod_files
    latest_file = max(files_modif, key=files_modif.get)
    print("--------Upload file---------", latest_file)
    text = ""
    with open(f"./uploads/{latest_file}", "rb") as filehandle:
        # with contextlib.redirect_stderr(open(os.devnull, "w")):
        pdf = PdfReader(filehandle)
        pages = len(pdf.pages)
        for i in range(pages):
            page = pdf.pages[i]
            text += page.extract_text().strip()    
    vectorizer = load(f'book/vectorize_sgd1_678.joblib')
    with open("book/sgd1_678.pkl", 'rb') as file:
        pickle_model = pickle.load(file)
    X_pred = pd.Series(text)
    X_pred_vec = vectorizer.transform(X_pred)
    pred = pickle_model.predict(X_pred_vec)
    # կուրսայինի համար ֊֊֊
    print("Your book genre is: ", ru_genres.get(pred[0]))
    #  ֊֊֊֊
    return pred[0]
