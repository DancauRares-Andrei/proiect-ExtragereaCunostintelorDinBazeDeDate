from pymongo import MongoClient
from bson.objectid import ObjectId
import bson
from datetime import datetime
client = MongoClient('mongodb+srv://rares:rares@cluster0.o62zky8.mongodb.net/')

db = client['electronic_db']

produse_collection = db['produse']
clienti_collection = db['clienti']
comenzi_collection = db['comenzi']
produse_collection.drop()
clienti_collection.drop()
comenzi_collection.drop()
def citire_imagine(cale):
    with open(cale, 'rb') as file:
        imagine_binara = bson.Binary(file.read())
    return imagine_binara
produse = [
    {
  "_id": ObjectId("6147f1eefb7a4e60a2e0525d"),
  "nume": "IdeaPad Gaming 3",
  "descriere": "Laptop performant cu procesor puternic și display de înaltă rezoluție.",
  "pret": 3399.99,
  "stoc": 50,
  "disponibil": True,
  "data_adaugare": datetime(2024,1,22,18,27,28),
  "specificatii": {
    "culoare": "Negru",
    "procesor": {
      "producator": "AMD",
      "tip": "Ryzen 5",
      "nuclee": 6,
      "frecventaGHz": 4.5
    },
    "RAM": "16 GB",
    "marca": "Lenovo",
    "altele": ["Touchscreen", "Wi-Fi 6", "Bluetooth 5.0"]
  },
  "imagini": [
    citire_imagine('IdeaPadG3.png'),citire_imagine('IdeaPadG3-2.png')
  ],
  "comentarii": [
    {
      "utilizator": "jane_smith",
      "comentariu": "Foarte mulțumită de performanțele acestui laptop!"
    },
    {
      "utilizator": "alex_brown",
      "comentariu": "Designul este elegant și tastatura este foarte confortabilă."
    }
  ]
},

    {
  "_id": ObjectId("6147f1eefb7a4e60a2e0525e"),
  "nume": "Motorola Moto E22",
  "descriere": "Du-ti experientele cotidiene de vizualizare si ascultare la un alt nivel, cu moto e22.",
  "pret": 350.0,
  "stoc": 100,
  "disponibil": True,
  "data_adaugare": datetime(2024,1,25,12,35,57),
  "specificatii": {
    "culoare": "Gri",
    "procesor": {
      "producator": "MediaTek",
      "tip": "Hello G37",
      "nuclee": 8,
      "frecventaGHz": 2.3
    },
    "RAM": "4 GB",
    "marca": "Motorola",
    "altele": ["4G", "LCD","Baterie 4020 mAh"]
  },
  "imagini": [
    citire_imagine('MOTOE22.png'),citire_imagine('MOTOE22-2.png')
  ],
  "comentarii": [
    {
      "utilizator": "jane_smith",
      "comentariu": "Sunt încântată de calitatea ecranului și de performanțele acestui smartphone!"
    },
    {
      "utilizator": "alex_brown",
      "comentariu": "Bateria ține foarte mult, sunt foarte mulțumit de achiziție."
    }
  ]
},
{
  "_id": ObjectId("6147f1eefb7a4e60a2e0525f"),
  "nume": "Laptop Gaming ASUS TUF A15 FA506NC",
  "descriere": "Pregatit pentru jocuri foarte serioase si oferind un stil complet nou, TUF Gaming A15 este un laptop pentru jocuri foarte performant ce te va ajuta sa fii victorios.",
  "pret": 3799.9,
  "stoc": 100,
  "disponibil": True,
  "data_adaugare": datetime(2024,1,30,13,30,28),
  "specificatii": {
    "culoare": "Negru",
    "procesor": {
      "producator": "AMD",
      "tip": "Ryzen 5",
      "nuclee": 6,
      "frecventaGHz": 4.5
    },
    "RAM":"16 GB",
    "marca": "ASUS",
    "altele": ["15.6 inch", "Adaptor 180W", "Ryzen 5"]
  },
  "imagini": [
    citire_imagine('A15.png'),citire_imagine('A15-2.png')
  ],
  "comentarii": [
    {
      "utilizator": "maria_garcia",
      "comentariu": "Un laptop foarte bun pentru jocuri!"
    },
    {
      "utilizator": "jane_smith",
      "comentariu": "Fiul meu a fost incantat de acest laptop!"
    }
  ]
},

    {
  "_id": ObjectId("6147f1eefb7a4e60a2e05260"),
  "nume": "Samsung Galaxy A04s",
  "descriere": "Extinde-ti vizualizarea la ecranul Infinity-V de 6,5 inch de pe Galaxy A04s si vezi ce ai ratat pana acum.",
  "pret": 534.3,
  "stoc": 150,
  "disponibil": True,
  "data_adaugare": datetime(2024,2,1,12,34,9),
  "specificatii": {
    "culoare": "Negru",
    "procesor": {
      "producator": "Samsung",
      "tip": "Exynos 850",
      "nuclee": 8,
      "frecventaGHz": 2
    },
    "RAM":"3 GB",
    "marca": "Samsung",
    "altele": ["4G", "PLS", "Procesor Octa-Core"]
  },
  "imagini": [
    citire_imagine('A04S.png'),citire_imagine('A04S-2.png')
  ],
  "comentarii": [
    {
      "utilizator": "michael_johnson",
      "comentariu": "Este un smartphone ok."
    },
    {
      "utilizator": "alex_brown",
      "comentariu": "Un cadou bun pentru fiica mea."
    }
  ]
},
{
  "_id": ObjectId("6147f1eefb7a4e60a2e05261"),
  "nume": "Laptop Lenovo V15 G4 IRU",
  "descriere": "V-ati saturat de laptopurile entry-level care nu dispun de instrumentele de care aveti nevoie pentru a conduce o afacere? Laptopul Lenovo V15 Gen 4 are atat caracteristici cat si un pret avantajos.",
  "pret": 2299.9,
  "stoc": 20,
  "disponibil": True,
  "data_adaugare": datetime(2024,2,2,10,10,54),
  "specificatii": {
    "culoare": "Negru",
    "procesor": {
      "producator": "Intel",
      "tip": "i5",
      "nuclee": 8,
      "frecventaGHz": 4.6
    },
    "RAM": "16 GB",
    "marca": "Lenovo",
    "altele": ["Alimentator 65W", "Placa video integrata", "SSD 512 GB"]
  },
  "imagini": [
    citire_imagine('V15.png'),citire_imagine('V15-2.png')
  ],
  "comentarii": [
    {
      "utilizator": "michael_johnson",
      "comentariu": "Este un laptop destul de bun pentru pretul acestuia."
    },
    {
      "utilizator": "alex_brown",
      "comentariu": "I l-am facut cadou sotiei si e foarte multumita!"
    }
  ]
},

    {
  "_id": ObjectId("6147f1eefb7a4e60a2e05262"),
  "nume": "Apple iPhone 13",
  "descriere": "Ecran superstralucitor intr-un design rezistent. Filmari demne de Hollywood, mai usor de realizat ca niciodata.",
  "pret": 3099.9,
  "stoc": 20,
  "disponibil": True,
  "data_adaugare": datetime(2024,2,10,16,43,29),
  "specificatii": {
    "culoare": "Midnight",
    "procesor": {
      "producator": "Apple",
      "tip": "A15 Bionic",
      "nuclee": 6,
      "frecventaGHz": 3.23
    },
    "RAM":"4 GB",
    "marca": "Apple",
    "altele": ["5G", "NFC", "iOS15"]
  },
  "imagini": [
    citire_imagine('I13.png'),citire_imagine('I13-2.png')
  ],
  "comentarii": [
    {
      "utilizator": "maria_garcia",
      "comentariu": "Sunt mereu multumita de produsele acestui brand!"
    },
    {
      "utilizator": "jane_smith",
      "comentariu": "Un produs cu care ma pot mandri cunostintelor!"
    }
  ]
},
{
  "_id": ObjectId("6147f1eefb7a4e60a2e05263"),
  "nume": "Laptop ACEMAGIC",
  "descriere": "Laptop ACEMAGIC cu procesor Intel Alder Lake N 95，pana la 3.4GHz, 16GB, 512Go SSD, 15,6 inch FHD, Windows 11, Intel UHD Graphics, Gri",
  "pret": 1799.8,
  "stoc": 0,
  "disponibil": False,
  "data_adaugare": datetime(2024,2,4,9,20,30),
  "specificatii": {
    "culoare": "Argintiu",
    "procesor": {
      "producator": "Intel",
      "tip": "Alder Lake N95",
      "nuclee": 4,
      "frecventaGHz": 3.4
    },
    "RAM": "16 GB",
    "marca": "ACEMAGIC",
    "altele": ["SSD 2TB","Windows 11","802.11 a/b/g/n/ac"]
  },
  "imagini": [
    citire_imagine('ACEMAGIC.png'),citire_imagine('ACEMAGIC-2.png')
  ],
  "comentarii": [
    {
      "utilizator": "maria_garcia",
      "comentariu": "Chiar daca nu este un nume de renume, este un laptop destul de bun."
    },
    {
      "utilizator": "michael_johnson",
      "comentariu": "Cel mai ieftin laptop de la acest magazin, astept sa fie din nou in stoc."
    }
  ]
},

    {
  "_id": ObjectId("6147f1eefb7a4e60a2e05264"),
  "nume": "Xiaomi Redmi Note 13 Pro+",
  "descriere": "Telefon mobil Xiaomi Redmi Note 13 Pro+, 8GB RAM, 256GB, 5G, Black",
  "pret": 1791.9,
  "stoc": 30,
  "disponibil": True,
  "data_adaugare": datetime(2024,2,14,15,45,19),
  "specificatii": {
    "culoare": "Midnight",
    "procesor": {
      "producator": "MediaTek",
      "tip": "Dimensity 7200 Ultra",
      "nuclee": 8,
      "frecventaGHz": 2.8
    },
    "RAM":"8 GB",
    "marca": "Xiaomi",
    "altele": ["5G", "AMOLED 6.67 inch", "5000 mAh"]
  },
  "imagini": [
    citire_imagine('NOTE13.png'),citire_imagine('NOTE13-2.png')
  ],
  "comentarii": [
    {
      "utilizator": "michael_johnson",
      "comentariu": "Pentru un brand chinezesc, este ok."
    },
    {
      "utilizator": "alex_brown",
      "comentariu": "E ok, nu am foarte mult de zis."
    }
  ]
},

    {
  "_id": ObjectId("6147f1eefb7a4e60a2e05268"),
  "nume": "Laptop Gaming ASUS ROG Strix SCAR 17 G733PY",
  "descriere": "Atinge apogeul jocurilor cu modelul 2023 Strix SCAR 17, cu un procesor AMD pana la Ryzen™ 9 7945HX si o placa grafica pana la NVIDIA® GeForce RTX™ 4090 Laptop GPU.",
  "pret": 15000.0,
  "stoc": 1,
  "disponibil": True,
  "data_adaugare": datetime(2024,4,4,19,2,30),
  "specificatii": {
    "culoare": "Negru",
    "procesor": {
      "producator": "AMD",
      "tip": "Ryzen 9",
      "nuclee": 16,
      "frecventaGHz": 5.4
    },
    "RAM": "32 GB",
    "marca": "ASUS",
    "altele": ["Adaptor 330W","SSD 1 TB","RTX 4090"]
  },
  "imagini": [
    citire_imagine('SCAR.png'),citire_imagine('SCAR-2.png')
  ],
  "comentarii": [
    {
      "utilizator": "john_doe",
      "comentariu": "Cel mai tare laptop!"
    },
    {
      "utilizator": "maria_garcia",
      "comentariu": "Mi-as dori sa am acest laptop, dar nu-mi permite bugetul."
    }
  ]
}
]

