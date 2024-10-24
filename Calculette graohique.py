from tkiteasy import *

largeur = 800
longueur = 700

class Calculette:

    def __init__(self):
        self.g = ouvrirFenetre(longueur, largeur)
        self.initGraphique()
    def initGraphique(self):
        un = self.g.afficherTexte("1",20,400,"white",40)
        deux = self.g.afficherTexte("2",100,400,"white",40)
        trois = self.g.afficherTexte("3",180,400,"white",40)
        quatre = self.g.afficherTexte("4",20,480,"white",40)
        cinq = self.g.afficherTexte("5",100,480,"white",40)
        six = self.g.afficherTexte("6",180,480,"white",40)
        sept = self.g.afficherTexte("7",20,560,"white",40)
        huit = self.g.afficherTexte("8",100,560,"white",40)
        neuf = self.g.afficherTexte("9",180,560,"white",40)
        zéro = self.g.afficherTexte("0",100,640,"white",40)
        plus = self
        self.g.attendreClic()

c = Calculette()