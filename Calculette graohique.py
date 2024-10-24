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
        plus = self.g.afficherTexte("+",260,400,"white",40)
        moins = self.g.afficherTexte("-",260,460,"white",40)
        fois = self.g.afficherTexte("x",260,520,"white",40)
        diviser = self.g.afficherTexte("%",260,580,"white",40)
        egal = self.g.afficherTexte("=",260,640,"white",40)
        self.g.attendreClic()

c = Calculette()