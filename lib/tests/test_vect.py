import vect as Vector
vect.path[:0] = ['../']
import unittest


class testVect(unittest.TestCase):

    """Test case utilisé pour tester les fonctions du module 'vect'."""

    def test_initVect(self):
        """Test le fonctionnement de la fonction 'vect.initVect'."""
        vect = Vector.initVect(5,0)
        self.assertEqual(vect, [0, 0, 0, 0, 0])

    def test_initVectList(self):
        """Test le fonctionnement de la fonction 'vect.initVectList'."""
        vectList = Vector.initVectList(5)
        self.assertEqual(vectList, [[], [], [], [], []])

    def test_initMat(self):
        """Test le fonctionnement de la fonction 'vect.initMat'."""
        vectMat = Vector.initMat(5,0)
        self.assertEqual(vectMat, [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])

    def test_affMat(self):
        """Test le fonctionnement de la fonction 'vect.initMat'."""
        vectaffMat = Vector.initMat(5,0)
        self.assertEqual(Vector.affMat(vectaffMat), print("[0, 0, 0, 0, 0]\n[0, 0, 0, 0, 0]\n[0, 0, 0, 0, 0]\n[0, 0, 0, 0, 0]\n[0, 0, 0, 0, 0]"))
