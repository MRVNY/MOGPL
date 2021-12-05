
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

Pour modéliser notre problème de plus court chemin en programme linéaire, nous avons tout d'abord convertis un graphe en programme linéaire. Ses sommets sont devenus les variables de décisions et ses arcs les contraintes de notre programme linéaire. Pour exemple, le sommet 1 et le sommet 2 sont devenus les variables x1 et x2 et l'arc qui réalisais la liaison entre les deux ce traduit par la contrainte x2 - x1 <= 1. On réaliste cette opération pour tout notre graphe. Il ne nous reste plus qu'a exprimer le problème du plus court chemin entre deux point avec la fonction objectif. Ici, il ne s'agissais pas de minimiser la distance entre Xstart et Xend mais justement de la maximiser. En effet, en maximisant la distance, cela permet de mettre en tension l'ensemble du programme linéaire pour que le problème ne sois pas non borné.

Dans notre projet, c'est la fonction conversion_PL(graphe,start,end) qui convertis les paramètres d'entrée en un programme linéaire et le solveur guroby ce charge ensuite de calculer la valeur de distance la plus courte et nous permet de retracer le chemin le plus court avec les variables mise en tension ( leur valeur est différente de 0 ).

