import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 9, 1000)
y_maaling = [0, 4.78, 6.83, 7.64, 8.12, 8.71, 8.82, 8.84, 8.98, 8.99]
tid = np.linspace(0, 9, len(y_maaling))  

def v(t):
    R = 15000
    C = 100 * 10**-6
    y_teori = 9 - 9 * np.exp(-t / (R * C))
    plt.plot(t, y_teori, label="Teoretisk kurve")
    plt.plot(tid, y_maaling, 'o', label="Praktisk maaling") 
    plt.legend()
    plt.xlabel("Tid (s)")
    plt.ylabel("Spenning (V)")
    plt.title("Spenning over kondensator i RC-krets")
    plt.grid(True)
    plt.show()

v(t)
