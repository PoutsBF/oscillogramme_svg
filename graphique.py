# -*- coding: utf-8 -*-
#! python3

"""
écran de 800 x 600
graduation haute (4 pts / 3 pts) 
graduation basse (4 pts / 3 pts)
graduation centre (6 pts / 4 pts)
points horizontaux

<svg width="800" height="600" xmlns="http://www.w3.org/2000/svg" xmlns:svg="http://www.w3.org/2000/svg">
 <!-- Created with SVG-edit - https://github.com/SVG-Edit/svgedit-->
 <title>oscillogramme</title>
 <g class="layer">
  <title>Layer 1</title>
  <line fill="none" id="svg_1" stroke="#000000" x1="1" x2="640" y1="240" y2="240"/>
 </g>
</svg>
"""
import xml.etree.ElementTree as cfg

largeur = 800
hauteur = 320

dessin = cfg.Element('svg')
dessin.set("width", f"{largeur + 15}")
dessin.set("height", f"{hauteur + 15}")
dessin.set("xmlns", "http://www.w3.org/2000/svg")
dessin.set("xmlns:svg", "http://www.w3.org/2000/svg")
dessin.text = "<!-- Created by Stéphane Lepoutère-->"

titre = cfg.SubElement(dessin, "title")
titre.text = "oscillogramme"

grille = cfg.SubElement(dessin, "g")
grille.set("class", "layer")
grille.set("id", "grille")
grille.set("transform", f"translate(15, 0)")


titre = cfg.SubElement(grille, "title")
titre.text = "grille"
#   <rect fill="#000000" height="342" id="svg_131" stroke="#000000" width="363" x="75" y="88"/>
fond = cfg.SubElement(grille, "rect") ; fond.set("fill", "#000000") ; fond.set("stroke", "#000000")
fond.set("x", "0") ; fond.set("y", "0") ; fond.set("width", f"{largeur}") ; fond.set("height", f"{hauteur}") ; 


# text = cfg.tostring(dessin, encoding='utf-8')

distance_x = largeur / 10
distance_s_x = distance_x / 5

distance_y = hauteur / 8
distance_s_y = distance_y / 5

for i in range(0,10):
    for j in range(0,4):
        x = int(((j * distance_s_x) + distance_s_x) + (i * distance_x))
        # haut : 
        ligne = cfg.SubElement(grille, "line") ; ligne.set("fill", "none") ; ligne.set("stroke", "#ffffff")
        ligne.set("x1", f"{x}") ; ligne.set("y1", "0") ; ligne.set("x2", f"{x}") ; ligne.set("y2", "2") ; 

        # millieu
        ligne = cfg.SubElement(grille, "line") ; ligne.set("fill", "none") ; ligne.set("stroke", "#ffffff")
        ligne.set("x1", f"{x}") ; ligne.set("y1", f"{int(hauteur/2) - 1}") ; ligne.set("x2", f"{x}") ; ligne.set("y2", f"{int(hauteur/2) + 2}") ; 

        # bas
        ligne = cfg.SubElement(grille, "line") ; ligne.set("fill", "none") ; ligne.set("stroke", "#ffffff")
        ligne.set("x1", f"{x}") ; ligne.set("y1", f"{hauteur - 2}") ; ligne.set("x2", f"{x}") ; ligne.set("y2", f"{hauteur}") ; 

        ## points verticaux
        for k in range(0, 8) :
            if (k != 4) :
                y = int(k * distance_y)
                # points
                ligne = cfg.SubElement(grille, "line") ; ligne.set("fill", "none") ; ligne.set("stroke", "#ffffff")
                ligne.set("x1", f"{x}") ; ligne.set("y1", f"{y}") ; ligne.set("x2", f"{x}") ; ligne.set("y2", f"{y+1}") ; 


for i in range(0,9):
    x = int((i * distance_x) + distance_x)
    # haut : 
    ligne = cfg.SubElement(grille, "line") ; ligne.set("fill", "none") ; ligne.set("stroke", "#ffffff")
    ligne.set("x1", f"{x}") ; ligne.set("y1", "0") ; ligne.set("x2", f"{x}") ; ligne.set("y2", "4") ; 

    if(i != 4) :
        # millieu
        ligne = cfg.SubElement(grille, "line") ; ligne.set("fill", "none") ; ligne.set("stroke", "#ffffff")
        ligne.set("x1", f"{x}") ; ligne.set("y1", f"{int(hauteur/2) - 3}") ; ligne.set("x2", f"{x}") ; ligne.set("y2", f"{int(hauteur/2) + 4}")

    # bas
    ligne = cfg.SubElement(grille, "line") ; ligne.set("fill", "none") ; ligne.set("stroke", "#ffffff")
    ligne.set("x1", f"{x}") ; ligne.set("y1", f"{hauteur - 4}") ; ligne.set("x2", f"{x}") ; ligne.set("y2", f"{hauteur}") ; 

    if(i != 4) :
        for k in range(0, 38) :
            y = int((k * distance_s_y) + distance_s_y)
            # points
            if(k != 19):
                ligne = cfg.SubElement(grille, "line") ; ligne.set("fill", "none") ; ligne.set("stroke", "#ffffff")
                ligne.set("x1", f"{x}") ; ligne.set("y1", f"{y}") ; ligne.set("x2", f"{x}") ; ligne.set("y2", f"{y+1}") ; 
    else:
        y = int(hauteur / 2)
        ligne = cfg.SubElement(grille, "line") ; ligne.set("fill", "none") ; ligne.set("stroke", "#ffffff")
        ligne.set("x1", f"{x}") ; ligne.set("y1", f"{y}") ; ligne.set("x2", f"{x}") ; ligne.set("y2", f"{y+1}") ; 


