import random
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

X = []
for i in range(10000):
    r = random.random()

    if r < 3/13:
        timp = np.random.exponential(1/3)
    elif r < 9/13:
        timp = np.random.exponential(1/6)
    else:
        timp = np.random.exponential(1/4)

    X.append(timp)

X = np.array(X)

print("Media:", np.mean(X))
print("Deviatia standard:", np.std(X))

sns.kdeplot(X, fill=True)
plt.title("Densitatea distributiei lui X")
plt.xlabel("Timp de servire (ore)")
plt.ylabel("Densitate")
plt.show()