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
      "nuclee": 6
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
      "comentariu": "Foarte mulțumit de performanțele acestui laptop!"
    },
    {
      "utilizator": "alex_brown",
      "comentariu": "Designul este elegant și tastatura este foarte confortabilă."
    }
  ]
},

    {
  "_id": ObjectId("6147f1eefb7a4e60a2e0525e"),
  "nume": "Smartphone Samsung",
  "descriere": "Smartphone performant cu cameră foto de înaltă calitate și ecran vibrant.",
  "pret": 1500.0,
  "stoc": 100,
  "disponibil": True,
  "data_adaugare": datetime.utcnow(),
  "specificatii": {
    "culoare": "Albastru",
    "dimensiuni": {
      "lungime": 15.2,
      "latime": 7.1,
      "inaltime": 0.8
    },
    "greutate": 0.2,
    "marca": "Samsung",
    "altele": ["5G", "Amoled Display", "Procesor Octa-Core"]
  },
  "imagini": [
    "<binary data 1>",
    "<binary data 2>",
    "<binary data 3>"
  ],
  "comentarii": [
    {
      "utilizator": "maria_23",
      "comentariu": "Sunt încântată de calitatea ecranului și de performanțele acestui smartphone!"
    },
    {
      "utilizator": "alex_87",
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
      "nuclee": 6
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
  "nume": "Smartphone Samsung",
  "descriere": "Smartphone performant cu cameră foto de înaltă calitate și ecran vibrant.",
  "pret": 1500.0,
  "stoc": 100,
  "disponibil": True,
  "data_adaugare": datetime.utcnow(),
  "specificatii": {
    "culoare": "Albastru",
    "dimensiuni": {
      "lungime": 15.2,
      "latime": 7.1,
      "inaltime": 0.8
    },
    "greutate": 0.2,
    "marca": "Samsung",
    "altele": ["5G", "Amoled Display", "Procesor Octa-Core"]
  },
  "imagini": [
    "<binary data 1>",
    "<binary data 2>",
    "<binary data 3>"
  ],
  "comentarii": [
    {
      "utilizator": "maria_23",
      "comentariu": "Sunt încântată de calitatea ecranului și de performanțele acestui smartphone!"
    },
    {
      "utilizator": "alex_87",
      "comentariu": "Bateria ține foarte mult, sunt foarte mulțumit de achiziție."
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
      "nuclee": 8
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
  "nume": "Smartphone Samsung",
  "descriere": "Smartphone performant cu cameră foto de înaltă calitate și ecran vibrant.",
  "pret": 1500.0,
  "stoc": 100,
  "disponibil": True,
  "data_adaugare": datetime.utcnow(),
  "specificatii": {
    "culoare": "Albastru",
    "dimensiuni": {
      "lungime": 15.2,
      "latime": 7.1,
      "inaltime": 0.8
    },
    "greutate": 0.2,
    "marca": "Samsung",
    "altele": ["5G", "Amoled Display", "Procesor Octa-Core"]
  },
  "imagini": [
    "<binary data 1>",
    "<binary data 2>",
    "<binary data 3>"
  ],
  "comentarii": [
    {
      "utilizator": "maria_23",
      "comentariu": "Sunt încântată de calitatea ecranului și de performanțele acestui smartphone!"
    },
    {
      "utilizator": "alex_87",
      "comentariu": "Bateria ține foarte mult, sunt foarte mulțumit de achiziție."
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
      "nuclee": 4
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
  "nume": "Smartphone Samsung",
  "descriere": "Smartphone performant cu cameră foto de înaltă calitate și ecran vibrant.",
  "pret": 1500.0,
  "stoc": 100,
  "disponibil": True,
  "data_adaugare": datetime.utcnow(),
  "specificatii": {
    "culoare": "Albastru",
    "dimensiuni": {
      "lungime": 15.2,
      "latime": 7.1,
      "inaltime": 0.8
    },
    "greutate": 0.2,
    "marca": "Samsung",
    "altele": ["5G", "Amoled Display", "Procesor Octa-Core"]
  },
  "imagini": [
    "in lucru"
  ],
  "comentarii": [
    {
      "utilizator": "maria_23",
      "comentariu": "Sunt încântată de calitatea ecranului și de performanțele acestui smartphone!"
    },
    {
      "utilizator": "alex_87",
      "comentariu": "Bateria ține foarte mult, sunt foarte mulțumit de achiziție."
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
      "nuclee": 16
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
    "nume": "John",
    "prenume": "Doe",
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
    "nume": "Jane",
    "prenume": "Smith",
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
    "nume": "Alex",
    "prenume": "Brown",
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
    "nume": "Maria",
    "prenume": "Garcia",
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
    "nume": "Michael",
    "prenume": "Johnson",
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
    "id_client": ObjectId("6247f1eefb7a4e60a2e0525d"),
    "produse": [
      {
        "id_produs": ObjectId("6247f1eefb7a4e60a2e0525e"),
        "cantitate": 2
      }
    ],
    "data_comanda": "2024-03-29T12:00:00Z",
    "adresa_livrare": {
      "strada": "Str. Libertatii",
      "oras": "Cluj-Napoca",
      "judet": "Cluj",
      "cod_postal": "400000"
    },
    "status": "În așteptare"
  },
  {
    "_id": ObjectId("6347f1eefb7a4e60a2e0525e"),
    "id_client": ObjectId("6247f1eefb7a4e60a2e0525e"),
    "produse": [
      {
        "id_produs": ObjectId("6147f1eefb7a4e60a2e0525d"),
        "cantitate": 3
      }
    ],
    "data_comanda": "2024-03-29T12:15:00Z",
    "adresa_livrare": {
      "strada": "Str. Revolutiei",
      "oras": "Timisoara",
      "judet": "Timis",
      "cod_postal": "300000"
    },
    "status": "Onorată"
  },
  {
    "_id": ObjectId("6347f1eefb7a4e60a2e0525f"),
    "id_client": ObjectId("6247f1eefb7a4e60a2e0525f"),
    "produse": [
      {
        "id_produs": ObjectId("6147f1eefb7a4e60a2e0525f"),
        "cantitate": 1
      }
    ],
    "data_comanda": "2024-03-29T12:30:00Z",
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
    "id_client": ObjectId("6247f1eefb7a4e60a2e05260"),
    "produse": [
      {
        "id_produs": ObjectId("6147f1eefb7a4e60a2e0525e"),
        "cantitate": 1
      },
      {
        "id_produs": ObjectId("6247f1eefb7a4e60a2e0525d"),
        "cantitate": 2
      }
    ],
    "data_comanda": "2024-03-29T12:45:00Z",
    "adresa_livrare": {
      "strada": "Str. Florilor",
      "oras": "Cluj-Napoca",
      "judet": "Cluj",
      "cod_postal": "400000"
    },
    "status": "În așteptare"
  },
  {
    "_id": ObjectId("6347f1eefb7a4e60a2e05261"),
    "id_client": ObjectId("6247f1eefb7a4e60a2e05261"),
    "produse": [
      {
        "id_produs": ObjectId("6147f1eefb7a4e60a2e0525f"),
        "cantitate": 2
      },
      {
        "id_produs": ObjectId("6247f1eefb7a4e60a2e05260"),
        "cantitate": 1
      }
    ],
    "data_comanda": "2024-03-29T13:00:00Z",
    "adresa_livrare": {
      "strada": "Str. Independentei",
      "oras": "Timisoara",
      "judet": "Timis",
      "cod_postal": "300000"
    },
    "status": "În așteptare"
  },
  {
    "_id": ObjectId("6347f1eefb7a4e60a2e05262"),
    "id_client": ObjectId("6247f1eefb7a4e60a2e05262"),
    "produse": [
      {
        "id_produs": ObjectId("6147f1eefb7a4e60a2e0525e"),
        "cantitate": 3
      }
    ],
    "data_comanda": "2024-03-29T13:15:00Z",
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
    "id_client": ObjectId("6247f1eefb7a4e60a2e05263"),
    "produse": [
      {
        "id_produs": ObjectId("6147f1eefb7a4e60a2e0525d"),
        "cantitate": 1
      },
      {
        "id_produs": ObjectId("6247f1eefb7a4e60a2e0525e"),
        "cantitate": 1
      }
    ],
    "data_comanda": "2024-03-29T13:30:00Z",
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
    "id_client": ObjectId("6247f1eefb7a4e60a2e05264"),
    "produse": [
      {
        "id_produs": ObjectId("6147f1eefb7a4e60a2e0525f"),
        "cantitate": 2
      }
    ],
    "data_comanda": "2024-03-29T13:45:00Z",
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
    "id_client": ObjectId("6247f1eefb7a4e60a2e05265"),
    "produse": [
      {
        "id_produs": ObjectId("6147f1eefb7a4e60a2e0525d"),
        "cantitate": 2
      },
      {
        "id_produs": ObjectId("6247f1eefb7a4e60a2e0525e"),
        "cantitate": 3
      }
    ],
    "data_comanda": "2024-03-29T14:00:00Z",
    "adresa_livrare": {
      "strada": "Str. Revolutiei",
      "oras": "Timisoara",
      "judet": "Timis",
      "cod_postal": "300000"
    },
    "status": "În așteptare"
  },
  {
    "_id": ObjectId("6347f1eefb7a4e60a2e05266"),
    "id_client": ObjectId("6247f1eefb7a4e60a2e05266"),
    "produse": [
      {
        "id_produs": ObjectId("6147f1eefb7a4e60a2e0525e"),
        "cantitate": 1
      },
      {
        "id_produs": ObjectId("6247f1eefb7a4e60a2e0525f"),
        "cantitate": 1
      }
    ],
    "data_comanda": "2024-03-29T14:15:00Z",
    "adresa_livrare": {
      "strada": "Str. Independentei",
      "oras": "Timisoara",
      "judet": "Timis",
      "cod_postal": "300000"
    },
    "status": "În așteptare"
  },
      {
    "_id": ObjectId("6348f1eefb7a4e60a2e0524d"),
    "id_client": ObjectId("6247f1eefb7a4e60a2e0525d"),
    "produse": [
      {
        "id_produs": ObjectId("6247f1eefb7a4e60a2e0525e"),
        "cantitate": 2
      }
    ],
    "data_comanda": "2024-03-29T12:00:00Z",
    "adresa_livrare": {
      "strada": "Str. Libertatii",
      "oras": "Cluj-Napoca",
      "judet": "Cluj",
      "cod_postal": "400000"
    },
    "status": "În așteptare"
  },
  {
    "_id": ObjectId("6348f1eefb7a4e60a2e0525e"),
    "id_client": ObjectId("6247f1eefb7a4e60a2e0525e"),
    "produse": [
      {
        "id_produs": ObjectId("6147f1eefb7a4e60a2e0525d"),
        "cantitate": 3
      }
    ],
    "data_comanda": "2024-03-29T12:15:00Z",
    "adresa_livrare": {
      "strada": "Str. Revolutiei",
      "oras": "Timisoara",
      "judet": "Timis",
      "cod_postal": "300000"
    },
    "status": "Onorată"
  },
  {
    "_id": ObjectId("6348f1eefb7a4e60a2e0525f"),
    "id_client": ObjectId("6247f1eefb7a4e60a2e0525f"),
    "produse": [
      {
        "id_produs": ObjectId("6147f1eefb7a4e60a2e0525f"),
        "cantitate": 1
      }
    ],
    "data_comanda": "2024-03-29T12:30:00Z",
    "adresa_livrare": {
      "strada": "Str. Independentei",
      "oras": "Timisoara",
      "judet": "Timis",
      "cod_postal": "300000"
    },
    "status": "Anulată"
  },
  {
    "_id": ObjectId("6348f1eefb7a4e60a2e05260"),
    "id_client": ObjectId("6247f1eefb7a4e60a2e05260"),
    "produse": [
      {
        "id_produs": ObjectId("6147f1eefb7a4e60a2e0525e"),
        "cantitate": 1
      },
      {
        "id_produs": ObjectId("6247f1eefb7a4e60a2e0525d"),
        "cantitate": 2
      }
    ],
    "data_comanda": "2024-03-29T12:45:00Z",
    "adresa_livrare": {
      "strada": "Str. Florilor",
      "oras": "Cluj-Napoca",
      "judet": "Cluj",
      "cod_postal": "400000"
    },
    "status": "În așteptare"
  },
  {
    "_id": ObjectId("6348f1eefb7a4e60a2e05261"),
    "id_client": ObjectId("6247f1eefb7a4e60a2e05261"),
    "produse": [
      {
        "id_produs": ObjectId("6147f1eefb7a4e60a2e0525f"),
        "cantitate": 2
      },
      {
        "id_produs": ObjectId("6247f1eefb7a4e60a2e05260"),
        "cantitate": 1
      }
    ],
    "data_comanda": "2024-03-29T13:00:00Z",
    "adresa_livrare": {
      "strada": "Str. Independentei",
      "oras": "Timisoara",
      "judet": "Timis",
      "cod_postal": "300000"
    },
    "status": "În așteptare"
  },
  {
    "_id": ObjectId("6348f1eefb7a4e60a2e05262"),
    "id_client": ObjectId("6247f1eefb7a4e60a2e05262"),
    "produse": [
      {
        "id_produs": ObjectId("6147f1eefb7a4e60a2e0525e"),
        "cantitate": 3
      }
    ],
    "data_comanda": "2024-03-29T13:15:00Z",
    "adresa_livrare": {
      "strada": "Str. Revolutiei",
      "oras": "Constanta",
      "judet": "Constanta",
      "cod_postal": "900000"
    },
    "status": "În așteptare"
  },
  {
    "_id": ObjectId("6348f1eefb7a4e60a2e05263"),
    "id_client": ObjectId("6247f1eefb7a4e60a2e05263"),
    "produse": [
      {
        "id_produs": ObjectId("6147f1eefb7a4e60a2e0525d"),
        "cantitate": 1
      },
      {
        "id_produs": ObjectId("6247f1eefb7a4e60a2e0525e"),
        "cantitate": 1
      }
    ],
    "data_comanda": "2024-03-29T13:30:00Z",
    "adresa_livrare": {
      "strada": "Str. Libertatii",
      "oras": "Cluj-Napoca",
      "judet": "Cluj",
      "cod_postal": "400000"
    },
    "status": "În așteptare"
  },
  {
    "_id": ObjectId("6348f1eefb7a4e60a2e05264"),
    "id_client": ObjectId("6247f1eefb7a4e60a2e05264"),
    "produse": [
      {
        "id_produs": ObjectId("6147f1eefb7a4e60a2e0525f"),
        "cantitate": 2
      }
    ],
    "data_comanda": "2024-03-29T13:45:00Z",
    "adresa_livrare": {
      "strada": "Str. Florilor",
      "oras": "Cluj-Napoca",
      "judet": "Cluj",
      "cod_postal": "400000"
    },
    "status": "În așteptare"
  },
  {
    "_id": ObjectId("6348f1eefb7a4e60a2e05265"),
    "id_client": ObjectId("6247f1eefb7a4e60a2e05265"),
    "produse": [
      {
        "id_produs": ObjectId("6147f1eefb7a4e60a2e0525d"),
        "cantitate": 2
      },
      {
        "id_produs": ObjectId("6247f1eefb7a4e60a2e0525e"),
        "cantitate": 3
      }
    ],
    "data_comanda": "2024-03-29T14:00:00Z",
    "adresa_livrare": {
      "strada": "Str. Revolutiei",
      "oras": "Timisoara",
      "judet": "Timis",
      "cod_postal": "300000"
    },
    "status": "În așteptare"
  },
  {
    "_id": ObjectId("6348f1eefb7a4e60a2e05266"),
    "id_client": ObjectId("6247f1eefb7a4e60a2e05266"),
    "produse": [
      {
        "id_produs": ObjectId("6147f1eefb7a4e60a2e0525e"),
        "cantitate": 1
      },
      {
        "id_produs": ObjectId("6247f1eefb7a4e60a2e0525f"),
        "cantitate": 1
      }
    ],
    "data_comanda": "2024-03-29T14:15:00Z",
    "adresa_livrare": {
      "strada": "Str. Independentei",
      "oras": "Timisoara",
      "judet": "Timis",
      "cod_postal": "300000"
    },
    "status": "În așteptare"
  }
]
comenzi_collection.insert_many(comenzi)

produse_collection.update_one({ 'nume': 'Laptop Dell' }, { '$set': { 'stoc': 45 } })
clienti_collection.update_one({ 'nume': 'Jane' }, { '$set': { 'telefon': "987651234" } })
comenzi_collection.update_one({ 'status': 'În așteptare' }, { '$set': { 'status': "Onorată" } })

produse_collection.delete_one({ '_id': ObjectId('6147f1eefb7a4e60a2e05268')})#De facut dupa atribute
clienti_collection.delete_one({ 'nume': 'John', 'prenume': 'Doe' })
comenzi_collection.delete_one({ "_id": ObjectId("6348f1eefb7a4e60a2e05266"), "status": "În așteptare" })#De facut dupa atribute

produse_collection.update_one({"_id": ObjectId("6147f1eefb7a4e60a2e05264"), "comentarii.utilizator": "alex_87"},{"$set": {"comentarii.$.comentariu": "Comentariu actualizat"}})#De facut dupa atribute
clienti_collection.update_one({"_id": ObjectId("6247f1eefb7a4e60a2e05261")}, {"$set": {"adresa.judet": "Bacău"}})#De facut dupa atribute
comenzi_collection.update_one({"_id": ObjectId("6348f1eefb7a4e60a2e05265")},{"$set": {"adresa_livrare.oras": "Bacău"}})#De facut dupa atribute

