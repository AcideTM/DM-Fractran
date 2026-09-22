class Fraction:

    def __init__(self, numérateur, dénominateur):
        self.numérateur = numérateur
        self.dénominateur = dénominateur

    def est_entier(self, n):
        return n % self.dénominateur == 0

    def valeur(self, n):
        return self.numérateur * (n // self.dénominateur)


class Facteur:

    def __init__(self, facteurs):
        self.facteurs = facteurs

    def nombre(self, L):
        c = 1
        for i in range(len(L)):
            c = c * (self.facteurs[i] ** L[i])
        return c

    def décomposition(self, n):
        L = []
        for p in self.facteurs:
            c = 0
            while n % p == 0:
                c += 1
                n = n // p
            L.append(c)
        return L


class Fractran:

    def __init__(self, fractions):
        self.programme = fractions

    def run(self, n):
        i = 0
        while i < len(self.programme):
            if self.programme[i].est_entier(n):
                n = self.programme[i].valeur(n)
                i = 0
            else:
                i += 1
        return n

    def suite(self, n, N):
        L = [n]
        i = 0
        while len(L) < N and i < len(self.programme):
            if self.programme[i].est_entier(n):
                n = self.programme[i].valeur(n)
                L.append(n)
                i = 0
            else:
                i += 1
        return L