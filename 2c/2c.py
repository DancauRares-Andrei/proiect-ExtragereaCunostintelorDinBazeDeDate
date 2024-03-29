from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime

client = MongoClient('mongodb+srv://rares:rares@cluster0.o62zky8.mongodb.net/')
db = client['electronic_db']
produse_collection = db['produse']
clienti_collection = db['clienti']
comenzi_collection = db['comenzi']

print("Produse cu pretul mai mic de 2000 care au stocul mai mare ca 10 pentru care se afiseaza numele si pretul, sortate descrescatoare dupa pret")
produse_gasite = produse_collection.find(
    {"pret": {"$lt": 2000}, "stoc": {"$gt": 10}},
    {"nume": 1, "pret": 1, "_id": 0}
).sort({"pret":-1})

for produs in produse_gasite:
    print(produs)

# Cautare clienti cu numele inceput cu litera "J"
clienti_gasiti = clienti_collection.find(
    {"nume": {"$regex": "^J"}}
)

for client in clienti_gasiti:
    print(client)

comenzi_gasite = comenzi_collection.find(
    {"adresa_livrare.judet": "Cluj"},
    {"adresa_livrare": 1, "data_comanda": 1, "_id": 0}
)

for comanda in comenzi_gasite:
    print(comanda)

comenzi_paginate = comenzi_collection.find().skip(2).limit(2)

for comanda in comenzi_paginate:
    print(comanda)

