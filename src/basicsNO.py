import vect

G=[[],[2,5,5],[1,3,4,4],[2,3,4],[2,2,3,5],[1,1,4]]
L=[[1,2],[1,5],[1,5],[2,3],[2,4],[2,4],[3,3],[3,4],[4,5]]


def nbSommets(G):
    return (len(G)-1)


def nbArete(G):
    n = 0
    for sommet in G:
        n += len(sommet)
    return n


def ajouteArete(G,  i, j):
     G.append([i, j])
     return G


def enleveArete(G, i, j):
    G[i].remove(j)
    G[j].remove(i)
    return G


def deg(G, i):
    return len(G[i])


def degre(G):
    V = initVect((len(G)-1), 0)
    print(V)
    for sommet in range(1, len(G)):
        V[sommet-1]=deg(G, sommet)
    return V


def listeToMatrice(G):

    matAdj = initMat((len(G) - 1), 0)
    for i in range(1,len(matAdj)):
        for j in range(1, len(matAdj[i])):
            for k in G[i+1]:
                 if k == j+1:
                     matAdj[i][j] = matAdj[i][j]+1

    return matAdj

def nonOriente(G):
        matAdj=listeToMatrice(G)
        for i in range(len(matAdj)-1):
            for j in range(len(matAdj)-1):
                if matAdj[i][j] != matAdj[j][i]:
                    return False
        return True


def kuratowski(n):
    V = initVectList(n+1)
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j:
                pass
            else:
                V[i].append(j)
    return V

def areteToListe(n, L):
    V = initVectList(n)
    for i in range(0,len(L)):
            V[L[i][0]].append(L[i][-1])
            V[L[i][-1]].append(L[i][0])
    return V

#Retourne la liste de tous les degrés
if __name__ == "__main__":
    print("Nombre de sommet du graphe G :", nbSommets(G))
    print("Nombre d'aretes du graphe G :", nbArete(G))
    print("L'arete a bien été ajouté, voici le nouveau graphe :", ajouteArete(G, 4, 6))
    print("L'arete a bien été enlevée, voici le nouveau graphe :", enleveArete(G, 1, 5))

    n = 2
    print("Voici le degré du sommet ", n , " dans le graphe G :", deg(G, 2))

    print("Voici la liste des degrés du graphes G : ", degre(G))
    print("Le graphe est il non orienté ?........ La réponse est :", nonOriente(G))

    p = 5
    print("Le graphe complet (ou de kuratowski)", p, "a pour listes d'adjacences :", kuratowski(p))

    print("Voici la liste d'adjacence V associée à la liste d'arete L :", areteToListe(nbSommets(G),L))
