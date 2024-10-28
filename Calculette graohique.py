from tkiteasy import *

largeur = 700
longueur = 550

class Calculette:

    def __init__(self):
        self.g = ouvrirFenetre(longueur, largeur)
        self.initGraphique()
        self.calcul()
        self.val1 = 0
        self.val2 = 0
        self.aff = 0

    def initGraphique(self):
        # Ligne 1 (Fonctions)
        diviser = self.g.afficherTexte("/", 500, 160, "orange", 40)

        # Ligne 2 (7, 8, 9, x)
        sept = self.g.afficherTexte("7", 50, 280, "white", 40)
        huit = self.g.afficherTexte("8", 200, 280, "white", 40)
        neuf = self.g.afficherTexte("9", 350, 280, "white", 40)
        fois = self.g.afficherTexte("x", 500, 280, "orange", 40)

        # Ligne 3 (4, 5, 6, -)
        quatre = self.g.afficherTexte("4", 50, 400, "white", 40)
        cinq = self.g.afficherTexte("5", 200, 400, "white", 40)
        six = self.g.afficherTexte("6", 350, 400, "white", 40)
        moins = self.g.afficherTexte("-", 500, 400, "orange", 40)

        # Ligne 4 (1, 2, 3, +)
        un = self.g.afficherTexte("1", 50, 520, "white", 40)
        deux = self.g.afficherTexte("2", 200, 520, "white", 40)
        trois = self.g.afficherTexte("3", 350, 520, "white", 40)
        plus = self.g.afficherTexte("+", 500, 520, "orange", 40)

        # Ligne 5 (0, ., =)
        AC = self.g.afficherTexte("AC", 50, 640, "white", 40)
        zéro = self.g.afficherTexte("0", 200, 640, "white", 40)
        point = self.g.afficherTexte(".", 350, 640, "white", 40)
        egal = self.g.afficherTexte("=", 500, 640, "orange", 40)
        self.resultat = self.g.afficherTexte("",100,280,"white",30)
        self.g.attendreClic()

    def calcul(self):
        val1 = ''
        self.g.afficherTexte(val1, 20, 40, "white", 20)
        clic = False  # Boucle qui nous permet de faire tourner le programme a l'infini
        while clic != True:
            self.chiffres = []
            click = self.g.attendreClic()

            # Ligne 1 (Fonctions)
            if 480 < click.x < 520 and 140 < click.y < 180:
                operateur = "/"
                self.chiffres.append(str(operateur))
                self.g.changerTexte(val1, val1 + str(operateur))
                val1 += str(operateur)


            # Ligne 2 (7, 8, 9, x)
            if 30 < click.x < 70 and 110 < click.y < 150:
                chiffre = 7
                self.chiffres.append(str(chiffre))
                self.g.changerTexte(val1, val1 + str(chiffre))
                val1 += str(chiffre)
            if 200 < click.x < 280 and 280 < click.y < 360:
                chiffre = 8
                self.chiffres.append(str(chiffre))
                self.g.changerTexte(val1, val1 + str(chiffre))
                val1 += str(chiffre)
            if 350 < click.x < 430 and 280 < click.y < 360:
                chiffre = 9
                self.chiffres.append(str(chiffre))
                self.g.changerTexte(val1, val1 + str(chiffre))
                val1 += str(chiffre)
            if 500 < click.x < 580 and 280 < click.y < 360:
                operateur = "x"
                self.chiffres.append(str(operateur))
                self.g.changerTexte(val1, val1 + str(operateur))
                val1 += str(operateur)

            # Ligne 3 (4, 5, 6, -)
            if 50 < click.x < 130 and 400 < click.y < 480:
                chiffre = 4
                self.chiffres.append(str(chiffre))
                self.g.changerTexte(val1, val1 + str(chiffre))
                val1 += str(chiffre)
            if 200 < click.x < 280 and 400 < click.y < 480:
                chiffre = 5
                self.chiffres.append(str(chiffre))
                val1 += str(chiffre)
                self.g.afficherTexte(val1, 20, 40, "white", 10)
            if 350 < click.x < 430 and 400 < click.y < 480:
                chiffre = 6
                self.chiffres.append(str(chiffre))
                self.g.changerTexte(val1, val1 + str(chiffre))
                val1 += str(chiffre)
            if 500 < click.x < 580 and 400 < click.y < 480:
                operateur = "-"
                self.chiffres.append(str(operateur))
                self.g.changerTexte(val1, val1 + str(operateur))
                val1 += str(operateur)

            # Ligne 4 (1, 2, 3, +)
            if 50 < click.x < 130 and 520 < click.y < 600:
                chiffre = 1
                self.chiffres.append(str(chiffre))
                self.g.changerTexte(val1, val1 + str(chiffre))
                val1 += str(chiffre)
            if 200 < click.x < 280 and 520 < click.y < 600:
                chiffre = 2
                self.chiffres.append(str(chiffre))
                self.g.changerTexte(val1, val1 + str(chiffre))
                val1 += str(chiffre)
            if 350 < click.x < 430 and 520 < click.y < 600:
                chiffre = 3
                self.chiffres.append(str(chiffre))
                self.g.changerTexte(val1, val1 + str(chiffre))
                val1 += str(chiffre)
            if 500 < click.x < 580 and 520 < click.y < 600:
                operateur = "+"
                self.chiffres.append(str(operateur))
                self.g.changerTexte(val1, val1 + str(operateur))
                val1 += str(operateur)

            # Ligne 5 (0, ., =)
            if 50 < click.x < 130 and 640 < click.y < 720:
                fonction = "AC"
                self.chiffres = []
                self.g.changerTexte(val1, '')

            if 200 < click.x < 280 and 640 < click.y < 720:
                chiffre = 0
                self.chiffres.append(str(chiffre))
                self.g.changerTexte(val1, val1 + str(chiffre))
                val1 += str(chiffre)
            if 350 < click.x < 430 and 640 < click.y < 720:
                fonction = "."
                self.chiffres.append(str(fonction))
                self.g.changerTexte(val1, val1 + str(fonction))
                val1 += str(fonction)
            if 500 < click.x < 580 and 640 < click.y < 720:
                operateur = "="
                self.operation()



    def operation(self):
        return None






c = Calculette()