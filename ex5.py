def calcul_factoriel(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * calcul_factoriel(n - 1)