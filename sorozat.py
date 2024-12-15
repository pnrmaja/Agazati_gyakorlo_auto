import random

def feladat2():
    print("II/A, B, C:")
    lotto_szamok:list[int] =[]
    lista_szamok_str:list[str] =[]
    x:int=0
    
    for x in  range(5):
        lotto_szam:int=random.randint(1,90)
        lotto_szamok.append(lotto_szam)
        lista_szamok_str.append(str(lotto_szam))
    print("; ".join(lista_szamok_str))
    return lotto_szamok

def egyjegyuek_szama(lotto_szamok:list[int]):

    print("II/D, E:")

    db:int=0
    for x in lotto_szamok:
        if 1 <= x <=9:
            db+=1
    return db

def konzol_kiir(egyjegyuek_szama:int):

    print(f"Az egyjegyűek száma: {egyjegyuek_szama}. ")

def file_kiir(egyjegyuek_szama:int):
    print(f"II/F:")
    with open("szamok.txt", "w",encoding='utf-8') as file:
        file.write(f"Az egyjegyűek száma: {egyjegyuek_szama}. ")

