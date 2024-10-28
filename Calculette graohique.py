from tkiteasy import *

largeur = 700
longueur = 550

class Calculette:

    def __init__(self):
        self.g = ouvrirFenetre(longueur, largeur)
        self.initGraphique()
        self.calcul()


    def initGraphique(self):
        #Ligne séparant calculette et résultat
        self.g.dessinerLigne(0,120,550,120,"white",4)

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
        AC = self.g.afficherTexte("AC", 50, 640, "orange", 40)
        zéro = self.g.afficherTexte("0", 200, 640, "white", 40)
        point = self.g.afficherTexte(",", 350, 640, "white", 40)
        egal = self.g.afficherTexte("=", 500, 640, "orange", 40)

    def calcul(self):
        self.chiffres = []
        val1 = ''
        resultat =''
        val = self.g.afficherTexte(val1, 100, 75, "white", 30)
        result = self.g.afficherTexte(resultat, 450, 75, "white", 30)
        clic = False  # Boucle qui nous permet de faire tourner le programme a l'infini
        while not clic:
            click = self.g.attendreClic()

            # Ligne 1 (Fonctions)
            if 460 < click.x < 540 and 120 < click.y < 200:
                operateur = '/'
                self.chiffres.append(str(operateur))
                self.g.changerTexte(val, val1 + operateur)
                val1 += str(operateur)


            # Ligne 2 (7, 8, 9, x)


            if 10 < click.x < 90 and 240 < click.y < 320:
                chiffre = 7
                self.chiffres.append(str(chiffre))
                self.g.changerTexte(val, val1 + str(chiffre))
                val1 += str(chiffre)

            if 160 < click.x < 240 and 240 < click.y < 320:
                chiffre = 8
                self.chiffres.append(str(chiffre))
                self.g.changerTexte(val, val1 + str(chiffre))
                val1 += str(chiffre)
            if 310 < click.x < 390 and 240 < click.y< 320:
                chiffre = 9
                self.chiffres.append(str(chiffre))
                self.g.changerTexte(val, val1 + str(chiffre))
                val1 += str(chiffre)

            if 460 < click.x < 540 and 240 < click.y < 320:
                operateur = 'x'
                self.chiffres.append('*')
                self.g.changerTexte(val, val1 + operateur)
                val1 += str(operateur)

            # Ligne 3 (4, 5, 6, -)
            if 10 < click.x < 90 and 360 < click.y < 440:
                chiffre = 4
                self.chiffres.append(str(chiffre))
                self.g.changerTexte(val, val1 + str(chiffre))
                val1 += str(chiffre)

            if 160 < click.x < 240 and 360 < click.y < 440:
                chiffre = 5
                self.chiffres.append(str(chiffre))
                self.g.changerTexte(val, val1 + str(chiffre))
                val1 += str(chiffre)

            if 310 < click.x < 390 and 360 < click.y < 440:
                chiffre = 6
                self.chiffres.append(str(chiffre))
                self.g.changerTexte(val, val1 + str(chiffre))
                val1 += str(chiffre)
            if 460 < click.x < 540 and 360 < click.y < 440:
                operateur = '-'
                self.chiffres.append(str(operateur))
                self.g.changerTexte(val, val1 + operateur)
                val1 += str(operateur)

            # Ligne 4 (1, 2, 3, +)
            if 10 < click.x < 90 and 480 < click.y < 560:
                chiffre = 1
                self.chiffres.append(str(chiffre))
                self.g.changerTexte(val, val1 + str(chiffre))
                val1 += str(chiffre)
            if 160 < click.x < 240 and 480 < click.y < 560:
                chiffre = 2
                self.chiffres.append(str(chiffre))
                self.g.changerTexte(val, val1 + str(chiffre))
                val1 += str(chiffre)
            if 310 < click.x < 390 and 480 < click.y < 560:
                chiffre = 3
                self.chiffres.append(str(chiffre))
                self.g.changerTexte(val, val1 + str(chiffre))
                val1 += str(chiffre)
            if 460 < click.x < 540 and 480 < click.y < 560:
                operateur = '+'
                self.chiffres.append(str(operateur))
                self.g.changerTexte(val, val1 + str(operateur))
                val1 += str(operateur)

            # Ligne 5 (0, ., =)
            if 10 < click.x < 90 and 600 < click.y < 680:
                fonction = 'AC'
                self.chiffres = []
                self.g.changerTexte(val, '')
                self.g.changerTexte(result,'')
                val1 = ''
                resultat = ''

            if 160 < click.x < 240 and 600 < click.y < 680:
                chiffre = 0
                self.chiffres.append(str(chiffre))
                self.g.changerTexte(val, val1 + str(chiffre))
                val1 += str(chiffre)

            if 310 < click.x < 390 and 600 < click.y < 680:
                fonction = '.'
                self.chiffres.append(str(fonction))
                self.g.changerTexte(val, val1 + str(fonction))
                val1 += str(fonction)
            if 460 < click.x < 540 and 600 < click.y < 680:
                operateur = '='
                self.g.changerTexte(result, str(self.operation()))
                resultat = str(self.operation())
                val1 = ''
                self.chiffres =[]
                self.chiffres.append(resultat)





    def operation(self):
        calc = ''.join(self.chiffres).replace('=', '')
        print(self.chiffres)
        res = eval(calc)
        return res






c = Calculette()

