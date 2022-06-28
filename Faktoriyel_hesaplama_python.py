
# FAKTORIYEL HESAPLAMA

sayi=int(input("Faktoriyel almak istediginiz sayiyi giriniz. \n"))
deger=1
if(sayi<=0):
   print("Sayi pozitif ve 0'dan buyuk olmalidir.")
else:
    for i in range(sayi):
        deger*=(i+1)

print("Girilen sayinin faktoriyeli {} dir".format(deger))
