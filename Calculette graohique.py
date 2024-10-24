from tkiteasy import *

largeur = 800
longueur = 700

class Calculette:

    def __init__(self):
        self.g = ouvrirFenetre(longueur, largeur)
        self.g.attendreClic()

        #def initGraphique(self):
        self.g.afficherTexte("1",jhg)


c = Calculette()