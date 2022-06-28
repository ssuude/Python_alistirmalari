
# DIZIDEKI AYNI ELEMANLARI AYIRIYOR

liste=["bir","iki","iki","dort","bes","bes","yedi"]

liste2=[]
listeTekrar=[]
for deger in liste:
    if deger not in liste2:
        liste2.append(deger)
    else:
        listeTekrar.append(deger)
print(liste2)
print(set(listeTekrar))
print("**********")
del liste[2]
print(liste)