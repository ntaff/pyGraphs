import lib.vect as Vector

def nbSommets(G):
    return len(G)-1

def nbArcs(G):
    return len(G)
    
def ajoutArc(G,i,j):
    G[i].append(j)
    

def enleveArc(G,i,j):
    G[i].remove(j)
           
def degS(G,i):
    return len(G[i])

def degreS(G):
    D=[]
    for i in range(1,len(G)):
        D.append(degS(G,i))
    return D

def degE(G,i):
    x = 0
    for k in range(len(G)):
        for j in G[k]:
            if j==i :
                x+=1
    return x
           
def voisinage(G,i):
    L =[]
    for k in range(len(G)):
        for j in range(len(G[k])):
             if G[k][j]==i :
                L.append(k)
    return L

def degreE(G):
    D=[]
    for i in range(1,len(G)):
        D.append(degE(G,i))
    return D     

def listeToMatrice(G):
    M = Vector.initMat(len(G) - 1, 0)
    for i in range(1, len(G)):
        for j in G[i]:
            M[i - 1][j - 1] += 1
    return M


def areteToListe(n, L):
    G = Vector.initVectList(n + 1)
    for i in range(len(L)):
        G[L[i][0]].append(L[i][1])

    return G


def matToListe(M):
    G = Vector.initVectList(len(M) + 1)
    for i in range(len(M)):
        for j in range(len(M[i])):
            x = M[i][j]
            while x > 0:
                G[i + 1].append(j + 1)
                x = x - 1
    return G
