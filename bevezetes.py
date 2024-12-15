def feladat1():
    print("I/A")

    neve:str = input("Autó neve:")
    gyartasi_eve:int = int(input("Gyártási dátum:"))

    print("I/B")

    if gyartasi_eve == 2024:
        print(f"friss gyártás")
    elif gyartasi_eve < 2000:
        print(f"öreg autó")
    else:
        print(f"átlagos korú")