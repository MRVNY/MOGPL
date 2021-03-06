import numpy as np
import sys 
import graphviz
import re
from Affichage import aff_graphe
from Generate import generate_graphe, generate_graphe_arcs, generate_graphe_sommets
from Algo import * 
from Programmation_Lineaire import conversion_PL
import time
import matplotlib.pyplot as plt

################################# RECUPERATION GRAPHE #################################

def parser():
    #recuperation des graphe sur le terminal
    nbSommet = int(input("Entrez le nombre de Sommet :"))
    nbArcs = int(input("Entrez le nombre d'Arcs :"))

    #sommet
    sommet = []
    for s in range (nbSommet):
        sommet.append(str(input("Sommet " + str(s+1) + " : ")))

    #arc
    arc = []
    for a in range (nbArcs):
        tmp = str(input("Arc " + str(a+1) + " (format : (u,v,t,lambda) : "))

        arc.append((str(tmp[1]),str(tmp[3]),int(tmp[5]),int(tmp[7])))
    
    #vérification du graphe
    allsom = []
    for a in arc:
        allsom.append(a[0])
        allsom.append(a[1])

    list_of_unique_som = []
    for unique in set(allsom):
        list_of_unique_som.append(unique)
    
    list_of_unique_som.sort()
    sommet.sort()

    #si le graphique contient des erreurs ( arc contenant des sommets inexistant)
    #le programme s'arrete.
    if list_of_unique_som != sommet :
        print("le graphique ne semble pas correct")
        sys.exit()
    

    return [nbSommet,nbArcs,sommet,arc]

def menu():
    #menu du programme
    mode = int(input("Entrez le mode de saisie de votre mutligraphe (1-Saisie au terminal ou 2-Saisie dans un fichier): "))
    if(mode ==  1):
        return parser()
    elif(mode == 2):
        filename = (str(input("Entrer le fichier: ")))
        return fichier(filename)
    else:
        print("Votre sélection ne correspond a aucun mode disponible")
        menu()


def fichier(filename):
    file = open(filename, 'r')

    #recuperation des graphe dans le fichier
    nbSommet = int(file.readline())
    nbArcs = int(file.readline())

    #sommet
    sommet = []
    for s in range (nbSommet):
        sommet.append(file.readline()[0])

    #arc
    arc = []
    for a in range (nbArcs):
        tmp = file.readline()
        t = re.findall("^.{5}(\d*)",tmp)
        l = re.findall("(\d*)\)$",tmp)
        arc.append((str(tmp[1]),str(tmp[3]),int(t[0]),int(l[0])))
    
    #vérification du graphe
    allsom = []
    for a in arc:
        allsom.append(a[0])
        allsom.append(a[1])

    list_of_unique_som = []
    for unique in set(allsom):
        list_of_unique_som.append(unique)
    
    list_of_unique_som.sort()
    sommet.sort()

    #print(list_of_unique_som,"\n",sommet)

    if list_of_unique_som != sommet :
        print("le graphique ne semble pas correct")
        sys.exit()
    
    file.close()
    return [nbSommet,nbArcs,sommet,arc]

################################# CONVERSION GRAPHIQUE PRIME #################################

def conv_graphe(graphe):
    nb_s , nb_a, sommet, arc = graphe
    #calcul des sommets entrant et sortant

    sommet_in = []
    sommet_out = []

    #On construit le tableau des arc in & out a partir d'un graphique
    for s in sommet:
        i, o = [], []
        for a in arc:
            if(a[1] == s):
                if (s,a[2]+a[3]) not in i:
                    i.append((s,a[2]+a[3]))
            if(a[0] == s):
                if(s,a[2]) not in o:
                    o.append((s,a[2]))
        sommet_in.append(i)
        sommet_out.append(o)

    #print(sommet_in, "\n", sommet_out)

    sommet_prime = []

    #ajout de tout nos sommets dans un seul tableau
    for s in sommet_in:
        if(len(s) == 0):
            continue
        sommet_prime.extend(s)
    for s in sommet_out:
        if(len(s) == 0):
            continue
        sommet_prime.extend(s)

    sommet_prime.sort()

    arc_prime = []

    #on ajoute les arc simple, ceux lier d'un meme point a un autre
    for i in range(len(sommet_prime)-1):
        if(sommet_prime[i][0] == sommet_prime[i+1][0] and sommet_prime[i][1] != sommet_prime[i+1][1]):
            arc_prime.append((sommet_prime[i], sommet_prime[i+1],0))
    
    #on complète les arc avec le reste des arcs de sommet du premier graphe
    for a in arc:
        arc_prime.append(((a[0],a[2]),(a[1],a[2]+a[3]),a[3]))    

    sommet_prime.sort(key=alph)#pour plus de clareté on trie 

    return (len(sommet_prime),len(arc_prime),sommet_prime,arc_prime)

def main():
    graphe = menu()
    print("Maintenant vous allez pouvoir entrer deux sommets pour chercher les chemins :")
    start = str(input("Partir de : "))
    end = str(input("Et Finir en :"))

    type1(conv_graphe(graphe),start,end)
    type2(conv_graphe(graphe),start,end)
    type3(conv_graphe(graphe),start,end)
    type4(conv_graphe(graphe),start,end)
    conversion_PL(conv_graphe(graphe),start,end)


