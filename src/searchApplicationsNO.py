import lib.vect as Vector
import DepthFirstSearch as DFS

def isConnexe(G):

    #Le graphe est connexe seulement si le parcours en profondeur
    #généralisé retourne une seule composante connexe
    return len(DFS.profondG(G)) == 1


def cyclicRec(G, pere, visite, cycle):
    if cycle[0]: #Si le graph est cyclique, on retourne vrai sans poursuivre
        return #On retourne vrai
    visite[pere] = True  # On ne revisite pas un sommet deja visité
    for voisin in G[pere]: #Pour tout les voisin sommet
        if visite[voisin] and voisin != pere:  # Si le voisin est marqué mais pas le pere, il y a un cycle
            cycle[0] = True #On détecte un cycle
            return #On retourne vrai sans poursuivre
        if not visite[voisin]: #Si on a pas visité le voisin du sommet
            cyclicRec(G, voisin, visite, cycle) #On le visite
        else: #Sinon
            pass #On poursuit
        
 
def is_cyclic(G):

    visite = Vector.initVect(len(G), False) #Vecteur de visite des sommets
    cyclic = [False] #On prend l'hypothèse que le graphe n'est de base pas cyclique

    for y in range(0, len(G)): #Pour tout les sommets de G
        if not visite[y]: #Si on a pas visité le sommet
            cyclicRec(G, y, visite, cyclic) #Appel à la fonction recursive
        if cyclic[0]: #Si le graph est cyclique, on retourne vrai sans poursuivre
            break #On sort de la boucle
    return cyclic[0] #Si on a parcouru tout le graphe, on retourne si le graphe est cyclic ou non


def isArbre(G):

    #Un graphe est un arbre si il est connexe mais pas cyclique.
    return isConnexe(G) and not is_cyclic(G) 
