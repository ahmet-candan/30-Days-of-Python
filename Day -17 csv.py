import csv

def arama(user_id = None,email = None):
    with open("data.csv","r") as csfile:
        reader = csv.DictReader(csfile)
        for i in reader:
            if user_id is not None and email is not None:
                if user_id == i.get("id") and email == i.get("email"):
                    return i
            else:
                return "Lütfen geçerli değerler giriniz"

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

#bilgi_ekle("data.csv","ahmet candan","ghost1234@gmail.com")
arama(user_id=2,email="ghost1234@gmail.com")
