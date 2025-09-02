#!/usr/bin/python3

# # Boucle sur le premier chiffre (de 0 à 9)
for i in range(10):
    # Boucle sur le deuxième chiffre (toujours plus grand que le premier)
    for j in range(i + 1, 10):
        # Si ce n'est pas la dernière combinaison, on ajoute ", "
        if i != 8 or j != 9:
            print(f"{i}{j}", end=", ")
# Dernière combinaison sans virgule
print("89")
