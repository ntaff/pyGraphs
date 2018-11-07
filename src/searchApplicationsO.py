def cyclicRec(G, i, Visite, cycle):
    Visite[i] = 1
    #Début du parcours de i
    for y in G[i]:
        if Visite[y] == 0:
            if cyclicRec(G, y, Visite, cycle):
                return True
        else:
            #Revisite de y
            return True
    Visite[i] = 0
    return False
    #Fin du parcours de i


def isCyclic(G):
    Visite = Vector.initVect(len(G), 0)
    for i in range(1, len(G)):
        if cyclicRec(G, i, Visite, False):
            return True
    return False