produse_collection.insert_many(produse)

clienti = [
  {
    "_id": ObjectId("6247f1eefb7a4e60a2e0525d"),
    "nume": "Doe",
    "prenume": "John",
    "email": "john.doe@example.com",
    "telefon": "123456789",
    "adresa": {
      "strada": "Str. Primaverii",
      "oras": "Bucuresti",
      "judet": "Bucuresti",
      "cod_postal": "010101"
    }
  },
  {
    "_id": ObjectId("6247f1eefb7a4e60a2e0525e"),
    "nume": "Smith",
    "prenume": "Jane",
    "email": "jane.smith@example.com",
    "telefon": "987654321",
    "adresa": {
      "strada": "Str. Florilor",
      "oras": "Cluj-Napoca",
      "judet": "Cluj",
      "cod_postal": "400000"
    }
  },
  {
    "_id": ObjectId("6247f1eefb7a4e60a2e0525f"),
    "nume": "Brown",
    "prenume": "Alex",
    "email": "alex.brown@example.com",
    "telefon": "456789123",
    "adresa": {
      "strada": "Str. Libertatii",
      "oras": "Iasi",
      "judet": "Iasi",
      "cod_postal": "700000"
    }
  },
  {
    "_id": ObjectId("6247f1eefb7a4e60a2e05260"),
    "nume": "Garcia",
    "prenume": "Maria",
    "email": "maria.garcia@example.com",
    "telefon": "369258147",
    "adresa": {
      "strada": "Str. Independentei",
      "oras": "Timisoara",
      "judet": "Timis",
      "cod_postal": "300000"
    }
  },
  {
    "_id": ObjectId("6247f1eefb7a4e60a2e05261"),
    "nume": "Johnson",
    "prenume": "Michael",
    "email": "michael.johnson@example.com",
    "telefon": "147258369",
    "adresa": {
      "strada": "Str. Revolutiei",
      "oras": "Constanta",
      "judet": "Constanta",
      "cod_postal": "900000"
    }
  }
]

