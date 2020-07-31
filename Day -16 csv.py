import csv
def satır_sayisi(dosya_ismi):
    with open(dosya_ismi,"r")as csv_read:
        reader = csv.reader(csv_read)
        reader =list(reader)
        return len(reader)

def bilgi_ekle(dosya_ismi,name,email):
    fieldnames = ["id","name","email"]
    nextid = satır_sayisi(dosya_ismi)

    with open(dosya_ismi,"a") as csvfile:
        writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
        writer.writerow({
            "id":nextid,
            "name":name,
            "email": email
        })

bilgi_ekle("data.csv","ahmet candan","ghost1234@gmail.com")
