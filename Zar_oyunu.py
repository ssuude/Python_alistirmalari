

import random
import time

#(zar_1,zar_2) seklinde 2 zar atiyoruz
i = 1
while True:
    zar_1 = random.randint(1, 6)
    zar_2 = random.randint(1, 6)
    # iki zara da rastegele degerler atiyorum

    if zar_1 == 6 and zar_2 == 6:
        print("""Deneme {}:\t({},{}) *** """.format(i, zar_1, zar_2))
        time.sleep(2)
        break

    print("""Deneme {}:\t({},{}) """.format(i, zar_1, zar_2))
    i += 1
    time.sleep(0.5)

print("""\n*** {}. denemede (6,6) geldi ***""".format(i))