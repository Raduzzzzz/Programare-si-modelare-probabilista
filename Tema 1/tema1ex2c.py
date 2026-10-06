import random
import matplotlib.pyplot as plt

def simuleaza_joc(p):
    N = 0
    S = 0
    while True:
        N = N + 1
        if random.random() < p:
            z = random.randint(1, 6)
            S = S + (z - 3)
            break
        else:
            S = S - 0.5
    return N, S

sume = []
for i in range(10000):
    rezultat = simuleaza_joc(0.5)
    sume.append(rezultat[1])

medie = sum(sume) / len(sume)
print("Media lui S:", medie)

plt.hist(sume, bins=30, edgecolor='black')
plt.title("Distributia sumei S")
plt.xlabel("S")
plt.ylabel("Frecventa")
plt.show()