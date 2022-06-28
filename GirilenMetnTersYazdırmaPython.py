
girilen_yazi = input("Cumle giriniz :")
yazinin_tersi = ""


def tersini_alma(yazi, tersi):
    for i in range(len(yazi) - 1, -1, -1):
        tersi += yazi[i]
    return tersi


kelimeler = []
for i in girilen_yazi.split(' '):
    kelimeler.append(tersini_alma(i, ""))

cumle_olarak_tersi = tersini_alma(girilen_yazi, yazinin_tersi)
kelime_olarak_tersi = " ".join(kelimeler)

print(
    """
    Cumlenin orjinali:                  {}
    
    Tamamen tersi alinmis hali:         {}
    
    Kelime kelime tersi alinmis hali:   {}
    
    """.format(girilen_yazi, cumle_olarak_tersi, kelime_olarak_tersi))