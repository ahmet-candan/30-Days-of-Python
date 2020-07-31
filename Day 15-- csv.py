import csv
with open("data.csv","w+",encoding ="UTF-8") as cvsfile:
    writers = csv.writer(cvsfile)
    writers.writerow(["Başlık","Tanımı","Burada",23])
    writers.writerow(["Satır","1","2"])  

with open("data.csv","a",encoding ="UTF-8") as cvsfile:
    writers = csv.writer(cvsfile)
    writers.writerow(["Başlık","Tanımı","Burada",23])
    writers.writerow(["Satır","1","2"]) 
      
with open("data.csv","r",encoding ="UTF-8") as csvfile:
    reader = csv.reader(csvfile)
    for i in reader:
        print(i)

with open("data.csv","r",encoding ="UTF-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for i in reader:
        print(i)


    