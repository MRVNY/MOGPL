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
    som_courant = sommet[tmp]

    #tant que l'on arrive pas à la fin on passe a l'arc suivant      
    return CPR(arc,sommet,som_courant,arrive)

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
    Attention source est l'indice dans arc de notre point de départ
    """
    nb_som, nb_arc, sommet, arc = G
    distance = [float("Inf")] * nb_som
    distance[source] = 0
    chemin = [None] * nb_som
    chemin[source] = None

    for _ in range(nb_som - 1):
        for a, b, c in arc:
            if distance[a] != float("Inf") and distance[a] + c < distance[b]:
                distance[b] = distance[a] + c
                chemin[b] = a

    for a, b, c in arc:
        if distance[a] != float("Inf") and distance[a] + c < distance[b]:
            print("Le graphe contient un circuit absorbant")
            return
    
    return distance, chemin
    
def simple_graph(G):
    """Permet de simplifier les graphiques ( convertir les sommets en entier) """
    nb_som, nb_arc, sommet, arc = G

    sommet_simple = [0] * nb_som
    arc_simple = [0] * nb_arc

    for i in range(nb_som):
        sommet_simple[i] = i
    
    for i in range(nb_arc):
        arc_simple[i] = (sommet.index(arc[i][0]),sommet.index(arc[i][1]),arc[i][2])
    return [nb_som,nb_arc,sommet_simple,arc_simple]

def type4(graphe,départ,arrivé):
    """Permet de calculer le chemin le plus rapide de Type IV"""
    som, arc = graphe[2], graphe[3]

    #recherche de l'emplacement des éléments de début et fin
    tmp1 = 0
    done = False
    tmp2 = []
    for i in som:
        if i[0] == départ and not done:
            tmp1 = som.index(i)
            done = True

        if i[0] == arrivé:
            tmp2.append(som.index(i))

    id_dep, id_arr = tmp1, tmp2 #emplacement des éléments de début et fin
    sim_g = simple_graph(graphe) #le graphe dois etre déja conv ! il est ensuite convertie en une version plus simple
    dist, che = Ford_Bellman(sim_g,id_dep)# On peu maintenant effectuer Ford-Bellman sur le graphe simplifié

    # on a maintenant besoin du point final parmis toute ses posibilitées( celle dans laquelle on est arrivé/le jour d'arrivée )
    m = float("Inf")
    tmp = 0
    for i in id_arr:
        if m > dist[i]:
            m = dist[i]
            tmp = i

    # on retrace ensuite le chemin que l'on a effectuer en utilisant la propriété trouver pendant la première question
    cur = tmp
    chemin = [cur]
    for i in range(len(som)):
        if che[cur] == None:
            break
        chemin.append(che[cur])
        cur = che[cur]

    chemin.reverse()

    #affichage des resultats
    res = min([dist[i] for i in id_arr])
    if res == float("Inf"):
        print("il n'y a pas de moyen d'atteindre " + arrivé + " depuis " + départ)
    else:
        print("Le chemin le plus rapide de Type4 de "+ départ +" à " +arrivé + " est", end =" ")
        for p in chemin:
            print(som[p], end =" ")
        print("avec une distance de "+ str(res))


