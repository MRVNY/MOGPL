import random

def generate_graphe():
    nb_sommet = random.randint(10,27) 
    a = []
    for i in range(nb_sommet-1):
        a.append(random.randint(1,4))

    nb_arc = sum(a)

    sommet = []
    arc = []

    for i in range(nb_sommet):
        sommet.append(chr(65 + i))
    
    for i in range(len(a)):
        for j in range(a[i]):
            s1 = i
            tmp = random.randint(s1+1,s1+4)
            if tmp > nb_sommet-1:
                tmp = nb_sommet-1
            s2 = tmp 
            t = random.randint(i-2,i+5)
            if t <= 0 :
                t = 1
            arc.append((sommet[s1],sommet[s2],t,1))
    
    return [nb_sommet,nb_arc,sommet,arc]


def generate_graphe_sommets(nbsommets):
    sommets = []
    arcs = []

    nbarcs = nbsommets - 1 

    for i in range(nbsommets):
        sommets.append(chr(i%26 + 65) + str(int(i/26)))

    for i in range(len(sommets)-1):
        arcs.append((sommets[i],sommets[i+1],i+1,1))
    
    return [nbsommets,nbarcs,sommets,arcs] 


def generate_graphe_arcs(nbarcs):
    sommets = []
    arcs = []

    nbsommets = 26

    for i in range(nbsommets):
        sommets.append(chr(i + 65))
    
    for i in range(nbarcs):
        s1 = random.randint(0,24)
        s2 = random.randint(s1,25)
        arcs.append((sommets[s1],sommets[s2],1,1)) # On cherche pas a vor l'influence des etiquette donc on les mets toutes a 1

    return [nbsommets,nbarcs,sommets,arcs]


