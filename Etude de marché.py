nbProduits = int(input())
nbPersonnes = int(input())
LISTE = []
produit=-1
for loop in range(nbPersonnes):
    numero_produit = int(input())
    LISTE.append(numero_produit)
for loop in range(nbProduits):
    produit +=1
    print(LISTE.count(produit))