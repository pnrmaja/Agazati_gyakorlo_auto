class Auto:
    def __init__(self, nev:str, gyartasi_datum:int):
        self.nev = nev
        self.gyartasi_datum = gyartasi_datum

    def __str__(self):
        return f"{self.nev} ({self.gyartasi_datum})"