from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient('mongodb+srv://rares:rares@cluster0.o62zky8.mongodb.net/')
db = client['electronic_db']
produse_collection = db['produse']
clienti_collection = db['clienti']
comenzi_collection = db['comenzi']

print("Produse care au 16 GB de RAM, fara imagini:")
cursor_produse = produse_collection.find({"specificatii.RAM": "16 GB"},{"imagini":0})
for produs in cursor_produse:
    print(produs)
print()
print("Produse care au stocul mai mic decat 10, sortate crescator dupa pret, fara imagini:")
cursor_stoc_redus = produse_collection.find({"stoc": {"$lt": 10}},{"imagini":0}).sort("pret")
for produs in cursor_stoc_redus:
    print(produs)
print()
print("Calculare stoc total al produselor cu procesorul produs de AMD:")
pipeline = [
    {"$match": {"specificatii.procesor.producator": "AMD"}},
    {"$group": {"_id": "$specificatii.procesor.producator", "total": {"$sum": "$stoc"}}}
]
result = produse_collection.aggregate(pipeline)
for doc in result:
    print(doc)
print()
print("Calculare pret total al produselor cu procesor octacore per producator:")
pipeline = [
    {"$match": {"specificatii.procesor.nuclee": 8}},
    {"$group": {"_id": "$specificatii.procesor.producator", "total": {"$sum": {"$multiply":["$pret","$stoc"]}}}}
]
result = produse_collection.aggregate(pipeline)
for doc in result:
    print(doc)
print()
print("Adaugare camp disponibilitate in functie de stoc, afisare nume si disponibilitate pentru primele 5 produse:")
pipeline_addFields = [
    {"$addFields": {"disponibilitate": {"$cond": {"if": {"$gt": ["$stoc", 0]}, "then": "Disponibil", "else": "Indisponibil"}}}},
    {"$limit": 5},
    {"$project":{"_id":0,"nume":1,"disponibilitate":1}}
]
result_addFields = produse_collection.aggregate(pipeline_addFields)
for doc in result_addFields:
    print(doc)

print()
print("Afisare nume si prenume client pentru fiecare comanda, folosind $lookup, sortate dupa numele clientului:")   
pipeline_lookup_comenzi = [
    {"$lookup": {"from": "clienti", "localField": "email_client", "foreignField": "email", "as": "client_info"}},
    {"$unwind": "$client_info"},
    {"$project": {"_id": 0, "nume_client": "$client_info.nume", "prenume_client": "$client_info.prenume", "produse": 1, "data_comanda": 1}},
    {"$sort": {"nume_client": 1}}
]
result_lookup_comenzi = comenzi_collection.aggregate(pipeline_lookup_comenzi)
for doc in result_lookup_comenzi:
    print(doc)

print()
print("Afisare detaliile produselor pentru fiecare comanda, folosind $lookup si $push, fără imagini:")   
pipeline_lookup_produse = [
    {"$unwind": "$produse"}, 
    {"$lookup": {"from": "produse", "localField": "produse.nume_produs", "foreignField": "nume", "as": "detalii_produs"}},
    {"$unwind": "$detalii_produs"}, 
    {"$project": {"detalii_produs.imagini": 0}}, 
    {"$group": {"_id": "$_id", "email_client": {"$first": "$email_client"}, "detalii_produse": {"$push": "$detalii_produs"}}}  
]

result_lookup_produse = comenzi_collection.aggregate(pipeline_lookup_produse)
for doc in result_lookup_produse:
    print(doc)

