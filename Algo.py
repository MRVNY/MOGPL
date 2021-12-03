def alph(s):
    return s[0]

"""def chemin_plus_rapide(graphe,debut,arrive):
    nb_sommet,nb_arc,sommet,arc = graphe

    #recherche du premier sommet
    sommet.sort(key=alph)
    tmp = 0
    for i in sommet:
        if i[0] == debut:
            tmp = sommet.index(i)
            break
    sommets_courant = sommet[tmp]

    #tant que l'on arrive pas à la fin on passe a l'arc suivant      
    return CPR(arc,sommet,sommets_courant,arrive)

def CPR(arc,sommet,current,arr):
    if current[0] == arr:
        return current
    else:
        #on cherche les prochain sommets disponibles grace aux arcs
        next_sommet = []
        for a in arc:
            if a[0] == current:
                next_sommet.append(a[1])
        if(len(next_sommet)==0):#si il n'y a plus de sommet dispo retourne false pour signifier la fermeture du chemin
            return False
        
        R = []
        for s in next_sommet:
            r = CPR(arc,sommet,s,arr)
            R.append(r)
        R = list(filter((False).__ne__, R))

        if(len(R)==0):
            return False
        
        return R"""

def Ford_Bellman(G,source):
    """
    Algorithme de Ford Bellman
    Attention source est l'indice dans arc de notre point de start
    """
    nb_sommets, nb_arc, sommet, arc = G
    distance = [float("Inf")] * nb_sommets
    distance[source] = 0
    chemin = [None] * nb_sommets
    chemin[source] = None

    for _ in range(nb_sommets - 1):
        for a, b, c in arc:
            if distance[a] != float("Inf") and distance[a] + c < distance[b]:
                distance[b] = distance[a] + c
                chemin[b] = a

    for a, b, c in arc:
        if distance[a] != float("Inf") and distance[a] + c < distance[b]:
            print("Le graphe contient un circuit absorbant")
            return
    
    return distance, chemin

def if_Existe_Chemin(graphe,start,end):
    
    return True
    
    
def simple_graph(G):
    """Permet de simplifier les graphiques ( convertir les sommets en entier) """
    nb_sommets, nb_arc, sommet, arc = G

    sommet_simple = [0] * nb_sommets
    arc_simple = [0] * nb_arc

    for i in range(nb_sommets):
        sommet_simple[i] = i
    
    for i in range(nb_arc):
        arc_simple[i] = (sommet.index(arc[i][0]),sommet.index(arc[i][1]),arc[i][2])
    return [nb_sommets,nb_arc,sommet_simple,arc_simple]

# Type I : Chemin d’ende au plus tôt
def type1(graphe,start,end):
    """on cherche le sommet de y, avec la plus petit chiffre"""
    return 0

# Type II : Chemin de start au plus tard
def type2(graphe,start,end):
    """on cherche le sommet de x, avec la plus grand chiffre"""

# Type III : Chemin le plus rapide
def type3(graphe,start,end):
    """
    On cherche tous les sommets de x et on les met dans X
    On cherche tous les sommets de y et on les met dans Y

    pour chaque sommet dans X:
        On suit les chemins jusqu'a où atteint un sommet de Y, on les met dans une liste C, sinon on abandonne, 
    On compare dans C la plus petite difference entre le chiffre de la fin et le chiffre du depart
    """

# Type IV : Plus court chemin
def type4(graphe,start,end):
    """Permet de calculer le chemin le plus rapide de Type IV"""
    sommets, arcs = graphe[2], graphe[3]

    #recherche de l'emplacement des éléments de début et fin
    tmp_dep = 0
    done = False
    tmp_arr = []
    for i in sommets:
        if i[0] == start and not done:
            tmp_dep = sommets.index(i)
            done = True

        if i[0] == end:
            tmp_arr.append(sommets.index(i))

    id_dep, id_arr = tmp_dep, tmp_arr #emplacement des éléments de début et fin
    sim_g = simple_graph(graphe) #le graphe dois etre déja conv ! il est ensuite convertie en une version plus simple
    dist, che = Ford_Bellman(sim_g,id_dep)# On peu maintenant effectuer Ford-Bellman sur le graphe simplifié

    # on a maintenant besoin du point final parmis toute ses posibilitées( celle dans laquelle on est end/le jour d'end )
    m = float("Inf")
    tmp = 0
    for i in id_arr:
        if m > dist[i]:
            m = dist[i]
            tmp = i

    # on retrace ensuite le chemin que l'on a effectuer en utilisant la propriété trouver pendant la première question
    cur = tmp
    chemin = [cur]
    for i in range(len(sommets)):
        if che[cur] == None:
            break
        chemin.append(che[cur])
        cur = che[cur]

    chemin.reverse()

    #affichage des resultats
    res = min([dist[i] for i in id_arr])
    if res == float("Inf"):
        print("il n'y a pas de moyen d'atteindre " + end + " depuis " + start)
    else:
        print("Le chemin le plus rapide de Type4 de "+ start +" à " +end + " est", end =" ")
        for p in chemin:
            print(sommets[p], end =" ")
        print("avec une distance de "+ str(res))


