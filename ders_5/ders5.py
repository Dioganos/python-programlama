import csv
import os
import zipfile
import pandas as pd
import sqlite3

yol = "C:/Users/emirc/Documents/GitHub/python-programlama/python-programlama/ders_5/Veri"
if not os.path.exists(yol):
    os.makedirs(yol)
with zipfile.ZipFile("../ders_10/pariteler_cikti_1hour_2022_2022.zip", "r") as zip_ref:
    zip_ref.extractall(yol)

dir_list = os.listdir(yol)
deger = []
with open("veri.csv",'w',encoding="UTF8",newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["otime","open","high","low","close","volume","parite"])
    for csv_dosya in dir_list:
        veriler = pd.read_csv("Veri/"+ csv_dosya)
        del veriler["volume"]

        for veri in veriler.values:
            for x in range(0,6):
                if deger[x]:
                    pass
            break
        break

"""
bag = sqlite3.connect("kripto.db")
cursor = bag.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS parite("
               +"id INTEGER PRIMARY KEY AUTOINCREMENT,"
               +" otime TEXT, open FLOAT,"
               +" high FLOAT, low FLOAT, close FLOAT);")



bag.commit()
bag.close()

"""