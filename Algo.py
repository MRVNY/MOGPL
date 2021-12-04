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

# def Ford_Bellman2(G,source):
#     """
#     Algorithme de Ford Bellman
#     Attention source est l'indice dans arc de notre point de start
#     """
#     nb_sommets, nb_arc, sommet, arc = G
#     distance = [float("Inf")] * nb_sommets
#     distance[source] = 0
#     chemin = [None] * nb_sommets
#     chemin[source] = None

#     for _ in range(nb_sommets - 1):
#         for a, b, c in arc:
#             if distance[a] != float("Inf") and distance[a] + c < distance[b]:
#                 distance[b] = distance[a] + c
#                 chemin[b] = a

#     for a, b, c in arc:
#         if distance[a] != float("Inf") and distance[a] + c < distance[b]:
#             print("Le graphe contient un circuit absorbant")
#             return
        
#     return distance, chemin

def Ford_Bellman(graphe, sStart):
    """
    (int,int,[(str,int)],[(str,int),(str,int),int]), (str,int) , (str,int) -> bool
    """
    nb_sommets, _, sommets, arcs = graphe
    distance = [float("Inf")] * nb_sommets
    distance[sommets.index(sStart)] = 0
    chemin = [None] * nb_sommets

    for _ in range(nb_sommets - 1):
        for sFrom, sTo, sDist in arcs:
            numFrom = sommets.index(sFrom)
            numTo = sommets.index(sTo)
            if distance[numFrom] != float("Inf") and distance[numFrom] + sDist < distance[numTo]:
                distance[numTo] = distance[numFrom] + sDist
                chemin[numTo] = sFrom
                
    for sFrom, sTo, sDist in arcs:
        numFrom = sommets.index(sFrom)
        numTo = sommets.index(sTo)
        if distance[numFrom] != float("Inf") and distance[numFrom] + sDist < distance[numTo]:
            print("Le graphe contient un circuit absorbant")
            return
    return distance, chemin
                
    
def tracer_Chemin(graphe,sStart,sEnd,chemin):
    sommets = graphe[2]
    tmp = sEnd
    out = [tmp[0]]
    
    while tmp != None:
        if out[-1] != tmp[0]: 
            out.append(tmp[0])
        tmp = chemin[sommets.index(tmp)]
    if out[-1] != sStart[0]: 
        out.append(sStart[0])
    out.reverse()
    
    return out

# def if_Existe_Chemin(graphe,sStart,sEnd):
#     """
#     (int,int,[(str,int)],[(str,int),(str,int),int]), (str,int) , (str,int) -> bool
#     verifier s'il existe un chemin entre start et end
#     """
#     arcs = graphe[3]
#     todo = [sStart]
    
#     while todo != []:
#         tmp = todo.pop()
#         for sFrom, sTo, _ in arcs:
#             if sTo == sEnd:
#                 return True
#             if sFrom==tmp:
#                 todo.append(sTo)
#     return False
    
    
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

# Type I : Chemin d’end au plus tôt
def type1(graphe,start,end):
    """
    (int,int,[(str,int)],[(str,int),(str,int),int]), str, str -> [str]
    """
    sommets = graphe[2]
    sEnds = []
    sStarts = []
    for s in sommets:
        if s[0] == end:
            sEnds.append(s)
        if s[0] == start and sStarts==[]:
            sStarts.append(s)

    sStart = sStarts[0]
    dist, chemin = Ford_Bellman(graphe,sStart)
    for sEnd in sEnds:
        if dist[sommets.index(s)] != float("Inf"):
            print("type1: ",tracer_Chemin(graphe,sStart,sEnd,chemin), ", arriver plus tôt: jour",sEnd[1])
            return
        
# Type II : Chemin de start au plus tard
def type2(graphe,start,end):
    """
    (int,int,[(str,int)],[(str,int),(str,int),int]), str, str -> [str]
    """
    sommets = graphe[2]
    iEnds = []
    sStarts = []
    for s in sommets:
        if s[0] == end:
            iEnds.append(sommets.index(s))
        if s[0] == start:
            sStarts.append(s)
            
    sStarts.reverse()
    for sStart in sStarts: 
        dist, chemin = Ford_Bellman(graphe,sStart)
        for i in iEnds:
            if dist[i] != float("Inf"):
                sEnd = sommets[i]
                print("type2: ",tracer_Chemin(graphe,sStart,sEnd,chemin), ", partir plus tard: jour",sStart[1])
                return
    
# Type III : Chemin le plus rapide
def type3(graphe,start,end):
    """
    (int,int,[(str,int)],[(str,int),(str,int),int]), str, str -> [str]
    """
    sommets = graphe[2]
    iEnds = []
    sStarts = []
    for s in sommets:
        if s[0] == end:
            iEnds.append(sommets.index(s))
        if s[0] == start:
            sStarts.append(s)
            
    sStarts.reverse()
    for sStart in sStarts: 
        dist, chemin = Ford_Bellman(graphe,sStart)
        for i in iEnds:
            if dist[i] != float("Inf"):
                sEnd = sommets[i]
                print("type3: ",tracer_Chemin(graphe,sStart,sEnd,chemin), ", Chemin le plus rapide: jour",sStart[1], " - jour",sEnd[1])
                return

# Type IV : Plus court chemin
def type4(graphe,start,end):
    """
    (int,int,[(str,int)],[(str,int),(str,int),int]), str, str -> [str]
    Permet de calculer le chemin le plus rapide de Type IV
    """
    sommets = graphe[2]
    sEnds = []
    sStarts = []

    #recherche de l'emplacement des éléments de début et fin
    # tmp_dep = 0
    # done = False
    # tmp_arr = []
    # for i in sommets:
    #     if i[0] == start and not done:
    #         tmp_dep = sommets.index(i)
    #         done = True

    #     if i[0] == end:
    #         tmp_arr.append(sommets.index(i))

    # id_dep, id_arr = tmp_dep, tmp_arr #emplacement des éléments de début et fin
    
    for s in sommets:
        if s[0] == end:
            sEnds.append(s)
        if s[0] == start and sStarts==[]:
            sStarts.append(s)
            
    #sim_g = simple_graph(graphe) #le graphe dois etre déja conv ! il est ensuite convertie en une version plus simple
    #dist, che = Ford_Bellman(sim_g,id_dep)# On peu maintenant effectuer Ford-Bellman sur le graphe simplifié
    sStart = sStarts[0]
    dist, chemin = Ford_Bellman(graphe,sStart)

    # on a maintenant besoin du point final parmis toute ses posibilitées( celle dans laquelle on est end/le jour d'end )
    m = float("Inf")
    sEnd = None
    for s in sEnds:
        if m > dist[s[1]]:
            m = dist[s[1]]
            sEnd = s

    # # on retrace ensuite le chemin que l'on a effectuer en utilisant la propriété trouver pendant la première question
    # cur = tmp
    # chemin = [cur]
    # for i in range(len(sommets)):
    #     if che[cur] == None:
    #         break
    #     chemin.append(che[cur])
    #     cur = che[cur]

    # chemin.reverse()
    
    trace = tracer_Chemin(graphe,start,sEnd,chemin)

    #affichage des resultats
    res = min([dist[sommets.index(s)] for s in sEnds])
    if res == float("Inf"):
        print("il n'y a pas de moyen d'atteindre " + end + " depuis " + start)
    else:
        print("Le chemin le plus rapide de Type4 de "+ start +" à " +end + " est", end =" ")
        print(trace, end =" ")
        print("avec une distance de "+ str(res))