for k in range(0, 8) :
    # grands traits
    if(k != 7) :
        y = int (k * distance_y) + distance_y
        ligne = cfg.SubElement(grille, "line") ; ligne.set("fill", "none") ; ligne.set("stroke", "#ffffff")
        ligne.set("x1", "0") ; ligne.set("y1", f"{y}") ; ligne.set("x2", "4") ; ligne.set("y2", f"{y}") ; 
        ligne = cfg.SubElement(grille, "line") ; ligne.set("fill", "none") ; ligne.set("stroke", "#ffffff")
        ligne.set("x1", f"{largeur}") ; ligne.set("y1", f"{y}") ; ligne.set("x2", f"{largeur - 4}") ; ligne.set("y2", f"{y}") ; 
        if(k != 3) :
            ligne = cfg.SubElement(grille, "line") ; ligne.set("fill", "none") ; ligne.set("stroke", "#ffffff")
            ligne.set("x1", f"{int((largeur / 2) -2)}") ; ligne.set("y1", f"{y}") ; ligne.set("x2", f"{(largeur / 2) + 2}") ; ligne.set("y2", f"{y}") ; 

    # petits traits
    for l in range(0,4) : 
        y = int(((l * distance_s_y) + distance_s_y) + (k * distance_y))
        # haut
        ligne = cfg.SubElement(grille, "line") ; ligne.set("fill", "none") ; ligne.set("stroke", "#ffffff")
        ligne.set("x1", f"0") ; ligne.set("y1", f"{y}") ; ligne.set("x2", "2") ; ligne.set("y2", f"{y}") ; 
        # milieu
        ligne = cfg.SubElement(grille, "line") ; ligne.set("fill", "none") ; ligne.set("stroke", "#ffffff")
        ligne.set("x1", f"{int((largeur / 2) -1)}") ; ligne.set("y1", f"{y}") ; ligne.set("x2", f"{(largeur / 2) + 1}") ; ligne.set("y2", f"{y}") ; 
        # bas
        ligne = cfg.SubElement(grille, "line") ; ligne.set("fill", "none") ; ligne.set("stroke", "#ffffff")
        ligne.set("x1", f"{largeur - 2}") ; ligne.set("y1", f"{y}") ; ligne.set("x2", f"{largeur}") ; ligne.set("y2", f"{y}") ; 

pointeur_CH1 = cfg.SubElement(dessin, "g")
pointeur_CH1.set("transform", f"translate(0, {int(hauteur * 2 / 8)})")
pointe_CH1 = cfg.SubElement(pointeur_CH1, "path")
pointe_CH1.set("d", "m0,0l15,-0l10,10l-10,10l-15,0l0,-15z")
pointe_CH1.set("fill", "#ffff00") ; pointe_CH1.set("id", "svg_852") ; pointe_CH1.set("stroke", "#ffffff") 
texte_CH1 = cfg.SubElement(pointeur_CH1, "text")
texte_CH1.set("fill", "#000000") ; texte_CH1.set("font-family", "Sans-serif") ; texte_CH1.set("font-size", "10px") ; texte_CH1.set("stroke", "#ffffff")
texte_CH1.set("stroke-width", "0") ; texte_CH1.set("text-anchor", "start") ; texte_CH1.set("x", "2") ; texte_CH1.set("y", "13.5") ; texte_CH1.set("xml:space", "preserve") ; 
texte_CH1.text = "CH1"
# Pointe :
"""<g id="svg_854">
   <path d="m160,110l16,-0l10,10l-10,10l-15,0l0,-15z" fill="#ffff00" id="svg_852" stroke="#ffffff"/>
   <text fill="#000000" font-family="Sans-serif" font-size="9" id="svg_853" stroke="#ffffff" stroke-width="0" text-anchor="start"  xml:space="preserve" y="123.75">CH1</text>
  </g>
"""

sortie = cfg.ElementTree(dessin)
with open ("dessin.svg", "wb") as files :
    sortie.write(files)

print ("fin")