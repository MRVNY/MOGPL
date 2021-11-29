
# Question 1
Dans un multigraphe orient ́e sans circuit avec des contraintes de temps :
## Assertion 1 : Un sous-chemin pr ́efixe d’un chemin d’arriv ́ee au plus tˆot peut ne pas ˆetre un chemin d’arriv ́ee au plus tˆot.

## Assertion 2 : Un sous-chemin postfixe d’un chemin de d ́epart au plus tard peut ne pas ˆetre un chemin de d ́epart au plus tard.
## Assertion 3 : Un sous-chemin d’un chemin le plus rapide peut ne pas ˆetre un chemin le plus rapide.
## Assertion 4 : Un sous-chemin d’un plus court chemin peut ne pas ˆetre un plus court chemin.

# Q2
## Type I : Chemin d’arrivée au plus tôt
P(x,y,[ta,tw])
```
on cherche le sommet de y, avec la plus petit chiffre
```
## Type II : Chemin de départ au plus tard
```
on cherche le sommet de x, avec la plus grand chiffre
```
## Type III : Chemin le plus rapide
```
On cherche tous les sommets de x et on les met dans X
On cherche tous les sommets de y et on les met dans Y

pour chaque sommet dans X:
    On suit les chemins jusqu'a où atteint un sommet de Y, on les met dans une liste C, sinon on abandonne, 
On compare dans C la plus petite difference entre le chiffre de la fin et le chiffre du depart 
```

## Type IV : Plus court chemin
```
On cherche tous les sommets de x et on les met dans X
On cherche tous les sommets de y et on les met dans Y

pour chaque sommet dans X:
    On suit les chemin jusqu'a où atteint un sommet de Y, on les met dans une liste C, sinon on abandonne
On compare dans C la plus petite somme des valeurs des arcs des chemins
```