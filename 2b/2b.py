from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime
client = MongoClient('mongodb+srv://rares:rares@cluster0.o62zky8.mongodb.net/')

db = client['electronic_db']

produse_collection = db['produse']
clienti_collection = db['clienti']
comenzi_collection = db['comenzi']
produse_collection.drop()
clienti_collection.drop()
comenzi_collection.drop()
produse = [
    {
  "_id": ObjectId("6147f1eefb7a4e60a2e0525d"),
  "nume": "Laptop Dell",
  "descriere": "Laptop performant cu procesor puternic și display de înaltă rezoluție.",
  "pret": 3000.0,
  "stoc": 50,
  "disponibil": True,
  "data_adaugare": datetime.utcnow(),
  "specificatii": {
    "culoare": "Negru",
    "dimensiuni": {
      "lungime": 35.5,
      "latime": 24.5,
      "inaltime": 2.0
    },
    "greutate": 2.0,
    "marca": "Dell",
    "altele": ["Touchscreen", "Wi-Fi 6", "Bluetooth 5.0"]
  },
  "imagini": [
    "<binary data 1>",
    "<binary data 2>",
    "<binary data 3>"
  ],
  "comentarii": [
    {
      "utilizator": "john_doe",
      "comentariu": "Foarte mulțumit de performanțele acestui laptop!"
    },
    {
      "utilizator": "jane_smith",
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
  "nume": "Laptop Dell",
  "descriere": "Laptop performant cu procesor puternic și display de înaltă rezoluție.",
  "pret": 3000.0,
  "stoc": 50,
  "disponibil": True,
  "data_adaugare": datetime.utcnow(),
  "specificatii": {
    "culoare": "Negru",
    "dimensiuni": {
      "lungime": 35.5,
      "latime": 24.5,
      "inaltime": 2.0
    },
    "greutate": 2.0,
    "marca": "Dell",
    "altele": ["Touchscreen", "Wi-Fi 6", "Bluetooth 5.0"]
  },
  "imagini": [
    "<binary data 1>",
    "<binary data 2>",
    "<binary data 3>"
  ],
  "comentarii": [
    {
      "utilizator": "john_doe",
      "comentariu": "Foarte mulțumit de performanțele acestui laptop!"
    },
    {
      "utilizator": "jane_smith",
      "comentariu": "Designul este elegant și tastatura este foarte confortabilă."
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
  "nume": "Laptop Dell",
  "descriere": "Laptop performant cu procesor puternic și display de înaltă rezoluție.",
  "pret": 3000.0,
  "stoc": 50,
  "disponibil": True,
  "data_adaugare": datetime.utcnow(),
  "specificatii": {
    "culoare": "Negru",
    "dimensiuni": {
      "lungime": 35.5,
      "latime": 24.5,
      "inaltime": 2.0
    },
    "greutate": 2.0,
    "marca": "Dell",
    "altele": ["Touchscreen", "Wi-Fi 6", "Bluetooth 5.0"]
  },
  "imagini": [
    "<binary data 1>",
    "<binary data 2>",
    "<binary data 3>"
  ],
  "comentarii": [
    {
      "utilizator": "john_doe",
      "comentariu": "Foarte mulțumit de performanțele acestui laptop!"
    },
    {
      "utilizator": "jane_smith",
      "comentariu": "Designul este elegant și tastatura este foarte confortabilă."
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
  "nume": "Laptop Dell",
  "descriere": "Laptop performant cu procesor puternic și display de înaltă rezoluție.",
  "pret": 3000.0,
  "stoc": 50,
  "disponibil": True,
  "data_adaugare": datetime.utcnow(),
  "specificatii": {
    "culoare": "Negru",
    "dimensiuni": {
      "lungime": 35.5,
      "latime": 24.5,
      "inaltime": 2.0
    },
    "greutate": 2.0,
    "marca": "Dell",
    "altele": ["Touchscreen", "Wi-Fi 6", "Bluetooth 5.0"]
  },
  "imagini": [
    "<binary data 1>",
    "<binary data 2>",
    "<binary data 3>"
  ],
  "comentarii": [
    {
      "utilizator": "john_doe",
      "comentariu": "Foarte mulțumit de performanțele acestui laptop!"
    },
    {
      "utilizator": "jane_smith",
      "comentariu": "Designul este elegant și tastatura este foarte confortabilă."
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
  "_id": ObjectId("6147f1eefb7a4e60a2e05268"),
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

produse_collection.delete_one({ '_id': ObjectId('6147f1eefb7a4e60a2e05268')})
clienti_collection.delete_one({ 'nume': 'John', 'prenume': 'Doe' })
comenzi_collection.delete_one({ "_id": ObjectId("6348f1eefb7a4e60a2e05266"), "status": "În așteptare" })

produse_collection.update_one({"_id": ObjectId("6147f1eefb7a4e60a2e05264"), "comentarii.utilizator": "alex_87"},{"$set": {"comentarii.$.comentariu": "Comentariu actualizat"}})
clienti_collection.update_one({"_id": ObjectId("6247f1eefb7a4e60a2e05261")}, {"$set": {"adresa.judet": "Bacău"}})
comenzi_collection.update_one({"_id": ObjectId("6348f1eefb7a4e60a2e05265")},{"$set": {"adresa_livrare.oras": "Bacău"}})

