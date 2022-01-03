# -*- coding: utf-8 -*-
#! python3

"""
fonction renvoyant une grille complète
"""

import xml.etree.ElementTree as cfg

def grille(largeur, hauteur, pos_x, pos_y) :
    # Crée l'élément englobant 
    grille = cfg.Element('g')

    # ligne suivante : utilisé lorsque tout le programme était en 1 bloc
#    grille = cfg.SubElement(dessin, "g")
    # attributs : class="layer", id="grille", transorm="..."
    grille.set("class", "layer")                    
    grille.set("id", "grille")
    grille.set("transform", f"translate({pos_x}, {pos_y})")


    # crée un sous élément "titre", avec un contenu texte "grille"
    titre = cfg.SubElement(grille, "title")
    titre.text = "grille"

    # Dessine le rectangle du fond en noir
    fond = cfg.SubElement(grille, "rect") ; fond.set("fill", "#000000") ; fond.set("stroke", "#000000")
    fond.set("x", "0") ; fond.set("y", "0") ; fond.set("width", f"{largeur}") ; fond.set("height", f"{hauteur}") ; 


    # Calcule les positions principales et secondaires pour les traits et points
    distance_x = largeur / 10
    distance_s_x = distance_x / 5

    distance_y = hauteur / 8
    distance_s_y = distance_y / 5

    # Grille horizontale 
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

    # Points trame
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


    # traits verticaux
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


    return grille

def pointeur(pos_y, couleur, canal) :
#    pointeur_CH = cfg.SubElement(dessin, "g")
    pointeur_CH = cfg.Element('g')
    pointeur_CH.set("transform", f"translate(0, {pos_y})")
    pointeur_CH.set("id", f"CH{canal}")

    pointe_CH = cfg.SubElement(pointeur_CH, "path")
    pointe_CH.set("d", "m0,0l15,-0l10,10l-10,10l-15,0l0,-15z")
    pointe_CH.set("fill", f"{couleur}") ; pointe_CH.set("id", "svg_852") ; pointe_CH.set("stroke", "#ffffff") 

    texte_CH = cfg.SubElement(pointeur_CH, "text")
    texte_CH.set("fill", "#000000") ; texte_CH.set("font-family", "Sans-serif") ; texte_CH.set("font-size", "10px") ; texte_CH.set("stroke", "#ffffff")
    texte_CH.set("stroke-width", "0") ; texte_CH.set("text-anchor", "start") ; texte_CH.set("x", "2") ; texte_CH.set("y", "13.5") ; texte_CH.set("xml:space", "preserve") ; 
    texte_CH.text = f"CH{canal}"

    """<g id="svg_854">
    <path d='m160,110l16,-0l10,10l-10,10l-15,0l0,-15z' fill="#ffff00" id="svg_852" stroke="#ffffff"/>
    <text fill="#000000" font-family="Sans-serif" font-size="9" id="svg_853" stroke="#ffffff" stroke-width="0" text-anchor="start"  xml:space="preserve" y="123.75">CH</text>
    </g>
    """
    return pointeur_CH

def legende(x, y, label) : 
#    legende = cfg.SubElement(dessin, "g")
    legende = cfg.Element()
    legende.set("id", "legende")
    legende.set("transform", f"translate({x}, {y})")

    rectangle_legende = cfg.SubElement(legende, "rect")
    rectangle_legende.set("x", "0") ; rectangle_legende.set("y", "0")
    rectangle_legende.set("width", f"{x}") ; 
    rectangle_legende.set("height", "20")
    rectangle_legende.set("rx", "5") ; rectangle_legende.set("ry", "5")

    texte_legende = cfg.SubElement(legende, "text")
    texte_legende.set("fill", "#ffffff") ; texte_legende.set("font-family", "Sans-serif") ; texte_legende.set("font-size", "8px") ; texte_legende.set("stroke", "#ffffff")
    texte_legende.set("stroke-width", "0") ; texte_legende.set("text-anchor", "start") ; texte_legende.set("x", "5") ; texte_legende.set("y", "13") ; texte_legende.set("xml:space", "preserve") ; 
    texte_legende.text = f"CH{1} : 5V / div"

    return legende