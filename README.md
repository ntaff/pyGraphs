# pyGraphs library

This repository contain some functions for manipulating [graphs objects](https://en.wikipedia.org/wiki/Graph_(discrete_mathematics)). 

The librairy now contain the following files :

1. `vect.py`: Contains primitives for the treatment of vectors and matrices (with python's lists)

2. `basicsNO.py`: Contains basics functions to manipulate non oriented graphs
   - `nbSommets(G)` Return the number of nodes from G graph
   - `nbArete(G)` Return the number of edges from G graph
   - `ajouteArete(G,  i, j)` Add an edge between nodes i and j in G graph
   - `enleveArete(G, i, j)` Delete an edge between nodes i and j in G graph
   - `deg(G, i)` Return i's degree
   - `degre(G)` Return G degree
   - `listeToMatrice(G)` Transform adjacency list in adjacency matrix
   - `nonOriente(G)` Verify adjacency list symetry (to verify if G is non-oriented)
   - `kuratowski(n)` Return adjacency list Vector from the n'th Kuratowski graph
   - `areteToListe(n, L)` Transform edges list in adjacency list
   - `matriceToListe(M)` Transform adjacency matrix in adjacency list

3. `basicsO.py`: Contains basics functions to manipulate oriented graphs 
   - `nbSommets(G)` Return the number of nodes from G graph
   - `nbArcs(G)` Return the number of edges from G graph
   - `ajouteArc(G,  i, j)` Add an edge between nodes i and j in G graph
   - `enleveArc(G, i, j)` Delete an edge between nodes i and j in G graph
   - `degS(G, i)` Return i's out-degree
   - `degreS(G)` Return G degree
   - `degE(G, i)` Return i's in-degree
   - `listeToMatrice(G)` Transform adjacency list in adjacency matrix
   - `voisinage(G, i)` Return i's neighborhood 
   - `areteToListe(n, L)` Transform edges list in adjacency list
   - `matToListe(M)` Transform adjacency matrix in adjacency list

4. `BreadthFirstSearch.py`: Implement simple and generalized BF search in graphs
   - `largeur(G, i)` Return nodes visit list for the simple BF search from the i node
   - `largeurG(G)` Return nodes visit list for the generalized BF search

5. `DepthFirstSearch.py`: Implement simple and generalized DF search in graphs
   - `profRec(G, i, Visite, ordreVisite)` Recursive function that do a simple DF search from a node i
   - `profond(G, i)` Return nodes visit list for the simple DF search from the i node
   - `profondG(G)` Return nodes visit list for the generalized DF search
   
6. `searchApplicationsNO.py`: Implement simple and generalized DF search in graphs 
   - `isConnexe(G)`: Return true if G is connected
   - `cyclicRec(G, pere, visite, cycle)`: Recursive cycles detection function
   - `isCyclic(G)`: Return true if G have, at least, one cycle
   - `isArbre(G)`: Return true if G is a tree (connected graph without cycles)


About the authors                                                  {#about}
-----------------

This library was written by Nicolas Taffoureau.
