import random
import time

pi_real = 3.14159

def monte_carlo(N):
    dentro = 0

    inicio = time.time()

    for i in range(N):
        x = random.uniform(-0.5, 0.5)
        y = random.uniform(-0.5, 0.5)

        if x*x + y*y < 0.25:
            dentro = dentro + 1

    pi = 4 * dentro / N
    error = abs(pi_real - pi)

    fin = time.time()

    return pi, error, fin - inicio


def las_vegas(K):
    dentro = 0
    total = 0

    inicio = time.time()

    while dentro < K:
        x = random.uniform(-0.5, 0.5)
        y = random.uniform(-0.5, 0.5)

        total = total + 1

        if x*x + y*y < 0.25:
            dentro = dentro + 1

    pi = 4 * K / total
    error = abs(pi_real - pi)

    fin = time.time()

    return pi, error, fin - inicio


print("ALGORITMO MONTE CARLO")

for N in [1000, 10000, 100000]:
    pi, error, tiempo = monte_carlo(N)

    print("\nN:", N)
    print("Pi estimado:", pi)
    print("Error:", error)
    print("Tiempo:", tiempo)


print("\nALGORITMO LAS VEGAS")

for K in [100, 1000, 5000]:
    pi, error, tiempo = las_vegas(K)

    print("\nK:", K)
    print("Pi estimado:", pi)
    print("Error:", error)
    print("Tiempo:", tiempo)
