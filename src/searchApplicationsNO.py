import lib.vect as Vector
import DepthFirstSearch as DFS

def isConnexe(G):

    return len(DFS.profondG(G)) == 1
