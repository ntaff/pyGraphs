from vect import *

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

def matriceToListe(M):
    V = initVectList(len(M) + 1)
    for i in range(len(M)):
        for j in range(len(M[i])):
            x = M[i][j]
            while x > 0:
                V[i + 1].append(j + 1)
                x = x - 1
    return V
