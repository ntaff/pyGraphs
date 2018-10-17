import lib.vect as Vector
import DepthFirstSearch as DFS

def isConnexe(G):

    return len(DFS.profondG(G)) == 1


def cyclicRec(G, pere, visite, cycle):
    if cycle[0]:
        return
    visite[pere] = True  # On ne revisite pas
    for voisin in G[pere]:
        if visite[voisin] and voisin != pere:  # Si le voisin est marqué mais pas le pere, il y a un cycle
            cycle[0] = True
            return
        if not visite[voisin]:
            cyclicRec(G, voisin, visite, cycle)
        else:
            pass
        
 
def is_cyclic(G):

    visite = Vector.initVect(len(G), False)
    cyclic = [False]

    for y in range(0, len(G)):
        if not visite[y]:
            cyclicRec(G, y, visite, cyclic)
        if cyclic[0]:
            break
    return cyclic[0]


def isArbre(G):

    return isConnexe(G) and not is_cyclic(G)
