# pyGraphs library

This repository contain some functions for manipulating [graphs objects](https://en.wikipedia.org/wiki/Graph_(discrete_mathematics)). 

The librairy now contain the following files :

1. `vect.py`: Contains primitives for the treatment of vectors and matrices (with python's lists)

2. `basicsNO.py`: Contains basics functions to manipulate non oriented graphs 

3. `basicsO.py`: Contains basics functions to manipulate oriented graphs 

4. `BreadthFirstSearch.py`: Implement simple and generalized BF search in graphs
   - `largeur(G, i)` Return nodes visit list for the simple BF search from the i node
   - `largeurG(G)` Return nodes visit list for the generalized BF search

5. `DepthFirstSearch.py`: Implement simple and generalized DF search in graphs

6. `searchApplicationsNO.py`: Implement simple and generalized DF search in graphs 
   - `isConnexe(G)`: Return true if G is connected


About the authors                                                  {#about}
-----------------

This library was written by Nicolas Taffoureau.
