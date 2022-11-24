import csv
import os
import json

PATH = "messages/"
NEWPATH = "yourdata/"
fromPy = open("from.py",'r')
exec(fromPy.read())
fromPy.close()

header = ["ID","Timestamp","Contents","Attachments","Channel"]

samecounter = 0
for file in os.listdir(PATH):
    d = os.path.join(PATH,file)
    if "index.json" not in d:
        with open(d+"/messages.csv",'r', newline='',encoding='utf8') as csvfile:
            reader = csv.DictReader(csvfile)
            if file in unknownMessages:
                samecounter += 1
                values = []
                with open(NEWPATH+"unknown{}.csv".format(str(samecounter)),'w',newline='',encoding="utf8") as newU:
                    writerU = csv.writer(newU)
                    writerU.writerow(header)
                    for row in reader:
                        values.append([row[header[0]],row[header[1]],row[header[2]],row[header[3]],"Unknown"])
                    writerU.writerows(values)
                    newU.close()
            if file in userMessages:
                values = []
                try:
                    with open(NEWPATH + "{}".format(data[file[1:]][20:]) + ".csv", 'w', newline='', encoding="utf8") as newU:
                        writerU = csv.writer(newU)
                        writerU.writerow(header)
                        for row in reader:
                            values.append([row[header[0]], row[header[1]], row[header[2]], row[header[3]], data[file[1:]]])
                        writerU.writerows(values)
                except (Exception):
                    with open(NEWPATH + "{}".format(data[file[1:]][-5:]) + ".csv", 'w', newline='', encoding="utf8") as newU:
                        writerU = csv.writer(newU)
                        writerU.writerow(header)
                        for row in reader:
                            values.append([row[header[0]], row[header[1]], row[header[2]], row[header[3]], data[file[1:]]])
                        writerU.writerows(values)


            if file in serverMessages:
                channels = open(d+"/channel.json",encoding="utf8")
                channeldata = json.load(channels)
                try:
                    print("{} : {}".format(channeldata["guild"]["name"], channeldata["name"]))
                except(Exception):
                    pass

                try:
                    header = ["ID", "Timestamp", "Contents", "Attachments", "Channel", "Room"]
                    values = []
                    with open(NEWPATH + "{}_{}".format(channeldata["guild"]["name"], channeldata["name"]) + ".csv", 'w', newline='',
                              encoding="utf8") as newU:
                        writerU = csv.writer(newU)
                        writerU.writerow(header)
                        for row in reader:
                            values.append([row[header[0]], row[header[1]], row[header[2]], row[header[3]], "{}".format(channeldata["guild"]["name"]), channeldata["name"]])
                        writerU.writerows(values)
                        newU.close()
                except(Exception):
                    header = ["ID", "Timestamp", "Contents", "Attachments", "Channel", "Room"]
                    values = []
                    with open(NEWPATH + "{}".format(channeldata["name"]) + ".csv", 'w',
                              newline='',
                              encoding="utf8") as newU:
                        writerU = csv.writer(newU)
                        writerU.writerow(header)
                        for row in reader:
                            values.append(
                                [row[header[0]], row[header[1]], row[header[2]], row[header[3]],channeldata["name"], None])
                        writerU.writerows(values)
                        newU.close()