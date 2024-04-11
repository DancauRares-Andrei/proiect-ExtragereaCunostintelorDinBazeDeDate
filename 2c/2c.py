from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime

client = MongoClient('mongodb+srv://rares:rares@cluster0.o62zky8.mongodb.net/')
db = client['electronic_db']
produse_collection = db['produse']
clienti_collection = db['clienti']
comenzi_collection = db['comenzi']

produse_gasite = produse_collection.find(
    {"pret": {"$lt": 2000}, "stoc": {"$gt": 10}},
    {"nume": 1, "pret": 1, "_id": 0}
).sort({"pret":-1})

print("Produse cu pretul mai mic de 2000 care au stocul mai mare ca 10 pentru care se afiseaza numele si pretul, sortate descrescator dupa pret:")
for produs in produse_gasite:
    print(produs)

clienti_gasiti = clienti_collection.find(
    {"prenume": {"$regex": "^M"}}
)
print()
print("Clienti al caror prenume incepe cu M:")
for client in clienti_gasiti:
    print(client)

comenzi_gasite = comenzi_collection.find(
    {"adresa_livrare.judet": "Cluj"},
    {"adresa_livrare": 1, "data_comanda": 1, "_id": 0}
)
print()
print("Cautare comenzi din judetul Cluj, afisand doar adresa de livrare si data comenzii")

for comanda in comenzi_gasite:
    print(comanda)
print()
comenzi_paginate = comenzi_collection.find().skip(2).limit(2).sort({"adresa_livrare.strada":-1})
print("Afisare comenzi paginata, cu cate 2 comenzi pe pagina, pagina a doua, sortate descrescator dupa numele strazii adresei de livrare")
for comanda in comenzi_paginate:
    print(comanda)
print()
produse_paginate = produse_collection.find({"pret": {"$gt": 1000}},{"_id":0,"nume":1,"stoc":1}).skip(3).limit(3)
print("Afisare paginata produse cu pretul mai mare de 1000 cu proiectie, cu cate 3 produse pe pagina, pagina a doua")
for produs in produse_paginate:
    print(produs)
print()
clienti_gasiti = clienti_collection.find(
    {"inexistent": "a"} 
)
print("Clienti care au valoarea a pe un atribut inexistent(nu ar trebui sa existe):")
for client in clienti_gasiti:
    print(client)
print() 
comenzi_gasite = comenzi_collection.find({"data_comanda":{"$type": 10}})
print("Comenzi care au valoarea null pe data_comanda(nu ar trebui sa existe):")
for comanda in comenzi_gasite:
    print(comanda)
