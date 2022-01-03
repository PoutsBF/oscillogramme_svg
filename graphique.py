# -*- coding: utf-8 -*-
#! python3

"""
Stéphane Lepoutère  / décembre 2021
objectif : automatiser la création d'oscillogrammes pour les procédures de 
    test électroniques.

écran de 800 x 600
graduation haute (4 pts / 3 pts) 
graduation basse (4 pts / 3 pts)
graduation centre (6 pts / 4 pts)
points horizontaux
"""
import xml.etree.ElementTree as cfg
from grille import grille, legende, pointeur

largeur = 800
hauteur = 320
pos_grille_x = 25
pos_grille_y = 0

dessin = cfg.Element('svg')
dessin.set("width", f"{largeur + 30}")
dessin.set("height", f"{hauteur + 25}")
dessin.set("xmlns", "http://www.w3.org/2000/svg")
dessin.set("xmlns:svg", "http://www.w3.org/2000/svg")
dessin.text = "<!-- Created by Stéphane Lepoutère-->"

titre = cfg.SubElement(dessin, "title")
titre.text = "oscillogramme"

dessin.append(grille(largeur, hauteur, pos_grille_x, pos_grille_y))

# Pointe :
dessin.append(pointeur(int(hauteur * 2 / 8), "#ffff00", 1))
dessin.append(pointeur(int(hauteur * 5 / 8), "#ff00ff", 2))
dessin.append(legende(largeur / 2, hauteur + 1, CH1="5V"))

"""
    Fin : sortie sous forme de fichier et de texte
"""
sortie = cfg.ElementTree(dessin)
with open ("dessin.svg", "wb") as files :
    sortie.write(files)

text = cfg.tostring(dessin, encoding='utf-8')
print (text)
print ("fin")