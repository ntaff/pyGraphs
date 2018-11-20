import lib.vect as Vector
from itertools import count, filterfalse


# Détermine le plus petit entier >= 1 qui n’appartient pas à la liste L. On se servira de cette fonction pour déterminer
# la plus petite couleur n’appartenant pas à la liste des couleurs interdites.
def mini(L):
    it = filterfalse(set(L).__contains__, count(1)) #Renvois le plus premier élément qui ne rempli pas la condition du
                                                    #filtre à l'aide d'un compteur
    return next(it) # Vu que it est un itérateur, on utilise la méthode next()


# Détermine une coloration du graphe G par l’algorithme naïf
def colorNaive(G):

    color = Vector.initVect(len(G), 0)  # On initialise le vecteur des couleurs à 0

    for x in range(1, len(G)):
        S = []
        for y in G[x]:
            if color[y] != 0:
                S.append(color[y])
        color[x] = mini(S)

    return color


# Effectue le calcul du noyau d’un ensemble de sommets, c’est à dire une liste maximale de sommets ne contenant pas de
# sommets adjacents.
def noyau(L, G):

    N = []
    while L:
        x = L.pop()
        N.append(x)
        for j in G[x]:
            if j in L:
                L.remove(j)
    return N


# Détermine une coloration du graphe G par l’algorithme glouton
def colorGlouton(G):

    color = Vector.initVect(len(G), 0)  # On initialise le vecteur des couleurs à 0
    S = list(range(1, len(G)))  # Liste des sommets restant à colorier
    c = 1
    while S:
        N = noyau(S.copy(),G) #Les sommets à colorier
        for i in N:
            color[i] = c
            S.remove(i)
        c += 1
    return color


# Détermine une coloration du graphe G par l’algorithme de Welsh et Powell.
def colorWP(G):

    color = Vector.initVect(len(G), 0)  # le vecteur des couleurs
    color[1] = 1

    # Calcul des degrés de chaque sommet
    Deg = []
    for i in range(1, len(G)):
        Deg.append([i, len(G[i])])
    # On tri par degré décroissant
    Deg = sorted(Deg, key=lambda x: x[1], reverse=True)
    print(Deg)
    # On lance la coloration
    for x in range(len(Deg)):
        sommet=Deg[x][0]
        S=[]
        for j in G[sommet]:
            if color[j]:
                S.append(color[j])
        color[sommet]=mini(S)
    return color


# BACKTRACKING

# Verifie si tous les sommets voisins sont d'une couleur differente
def is_valid(G, i, solution):
    
    for x in G[i]:
        if solution[x] == solution[i]:
            return False

    return True


def backtracking_rec(G, colors, i, solution, solutionList):
    if i == len(G):
        solutionList.append(solution[:])
    else:
        for color in colors:
            solution[i] = color
            if is_valid(G, i, solution):
                backtracking_rec(G, colors, i+1, solution, solutionList)
            solution[i] = 0


def backtracking(G, colors=None):
    solutionList = []

    # On a fourni une liste de couleur a tester
    if colors:
        backtracking_rec(G, colors, 1, [0] * len(G), solutionList)
    # On test avec le moins de couleur possible jusqu'a avoir une solution
    else:
        n = 2
        while not solutionList:
            backtracking_rec(G, list(range(1, n)), 1, [0] * len(G), solutionList)
            n +=1

    return solutionList