clienti_collection.insert_many(clienti)

comenzi = [
    {
    "_id": ObjectId("6347f1eefb7a4e60a2e0525d"),
    "email_client":"jane.smith@example.com",
    "produse": [
      {
        "nume_produs":"IdeaPad Gaming 3",
        "cantitate": 2
      },
      {
        "nume_produs":"Motorola Moto E22",
        "cantitate": 3
      },
    ],
    "data_comanda": datetime(2024,3,2,12,35,57),
    "adresa_livrare": {
      "strada": "Str. Florilor",
      "oras": "Cluj-Napoca",
      "judet": "Cluj",
      "cod_postal": "400000"
    },
    "status": "Livrată"
  },
  {
    "_id": ObjectId("6347f1eefb7a4e60a2e0525e"),
    "email_client": "alex.brown@example.com",
    "produse": [
      {
        "nume_produs": "IdeaPad Gaming 3",
        "cantitate": 3
      },
      {
        "nume_produs": "Motorola Moto E22",
        "cantitate": 5
      }
    ],
    "data_comanda": datetime(2024,3,3,14,53,17),
    "adresa_livrare": {
      "strada": "Str. Libertatii",
      "oras": "Iasi",
      "judet": "Iasi",
      "cod_postal": "700000"
    },
    "status": "Livrată"
  },
  {
    "_id": ObjectId("6347f1eefb7a4e60a2e0525f"),
    "email_client": "maria.garcia@example.com",
    "produse": [
      {
        "nume_produs": "Laptop Gaming ASUS TUF A15 FA506NC",
        "cantitate": 1
      },
      {
        "nume_produs": "Apple iPhone 13",
        "cantitate": 2
      }
    ],
    "data_comanda": datetime(2024,3,4,11,30,10),
    "adresa_livrare": {
      "strada": "Str. Independentei",
      "oras": "Timisoara",
      "judet": "Timis",
      "cod_postal": "300000"
    },
    "status": "Anulată"
  },
  {
    "_id": ObjectId("6347f1eefb7a4e60a2e05260"),
    "email_client": "jane.smith@example.com",
    "produse": [
      {
        "nume_produs": "Laptop Gaming ASUS TUF A15 FA506NC",
        "cantitate": 1
      },
      {
        "id_produs": "Apple iPhone 13",
        "cantitate": 3
      }
    ],
    "data_comanda": datetime(2024,3,5,9,25,42),
    "adresa_livrare": {
      "strada": "Str. Revolutiei",
      "oras": "Cluj-Napoca",
      "judet": "Cluj",
      "cod_postal": "400200"
    },
    "status": "Livrată"
  },
  {
    "_id": ObjectId("6347f1eefb7a4e60a2e05261"),
    "email_client": "alex.brown@example.com",
    "produse": [
      {
        "nume_produs": "Samsung Galaxy A04s",
        "cantitate": 2
      },
      {
        "nume_produs": "Laptop Lenovo V15 G4 IRU",
        "cantitate": 1
      }
    ],
    "data_comanda": datetime(2024,3,7,15,35,32),
    "adresa_livrare": {
      "strada": "Str. Independentei",
      "oras": "Iasi",
      "judet": "Iasi",
      "cod_postal": "700030"
    },
    "status": "În așteptare"
  },
  {
    "_id": ObjectId("6347f1eefb7a4e60a2e05262"),
    "email_client": "michael.johnson@example.com",
    "produse": [
      {
        "nume_produs": "Samsung Galaxy A04s",
        "cantitate": 3
      },
      {
        "id_produs": "Laptop Lenovo V15 G4 IRU",
        "cantitate": 3
      }
    ],
    "data_comanda": datetime(2024,3,17,12,3,15),
    "adresa_livrare": {
      "strada": "Str. Revolutiei",
      "oras": "Constanta",
      "judet": "Constanta",
      "cod_postal": "900000"
    },
    "status": "În așteptare"
  },
  {
    "_id": ObjectId("6347f1eefb7a4e60a2e05263"),
    "email_client": "maria.garcia@example.com",
    "produse": [
      {
        "nume_produs": "Laptop ACEMAGIC",
        "cantitate": 1
      }
    ],
    "data_comanda": datetime(2024,3,19,16,37,24),
    "adresa_livrare": {
      "strada": "Str. Libertatii",
      "oras": "Cluj-Napoca",
      "judet": "Cluj",
      "cod_postal": "400000"
    },
    "status": "În așteptare"
  },
  {
    "_id": ObjectId("6347f1eefb7a4e60a2e05264"),
    "email_client": "alex.brown@example.com",
    "produse": [
      {
        "nume_produs": "Xiaomi Redmi Note 13 Pro+",
        "cantitate": 2
      }
    ],
    "data_comanda": datetime(2024,3,22,13,40,12),
    "adresa_livrare": {
      "strada": "Str. Florilor",
      "oras": "Cluj-Napoca",
      "judet": "Cluj",
      "cod_postal": "400000"
    },
    "status": "În așteptare"
  },
  {
    "_id": ObjectId("6347f1eefb7a4e60a2e05265"),
    "email_client": "michael.johnson@example.com",
    "produse": [
      {
        "nume_produs": "Laptop ACEMAGIC",
        "cantitate": 2
      },
      {
        "nume_produs": "Xiaomi Redmi Note 13 Pro+",
        "cantitate": 1
      }
    ],
    "data_comanda": datetime(2024,3,23,10,15,31),
    "adresa_livrare": {
      "strada": "Str. Independentei",
      "oras": "Timisoara",
      "judet": "Timis",
      "cod_postal": "300000"
    },
    "status": "În așteptare"
  },
  {
    "_id": ObjectId("6347f1eefb7a4e60a2e05266"),
    "email_client": "maria.garcia@example.com",
    "produse": [
      {
        "nume_produs": "Laptop Gaming ASUS TUF A15 FA506NC",
        "cantitate": 2
      },
      {
        "nume_produs": "Apple iPhone 13",
        "cantitate": 1
      }
    ],
    "data_comanda": datetime(2024,3,31,15,35,32),
    "adresa_livrare": {
      "strada": "Str. Independentei",
      "oras": "Timisoara",
      "judet": "Timis",
      "cod_postal": "300000"
    },
    "status": "În așteptare"
  },
  {
    "_id": ObjectId("6347f1eefb7a4e60a2e0526f"),
    "email_client": "alex.brown@example.com",
    "produse": [
      {
        "nume_produs": "Apple iPhone 13",
        "cantitate": 2
      }
    ],
    "data_comanda": datetime(2024,4,1,12,20,12),
    "adresa_livrare": {
      "strada": "Str. Florilor",
      "oras": "Cluj-Napoca",
      "judet": "Cluj",
      "cod_postal": "400000"
    },
    "status": "În așteptare"
  }
]
comenzi_collection.insert_many(comenzi)

