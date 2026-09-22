from fractran import Facteur, Fraction, Fractran

print("--- Somme ---")
somme = [Fraction(3, 2)]
facteurs_somme = Facteur([2, 3, 5])

for i in range(1, 11):
    for j in range(1, 11):
        n = facteurs_somme.nombre([i, j, 0])
        s = Fractran(somme).run(n)
        decomp = facteurs_somme.décomposition(s)
        print(i, "+", j, "=", decomp[1])


print("\n--- Multiplication ---")
produit = [Fraction(385, 13),Fraction(13, 21),Fraction(1, 7),Fraction(3, 11),Fraction(7, 2),Fraction(1, 3),]
facteurs_produit = Facteur([2, 3, 5])

for i in range(1, 11):
    for j in range(1, 11):
        n = facteurs_produit.nombre([i, j, 0])
        p = Fractran(produit).run(n)
        decomp = facteurs_produit.décomposition(p)
        print(i, "*", j, "=", decomp[2])


print("\n--- Fibonacci ---")
fibonacci = [Fraction(23, 95),Fraction(57, 23),Fraction(17, 39),Fraction(130, 17),Fraction(11, 14),Fraction(35, 11),Fraction(19, 13),Fraction(1, 19),Fraction(35, 2),Fraction(13, 7),Fraction(7, 1),]

sortie_brute = Fractran(fibonacci).suite(3, 1000)
sortie = []
f23 = Facteur([2, 3])

for n in sortie_brute:
    d = f23.décomposition(n)
    if f23.nombre(d) == n:
        sortie.append(d)

print(sortie)


print("\n--- Nombres Premiers ---")
nb_premiers = [Fraction(17, 91),Fraction(78, 85),Fraction(19, 51),Fraction(23, 38),Fraction(29, 33),Fraction(77, 29),Fraction(95, 23),Fraction(77, 19),Fraction(1, 17),Fraction(11, 13),Fraction(13, 11),Fraction(15, 2),Fraction(1, 7),Fraction(55, 1),]

états = Fractran(nb_premiers).suite(2, 100000)
premiers = []

for n in états:
    d = f23.décomposition(n)
    if d[0] > 1 and f23.nombre([d[0], 0]) == n:
        if d[0] not in premiers:
            premiers.append(d[0])

print(premiers)