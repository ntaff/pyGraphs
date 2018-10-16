import lib.vect as Vector


def largeur(G, i):
    #Parcours en largeur simple à partir d'un sommet donné en paramètre
    
    # Initialisation
    Visite = Vector.initVect(len(G), False) #Quels sommets ont déjà été visités
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

def largeurG(G):
    
    # Effectue le parcours en largeur généralisé à tout le graphe G
 
    Visite = Vector.initVect(len(G), 0)
    ordreVisite = []
    File = []
    for i in range(1, len(G)):
        if Visite[i] == 0:
            ordreSousVisite = []
            File.append(i)
            Visite[i] = 1
            #Parcours à partir de i
            while File:
                y = File.pop(0)
                ordreSousVisite.append(y)
                # Visite de y
                for z in G[y]:
                    if Visite[z] == 0:
                        Visite[z] = 1
                        File.append(z)
                        #On ajoute z à la file d'attente
                        else:
                        #Revisite de z
                        pass
            ordreVisite.append(ordreSousVisite)
    return ordreVisite
