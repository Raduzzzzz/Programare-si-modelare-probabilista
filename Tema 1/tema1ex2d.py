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

for p in [0.3, 0.5, 0.7]:
    sume = []
    for i in range(10000):
        rezultat = simuleaza_joc(p)
        sume.append(rezultat[1])

    medie = sum(sume) / len(sume)
    print("p =", p, "| Media S =", medie)

    plt.hist(sume, bins=30, edgecolor='black', alpha=0.6, label=str(p))

plt.legend()
plt.show()