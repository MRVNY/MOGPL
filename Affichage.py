import graphviz

#ATTENTION ! 
#Il faut avoir installer une extention Graphviz pour que cette 
#partie fonctionne. Il est donc impossible de l'utiliser sans 
#l'installation de ce dernier.

def aff_graphe(graphe):
    """Permet d'afficher un graphique grâce a l'extention graphviz"""
    nb_som, nb_arc, sommet_prime, arc_prime = graphe

    f = graphviz.Digraph('G\'', filename='fsm.gv')
    f.attr(rankdir='LR', size='8,5')
    f.attr('node', shape='circle')

    for a in arc_prime:
        f.edge(str(a[0]),str(a[1]), label=str(a[2]))

    f.view()