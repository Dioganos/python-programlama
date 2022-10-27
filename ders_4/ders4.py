"""                                              Ders-4                                                              """

"""

import csv

with open('iris.data', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row[""])

"""

import csv

baslik = ["sicaklik","nem","basinc"]

veri = [[30,75.5,10],[32.3,50,3]]

with open('sensor_veri.csv','w',encoding="UTF8",newline='') as f:
    writer = csv.writer(f)
    writer.writerow(baslik)
    #writer.writerows(veri)
    for i in veri:
        writer.writerow(i)