import csv
import os

PATH = "./messages/"
if not os.path.exists("yourData"):
    os.mkdir("yourData")
    print("olustu")

for file in os.listdir(PATH):
    d = os.path.join(PATH,file)
    if "index.json" not in d:
        with open(d+"/messages.csv", newline='',encoding='utf8') as csvfile:
            reader = csv.DictReader(csvfile)
            x = []
            y = ""
            for row in reader:
                x.append(row["Timestamp"] + " : " + row["Contents"] + " : " + row["Attachments"] + "\n")
            x.reverse()
            for i in range(len(x)):
                y += x[i]

            doc = open("yourData/" + row["Timestamp"][0:11] + ".txt", 'w', encoding='utf8')
            print(y,file=doc)