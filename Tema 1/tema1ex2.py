
# a) Distributie geometrica

import random

def simuleaza_joc(p):
    N = 0
    S = 0

    while True:
        N = N + 1
        moneda = random.random()

        if moneda < p:
            z = random.randint(1, 6)
            S = S + (z - 3)
            break
        else:
            S = S - 0.5

    return N, S

rezultat = simuleaza_joc(0.5)
print("Numar de pasi:", rezultat[0])
print("Suma totala S:", rezultat[1])