################################# TEST #################################

def test_sommets_guroby():
    filename = "test_sommets.txt"
    fichier = open(filename,'w')
    ite = [i for i in range(10,510,10)]
    res = []
    for i in range(10,510,10):
        g = generate_graphe_sommets(i)
        start, end = g[2][0], g[2][-1]
        ts = time.time()
        conversion_PL(conv_graphe(g),start,end)
        te = time.time() - ts
        fichier.writelines( str(te) + " \n")
        #fichier.writelines("Pour " + str(i) + " sommets, temps d'execution (en seconde) : " + str(te) + " \n")
        res.append(te)
    _, ax = plt.subplots()  
    ax.plot(ite, res)  
    ax.set_xlabel('Nombre de sommets')  
    ax.set_ylabel('Temps d\'exécution (en seconde)') 
    ax.set_title("Temps de recherche du plus cours chemin en fonction du nombre de Sommets")  
    plt.show()

    fichier.close()

    return ite, res


def test_arcs_guroby():
    filename = "test_arcs.txt"
    fichier = open(filename,'w')
    ite = [i for i in range(100,2010,10)]
    res = []
    for i in range(100,2010,10):
        g = generate_graphe_arcs(i)
        start, end = g[2][0], g[2][-1]
        ts = time.time()
        conversion_PL(conv_graphe(g),start,end)
        te = time.time() - ts
        fichier.writelines( str(te) + " \n")
        #fichier.writelines("Pour " + str(i) + " arcs, temps d'execution (en seconde) : " + str(te) + " \n")
        res.append(te)
    
    _, ax = plt.subplots()  
    ax.plot(ite, res)  
    ax.set_xlabel('Nombre d\'arc')  
    ax.set_ylabel('Temps d\'exécution (en seconde)') 
    ax.set_title("Temps de recherche du plus cours chemin en fonction du nombre de d\'Arc")  
    plt.show()

    fichier.close()

def test_sommets_typeIV():
    filename = "test_sommets.txt"
    fichier = open(filename,'w')
    ite = [i for i in range(10,510,10)]
    res = []
    for i in range(10,510,10):
        g = generate_graphe_sommets(i)
        start, end = g[2][0], g[2][-1]
        ts = time.time()
        type4(conv_graphe(g),start,end)
        te = time.time() - ts
        fichier.writelines( str(te) + " \n")
        #fichier.writelines("Pour " + str(i) + " sommets, temps d'execution (en seconde) : " + str(te) + " \n")
        res.append(te)
    _, ax = plt.subplots()  
    ax.plot(ite, res)  
    ax.set_xlabel('Nombre de sommets')  
    ax.set_ylabel('Temps d\'exécution (en seconde)') 
    ax.set_title("Temps de recherche du plus cours chemin en fonction du nombre de Sommets")  
    plt.show()

    fichier.close()

    return ite, res


################################# MAIN #################################

#les éléments sont commenter pour simplifier les tests
#menu()
#parser()
#print(conv_graphe(fichier("graphe.txt")))
#génere un graphe aléatoire 
#graphe_aleatoire = generate_graphe()

#ATTENTION ! Ne fonctionne pas sans Graphviz
#aff_graphe(fichier("graphe_complexe.txt"))
#aff_graphe(conv_graphe(fichier("graphe.txt")))
#aff_graphe(simple_graph(conv_graphe(fichier("graphe.txt"))))

#print(graphe_aleatoire[2])
#aff_graphe(graphe_aleatoire)
#aff_graphe(conv_graphe(graphe_aleatoire))

#print(chemin_plus_rapide(conv_graphe(fichier("graphe_complexe.txt")),"A","G"))
#print(Ford_Bellman(simple_graph(conv_graphe(fichier("graphe_complexe.txt"))),0))

#aff_graphe((conv_graphe(fichier("graphe.txt"))))
#print(conv_graphe(fichier("graphe.txt")))

# type1(conv_graphe(graphe_aleatoire),"A",graphe_aleatoire[2][-1][0])
# type2(conv_graphe(graphe_aleatoire),"A",graphe_aleatoire[2][-1][0])
# type3(conv_graphe(graphe_aleatoire),"A",graphe_aleatoire[2][-1][0])
# type4(conv_graphe(graphe_aleatoire),"A",graphe_aleatoire[2][-1][0])
#aff_graphe(simple_graph(conv_graphe(fichier("graphe.txt"))))
#conversion_PL(conv_graphe(fichier("graphe.txt")),"A","F")

#main()

i1,r1 = test_sommets_guroby()
i2,r2 = test_sommets_typeIV()

_, ax = plt.subplots()  
ax.plot(i1, r1,color = 'tab:blue', label = 'Fonction conversion_PL')  
ax.plot(i2, r2,color = 'tab:orange', label = 'Fonction typeIV')  
ax.set_xlabel('Nombre de sommets')  
ax.set_ylabel('Temps d\'exécution (en seconde)') 
ax.set_title("Temps de recherche du plus cours chemin en fonction du nombre de Sommets")  
plt.legend()
plt.show()