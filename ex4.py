liste_nombres = [23, 45, 12, 67, 89, 34, 56, 78, 90, 21]

maximum = liste_nombres[0]
for nombre in liste_nombres:
    if nombre > maximum:
        maximum = nombre
print("Le maximum est :", maximum)
minimum = liste_nombres[0]
for nombre in liste_nombres:
    if nombre < minimum:
        minimum = nombre
print("Le minimum est :", minimum)
somme = 0
for nombre in liste_nombres:
    somme += nombre
moyenne = somme / len(liste_nombres)
print("La moyenne est :", moyenne)