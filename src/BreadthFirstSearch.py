from vect import *

#Parcours en largeur simple à partir d'un sommet donné en paramètre
def largeur(G, i):
    # Initialisation
    Visite = initVect(len(G), False) #Quels sommets ont déjà été visités
    File = [i] #Liste d'attente
    ordreVisite = [] #Ordre de visite des sommets
    Visite[i] = True  # On traite premier sommet
    # Parcours
    while len(File) != 0: #Tant que la liste d'attente n'est pas vide
        x = File[0] #On prend le premier element de la liste d'attente
        File.pop(0) # On enlève le sommet que l'on traite de la file
        ordreVisite.append(x) #On rejoute le sommet traité à la liste de visite
        # Parcours des successeurs
        for succ in G[x]:
            if Visite[succ] == False: #Si on a pas visité le sommet
                Visite[succ] = True #On le visite
                File.append(succ) #Et on l'ajoute à la liste d'attente
            # sinon révisite
    return ordreVisite #On renvoit la liste finale dans l'ordre de visite
	
##JEU DE TESTS

G1 = [[],[5],[1,4],[2],[3],[2,4]]
G2 = [[],[5],[1,4,5],[2,4],[],[4]]
G3 = [[],[3,5,6],[1],[2,4],[],[],[4]]
Petersen = [[],[2,5,6],[1,3,7],[2,4,8],[3,5,9],[1,4,10],[1,8,9],[2,9,10],[3,6,10],[4,6,7],[5,7,8]]


  print(largeur(G1, 1)) ## ---> [1, 5, 2, 4, 3]
	print(largeur(G2, 1)) ## ---> [1, 5, 4]
	print(largeur(G3, 1)) ## ---> [1, 3, 5, 6, 2, 4]
	print(largeur(Petersen, 1)) ## ---> [1, 2, 5, 6, 3, 7, 4, 10, 8, 9]
	print(largeur(G1, 3)) ## ---> [3, 2, 1, 4, 5]
	print(largeur(Petersen, 7)) ## ---> [7, 2, 9, 10, 1, 3, 4, 6, 5, 8]
