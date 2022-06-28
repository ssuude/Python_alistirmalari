
# GÝRÝLEN SAYIYA KADAR OLAN ASAL SAYILARI BULMA 

girilenSayi=int(input("Sinir sayisi giriniz. : "))
asal=[]

# 2 en küçük asal sayý

for i in range(2,girilenSayi):
    for j in range(2,i):
        if i%j==0:
            break

    else:
        asal.append(i)

print("{} e kadar {} tane asal sayi vardir.".format(girilenSayi,len(asal)))