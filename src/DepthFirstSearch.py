import lib.vect as Vector

def profRec(G, i, Visite, ordreVisite):

   # Fonction auxiliaire récursive qui provoque un parcours en profondeur du graphe à partir d'un sommet i
   # Met à jour les paramètres Visite et ordreVisite
   
    Visite[i] = 1
    #Début du parcours de i
    ordreVisite.append(i)  # Première visite

    for y in G[i]:
        if Visite[y] == 0:
            profRec(G, y, Visite, ordreVisite)
        else:
            #Revisite de y
            pass

    # Fin du parcours de i


def profond(G, i):

   # Effectue le parcours en profondeur du graphe G à partir d'un sommet i
  
    Visite = Vector.initVect(len(G), 0)
    ordreVisite = []
    profRec(G, i, Visite, ordreVisite)
    return ordreVisite


def profondG(G):

   # Effectue le parcours en profondeur généralisé à tout le graphe G

    Visite = Vector.initVect(len(G), 0)
    ordreVisite = []

    for i in range(1, len(G)):
        if Visite[i] == 0:
            ordreSousVisite = []
            profRec(G, i, Visite, ordreSousVisite)
            ordreVisite.append(ordreSousVisite)

    return ordreVisite
