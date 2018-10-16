def initVect(n,a):

    #Initialisation d'un vecteur de taille n et de valeur numérique a
    
    V=[]
    for j in range(n):
        V.append(a)
    return V


def initVectList(n):
    
   #Initialisation d'un vecteur à n listes vides
   
    V=[]
    for j in range(n):
        V.append([])
    return V


def initMat(n,a):

    #création d'une matrice carrée de taille n initialisée à a
    
    M=[]
    for i in range(n):
        L=[]
        for j in range(n):
            L.append(a)
        M.append(L)
    return M


def affMat(M):

    #Affichage d'une matrice
    
    for i in range(len(M)):
        print(M[i])
