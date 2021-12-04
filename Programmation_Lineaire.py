from gurobipy import *
from Algo import simple_graph
import numpy as np

def conversion_PL(graphe,start,end):
    """Permet de trouver le chemin le plus court en convertissant le graphe d'entrée en un programme linéaire"""
    nb_som, nb_arc, _, arc = simple_graph(graphe)

    sommets = graphe[2]
    sEnds = []
    sStarts = []

    for s in sommets:
        if s[0] == end:
            sEnds.append(s)
        if s[0] == start and sStarts==[]:
            sStarts.append(s)
    
    sStart = sStarts[0]

    
    nbcont = nb_arc
    nbvar = nb_som

    # Range of plants and warehouses
    lignes = range(nbcont)
    colonnes = range(nbvar)

    # Matrice des contraintes
    a = []
    for i in range(nbcont):
        c = [0] * nbvar
        c[arc[i][0]] = -1
        c[arc[i][1]] = 1
        a.append(c)

    # Second membre LES VALEURS DES ARC
    b = [i[2] for i in arc]

    # Coefficients de la fonction objectif
    c = [0] * nbvar
    c[sommets.index(sStart)] = -1
    c[sommets.index(sEnds[0])] = 1


    m = Model("mogplex")     
            
    # declaration variables de decision
    x = []
    for i in colonnes:
        x.append(m.addVar(vtype=GRB.INTEGER, lb=0, name="x%d" % (i+1)))

    # maj du modele pour integrer les nouvelles variables
    m.update()

    obj = LinExpr();
    obj =0
    for j in colonnes:
        obj += c[j] * x[j]
            
    # definition de l'objectif
    m.setObjective(obj,GRB.MAXIMIZE)

    # Definition des contraintes
    for i in lignes:
        m.addConstr(quicksum(a[i][j]*x[j] for j in colonnes) <= b[i], "Contrainte%d" % i)

    # Resolution
    m.optimize()

    chemin = [j for j in colonnes if x[j].x!=0]
    chemin.insert(0,sommets.index(sStart))
    for i in range(len(chemin)):
        chemin[i] = sommets[chemin[i]][0]


    if m.objVal == float("Inf"):
        print("\nil n'y a pas de moyen d'atteindre " + end + " depuis " + start+ "\n")
    else:
        print("\nLe chemin le plus rapide de TypeIV convertie de programme linéaire de "+ start +" à " +end + " est", end =" ")
        print(np.unique(np.array(chemin)).tolist(), end =" ")
        print("avec une distance de "+ str(int(m.objVal)) + "\n")
    