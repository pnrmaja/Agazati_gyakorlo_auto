from auto import Auto
import autom
import bevezetes
import sorozat

#bevezetes.feladat1()
#sorozat.feladat2()
"""


lotto_szamok:list[int]=sorozat.feladat2()
egyjegyuek_szama:int=sorozat.egyjegyuek_szama(lotto_szamok)
sorozat.konzol_kiir(egyjegyuek_szama)
sorozat.file_kiir(egyjegyuek_szama)
"""

autok:list[Auto]=autom.feladat3()
autom.flotta(autok)
autom.legfiatalabb(autok)
autom.atlag_kor(autok)