produse_collection.update_one({ 'pret': 3399.99 }, { '$set': { 'stoc': 45 } })
clienti_collection.update_one({ 'prenume': 'Jane' }, { '$set': { 'telefon': "987651234" } })
comenzi_collection.update_one({ 'status': 'În așteptare' }, { '$set': { 'status': "Livrată" } })

produse_collection.delete_one({ 'descriere':"Atinge apogeul jocurilor cu modelul 2023 Strix SCAR 17, cu un procesor AMD pana la Ryzen™ 9 7945HX si o placa grafica pana la NVIDIA® GeForce RTX™ 4090 Laptop GPU."})
clienti_collection.delete_one({ 'prenume': 'John', 'nume': 'Doe' })
comenzi_collection.delete_one({ "email_client": "alex.brown@example.com", "status": "În așteptare", "data_comanda": datetime(2024,4,1,12,20,12) })

produse_collection.update_one({"nume": "Xiaomi Redmi Note 13 Pro+", "comentarii.utilizator": "alex_brown"},{"$set": {"comentarii.$.comentariu": "Comentariu actualizat"}})
clienti_collection.update_one({"email":"michael.johnson@example.com"}, {"$set": {"adresa.judet": "Bacău"}})
comenzi_collection.update_one({"email_client":"maria.garcia@example.com","data_comanda": datetime(2024,3,31,15,35,32)},{"$set": {"adresa_livrare.oras": "Bacău"}})

