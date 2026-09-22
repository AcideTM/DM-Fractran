# Projet Interpréteur FRACTRAN

Ce projet implémente un interpréteur pour le langage FRACTRAN inventé par John Conway.

## Explication du code de la suite de Fibonacci

Le programme FRACTRAN pour la suite de Fibonacci génère une suite de nombres entiers. Durant l'exécution, beaucoup de ces nombres contiennent d'autres facteurs premiers (comme 5, 7, 11, etc.) qui servent de variables temporaires pour effectuer les calculs.

Dans le script principal `main.py`, le fonctionnement pour récupérer la suite est le suivant :

1. `Fractran(fibonacci).suite(3, 1000)` récupère la liste des 1000 premiers entiers générés par l'algorithme.
2. Pour filtrer les résultats et ne garder que les valeurs finales, on utilise l'objet `Facteur([2, 3])`.
3. On calcule la décomposition de `n` en facteurs de 2 et 3 avec `f23.décomposition(n)`.
4. La condition `f23.nombre(d) == n` vérifie si l'entier `n` est composé uniquement de puissances de 2 et 3. Si `n` contient d'autres facteurs premiers, l'égalité est fausse.
5. Quand la condition est vraie, les exposants retenus dans la liste `d` correspondent directement aux couples de termes consécutifs de Fibonacci $(F_n, F_{n+1})$.