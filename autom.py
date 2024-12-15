from datetime import datetime
from auto import Auto


def feladat3():
    auto_lista:list[Auto]=[]
    with open("auto.txt", "r",encoding='utf-8') as file:
        next(file)  
        for line in file:
            adatok:list[str]=line.split("$")
            auto:Auto=Auto(adatok[0],int(adatok[1]))
            auto_lista.append(auto)
    return auto_lista

def flotta(auto_lista:list[Auto]):
    db:int=len(auto_lista)
    print(f"Autók száma: {db}")
    return db

def legfiatalabb(auto_lista:list[Auto]):
    legfiatalabb:Auto=auto_lista[0]
    for x in auto_lista:
        if legfiatalabb.gyartasi_datum < x.gyartasi_datum:
            legfiatalabb=x

    print(f"A legfiatalabb autó: {legfiatalabb}")

def atlag_kor(auto_lista:list[Auto]):
    aktualis_ev = datetime.now().year
    db:int=len(auto_lista)
    atlag:float=0
    osszeg:float=0

    for x in auto_lista:
        osszeg+=aktualis_ev-x.gyartasi_datum
    
    atlag=osszeg/db
    print(f"Az autók átlagos kora: {atlag:.2f} év.")


    

