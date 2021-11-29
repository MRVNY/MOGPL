import random

def generate_graphe():
    nb_sommet = random.randint(10,61) 
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