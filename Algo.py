"""
Structure du graphe:
graphe = (nb_sommets,nb_arc,list(sommet),list(arc))
arc = (sommet,sommet,int)
sommet = (str,int)
"""

def alph(s):
    return s[0]

def Ford_Bellman(graphe, sStart):
    """
    Algo de Bellman
    graphe, sommet -> bool
    (int,int,[(str,int)],[(str,int),(str,int),int]), (str,int) , (str,int) -> bool
    """
    nb_sommets, _, sommets, arcs = graphe
    distance = [float("Inf")] * nb_sommets
    distance[sommets.index(sStart)] = 0
    chemin = [None] * nb_sommets

    #Construire le tableau vu en cours, et le condenser dans une liste (les chemins sont tous gardés)
    for _ in range(nb_sommets - 1):
        for sFrom, sTo, sDist in arcs:
            numFrom = sommets.index(sFrom)
            numTo = sommets.index(sTo)
            if distance[numFrom] != float("Inf") and distance[numFrom] + sDist < distance[numTo]:
                distance[numTo] = distance[numFrom] + sDist
                chemin[numTo] = sFrom
    
    #On verifie s'il existe un circuit absorbant
    for sFrom, sTo, sDist in arcs:
        numFrom = sommets.index(sFrom)
        numTo = sommets.index(sTo)
        if distance[numFrom] != float("Inf") and distance[numFrom] + sDist < distance[numTo]:
            print("Le graphe contient un circuit absorbant")
            return
        
    return distance, chemin
                
    
def tracer_Chemin(graphe,sStart,sEnd,chemin):
    """
    tracer le chemin de sStart à sEnd selon le Bellman
    graphe, sommet, sommet -> bool
    """
    sommets = graphe[2]
    tmp = sEnd
    out = [tmp[0]]
    
    #on part de la fin, lors qu'on n'ateint pas le debut(None), on continue le while
    while tmp != None:
        #On garde qu'une seule fois le sommet, cad (A,1)->(A,2) = A
        if out[-1] != tmp[0]: 
            out.append(tmp[0])
        tmp = chemin[sommets.index(tmp)]
        
    #Si le debut n'est pas la fin (None empeche le dernier sommet a etre ajouté), on le rajoute manuellement
    if out[-1] != sStart[0]: 
        out.append(sStart[0])
    out.reverse()
    
    return out

    
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
    
    #Sommets du debut et de la fin à traiter, déjà triés
    sEnds = []
    sStarts = []
    for s in sommets:
        if s[0] == end:
            sEnds.append(s)
        #On garde le premier debut, Parce qu'on peut en aller partout et on distingue pas les debut
        if s[0] == start and sStarts==[]:
            sStarts.append(s)

    #Bellman
    sStart = sStarts[0]
    dist, chemin = Ford_Bellman(graphe,sStart)
    
    #Trouver S'il existe un chemin, le premier sera le plus petit (puisque déjà trié), et donc sera le resultat
    for sEnd in sEnds:
        if dist[sommets.index(sEnd)] != float("Inf"):
            print("typeI: ",tracer_Chemin(graphe,sStart,sEnd,chemin), ", arriver plus tôt: jour",sStart[1], " - jour",sEnd[1])
            return
        
    print("Pas de chemin")
    return
        
        
# Type II : Chemin de start au plus tard
def type2(graphe,start,end):
    """
    (int,int,[(str,int)],[(str,int),(str,int),int]), str, str -> [str]
    """
    sommets = graphe[2]
    
    #Sommets du debut et de la fin à traiter, déjà triés
    #Ici on garde les debuts parce qu'il faut distinguer les debuts, mais on ne garde que la derniere fin
    iEnds = [None]
    sStarts = []
    for s in sommets:
        if s[0] == end:
            iEnds[0] = sommets.index(s)
        if s[0] == start:
            sStarts.append(s)
    
    #Bellman sur chaque sommets de debut 
    sStarts.reverse() #parce que le plus grand est le meilleur
    for sStart in sStarts: 
        dist, chemin = Ford_Bellman(graphe,sStart)
        for i in iEnds:
            if dist[i] != float("Inf"): #S'il existe un chemin du premier debut à n'inporte quelle fin, on arrete
                sEnd = sommets[i]
                print("typeII: ",tracer_Chemin(graphe,sStart,sEnd,chemin), ", partir plus tard: jour",sStart[1], " - jour",sEnd[1])
                return
    
    print("Pas de chemin")
    return
    
    
# Type III : Chemin le plus rapide
def type3(graphe,start,end):
    """
    (int,int,[(str,int)],[(str,int),(str,int),int]), str, str -> [str]
    """
    sommets = graphe[2]
    
    #Ici on garde tous les debuts et fin parce qu'il faut distinguer les 2
    iEnds = []
    sStarts = []
    for s in sommets:
        if s[0] == end:
            iEnds.append(sommets.index(s))
        if s[0] == start:
            sStarts.append(s)
       
    #Bellman     
    sStarts.reverse()
    
    chemins = []
    durs = []
    for sStart in sStarts: 
        dist, chemin = Ford_Bellman(graphe,sStart)
        for i in iEnds:
            if dist[i] != float("Inf"):
                sEnd = sommets[i]
                chemins.append((sStart,sEnd))
                durs.append(sEnd[1]-sStart[1])
    
    if durs==[]:
        print("Pas de chemin")
        return
    (sStart,sEnd) = chemins[durs.index(min(durs))]
    print("typeIII: ",tracer_Chemin(graphe,sStart,sEnd,chemin), ", Chemin le plus rapide: jour",sStart[1], " - jour",sEnd[1])
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
    
    for s in sommets:
        if s[0] == end:
            sEnds.append(s)
        if s[0] == start and sStarts==[]:
            sStarts.append(s)
            
    sStart = sStarts[0]
    dist, chemin = Ford_Bellman(graphe,sStart)

    # on a maintenant besoin du point final parmis toute ses posibilitées( celle dans laquelle on est end/le jour d'end )
    m = float("Inf")
    sEnd = None
    for s in sEnds:
        if m > dist[s[1]]:
            m = dist[s[1]]
            sEnd = s

    # on retrace ensuite le chemin que l'on a effectuer en utilisant la propriété trouver pendant la première question
    trace = tracer_Chemin(graphe,sStart,sEnd,chemin)

    #affichage des resultats
    res = min([dist[sommets.index(s)] for s in sEnds])
    if res == float("Inf"):
        print("il n'y a pas de moyen d'atteindre " + end + " depuis " + start)
    else:
        print("Le chemin le plus rapide de TypeIV de "+ start +" à " +end + " est", end =" ")
        print(trace, end =" ")
        print("avec une distance de "+ str(res))


