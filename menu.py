#-*-coding:Utf-8 -*

#    TheSecretTower
#    Copyright (C) 2011 Pierre SURPLY
#
#    This file is part of TheSecretTower.
#
#    TheSecretTower is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    TheSecretTower is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with TheSecretTower.  If not, see <http://www.gnu.org/licenses/>.

# Auteur : Pierre Surply

import pygame
from pygame.locals import *

import app
import element
import const
import event

from time import *


def menu(app, ptitle, pmenu):

    input = event.Input()

    fond_menu = element.Element()
    fond_menu.changer_image(pygame.image.load(const.path_fond_menu).convert())

    img_choix = element.Element()
    img_choix.changer_image(pygame.image.load(const.path_choix).convert_alpha())
    img_choix.x = 30
    img_choix.y = 300

    pointeur = element.Element()
    pointeur.changer_image(pygame.image.load("img/pointeur.png").convert_alpha())


    w_title = element.Element()
    w_title.changer_text(ptitle, app.font, (255,255,255))
    w_title.move_el(84,254)
    title = element.Element()
    title.changer_text(ptitle, app.font)
    title.move_el(80,250)
    
    menu = []
    w_menu = []

    for i in pmenu:
        # White
        entry = element.Element()
        entry.changer_text(i, app.font, (255,255,255))
        w_menu.append(entry)
        # Black
        entry = element.Element()
        entry.changer_text(i, app.font)
        menu.append(entry)


    cmd = 1

    while input.update_event(app):
        # Evenement
        pointeur.move_el(-pointeur.x+input.mouse[0], -pointeur.y+input.mouse[1])
        for i in range(1,1+len(menu)):
            if input.mouse[1] > 250+(i*50) and input.mouse[1] < 300+(i*50):
                cmd = i
                img_choix.y= 250+(cmd*50)
        if input.key[K_SPACE] or input.key[K_RETURN] or input.mousebuttons[1]:
            if pmenu[cmd-1] == "Quit":
                return 0
            return cmd
        
        # Affichage
        app.blit(fond_menu)
        app.blit(w_title)
        app.blit(title)

        x = 104
        y = 304
        for entry in w_menu:
            entry.x = x
            entry.y = y
            app.blit(entry)
            y = y + 50
                
        x = 100
        y = 300
        for entry in menu:
            entry.x = x
            entry.y = y
            app.blit(entry)
            y = y + 50
        
        app.blit(img_choix)
        app.blit(pointeur)
            
        app.flip()

    return 0

def ask(app, ptitle):
    
    input = event.Input()

    fond_menu = element.Element()
    fond_menu.changer_image(pygame.image.load(const.path_fond_menu).convert())

    w_title = element.Element()
    w_title.changer_text(ptitle, app.font, (255,255,255))
    w_title.move_el(84,254)
    title = element.Element()
    title.changer_text(ptitle, app.font)
    title.move_el(80,250)

    preponse = ""
    w_reponse = element.Element()
    w_reponse.changer_text(preponse, app.font, (255,255,255))
    w_reponse.move_el(104, 304)
    reponse = element.Element()
    reponse.changer_text(preponse, app.font)
    reponse.move_el(100, 300)

    while 1:
        preponse = input.write(preponse)
        input.update_event(app)

        if input.key[K_RETURN]:
            if preponse != "":
                return preponse

        w_reponse.changer_text(preponse, app.font, (255,255,255))
        reponse.changer_text(preponse, app.font)
        app.blit(fond_menu)
        app.blit(w_title)
        app.blit(title)
        app.blit(w_reponse)
        app.blit(reponse)

        app.flip()
