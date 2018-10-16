import lib.vect as Vector

# Fonction auxiliaire récursive qui provoque un parcours en profondeur du graphe à partir d'un sommet i
def profRec(G, i, Visite, ordreVisite):

    #Début du parcours de i
    Visite[i] = 1

    # Première visite
    ordreVisite.append(i)  

    for y in G[i]:
        #Si on a pas visité y
        if Visite[y] == 0:
            profRec(G, y, Visite, ordreVisite)
        else:
            #Revisite de y
            pass

    # Fin du parcours de i

# Effectue le parcours en profondeur du graphe G à partir d'un sommet i
def profond(G, i):

    Visite = Vector.initVect(len(G), 0)
    ordreVisite = []
    profRec(G, i, Visite, ordreVisite)
    return ordreVisite

# Effectue le parcours en profondeur généralisé à tout le graphe G
def profondG(G):

    Visite = Vector.initVect(len(G), 0)
    ordreVisite = []

    for i in range(1, len(G)):
        if Visite[i] == 0:
            ordreSousVisite = []
            profRec(G, i, Visite, ordreVisiteRec)
            ordreVisite.append(ordreVisiteRec)

    return ordreVisite
