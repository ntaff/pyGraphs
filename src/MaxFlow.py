import lib.vect as Vector

"""
Transforme une liste d'arcs avec ses flots et sa capacité maximale

E:	
	n: int -> nombre de sommets du graphe
	L: list of list -> liste d'arcs possédant i,j,flot et capacité maximale

S:	
	P: list of list -> Liste de prédécesseurs
	G: list of list -> Liste d'adjacence
	C: list of list -> Matrice de capacité maximale
	F: list of list -> Matrice de flots	
"""
def arcsToListes(n,L):
	P = Vector.initVectList(n+1) #Liste des prédécesseurs
	G = Vector.Vector.Vector.initVectList(n+1) #Liste d'adjacence
	C = Vector.Vector.initMat(n+1, float("inf")) #Matrice des capacités maximales
	F = Vector.initMat(n+1, float("inf")) #Matrice des flots

	for i,j,flot,cap in L:
		G[i].append(j)
		P[j].append(i)
		F[i][j] = flot
		C[i][j] = cap

	return (G,P,C,F)


"""
Calcule une chaîne augmentante du graphe G

E:	
	P: list of list -> Liste de prédécesseurs
	G: list of list -> Liste d'adjacence
	C: list of list -> Matrice de capacité maximale
	F: list of list -> Matrice de flots	
	s: int -> la source

S:	
	-: bool -> True si une chaîne augmentante a été trouvée, False sinon
	pere: list -> Vecteur des pères de la chaîne augmentante
	e: int -> la quantité qu'il faudra ajouter (ou diminuer) aux arcs de la chaîne augmentante
			  (vaudra 0 s'il n'y a plus de chaînes augmentantes)
"""
def chaineAugmentante(P,G,C,F,s):
	p = len(G)-1 #indice du puits

	visite = Vector.initVect(len(G),0)
	delta = Vector.initVect(len(G),0)
	pere = Vector.initVect(len(G),float("inf"))

	visite[s] = 1
	delta[s] = float("inf")
	pere[s] = float("inf")

	File = [s]


	while File != [] and visite[p] == 0:
		#print(visite, pere)

		sommet = File.pop(0)

		for succ in G[sommet]:
			if visite[succ] == 0 and F[sommet][succ] < C[sommet][succ]:
				visite[succ] = 1
				pere[succ] = sommet
				delta[succ] = min(delta[sommet], C[sommet][succ] - F[sommet][succ])
				File.append(succ)

		for pred in P[sommet]:
			if pred == 0 and F[pred][sommet] > 0:
				visite[pred] = 1
				pere[pred] = -sommet
				delta[pred] = min(delta[sommet], F[pred][sommet])
				File.append(pred)

	if visite[p] == 1:
		print("Il y a une chaîne augmentante")
		e = delta[p] #Le delta pour cette chaîne augmentante
		return True, pere, e
	else:
		print("Il n'y a pas de chaîne augmentante: le flot est optimal!")
		return False, pere, 0



"""
Met à jour une chaîne augmentante de G

E:	
	F: list of list -> Matrice de flots
	pere: list -> Vecteur des pères pour la chaîne augmentante
	e: int -> quantité à ajouter (ou enlever) aux arcs de la chaîne

S: -

"""
def updateChaine(F,pere,e):
	j = len(pere)-1
	i = pere[j]

	while i != float("inf"): #tant que i n'est pas la source
		if i > 0: #arc en avant
			print("f(%d,%d) = %d + %d = %d"%(i,j,F[i][j],e, F[i][j] + e))
			F[i][j] += e
		else: #arc en arrière
			i = -i #Pour avoir la valeur absolue de i
			F[j][i] -= e
			print("f(%d,%d) = %d - %d = %d"%(j,i,F[j][i], e, F[j][i]-e))

		j=i
		i=pere[j]


"""
Applique l'algorithme de Ford-Fulkerson au graphe G

E:
	P: list of list -> Liste de prédécesseurs
	G: list of list -> Liste d'adjacence
	C: list of list -> Matrice de capacité maximale
	F: list of list -> Matrice de flots	
	s: int -> la source

S:
	FlotMax: int -> le flot maximal pour le graphe G

"""
def fordFulkerson(P,G,C,F,s):
	print("Recherche d'une chaîne augmentante...\n")
	chaine_augmentante, pere, e = chaineAugmentante(P,G,C,F,s)
	if chaine_augmentante:
		print("Vecteur des pères: ",pere)
		print("e =",e)
		print()
		print("Mise à jour de la chaîne augmentante:")
		updateChaine(F,pere,e)
		print()
		return fordFulkerson(P,G,C,F,s)
	else:
		print()
		FlotMax = 0
		for succ in G[s]: #FlotMax = f+(s)
			FlotMax += F[s][succ]
		return FlotMax
