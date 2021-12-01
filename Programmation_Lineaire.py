from gurobipy import *
from Algo import simple_graph

def conversion_PL(graphe):
    nb_som, nb_arc, sommet, arc = simple_graph(graphe)
    
    nbcont = nb_arc
    nbvar = nb_som

    # Range of plants and warehouses
    lignes = range(nbcont)
    colonnes = range(nbvar)

    # Matrice des contraintes
    a = [[1,0],
        [0,1],
        [1,2],
        [2,1]]

    # Second membre LES VALEURS DES ARC
    b = [i[2] for i in arc]

    # Coefficients de la fonction objectif
    c = [1] * nb_som

    m = Model("mogplex")     
            
    # declaration variables de decision
    x = []
    for i in colonnes:
        x.append(m.addVar(vtype=GRB.CONTINUOUS, lb=0, name="x%d" % (i+1)))

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


    print("")                
    print('Solution optimale:')
    for j in colonnes:
        print('x%d'%(j+1), '=', x[j].x)
    print("")
    print('Valeur de la fonction objectif :', m.objVal)