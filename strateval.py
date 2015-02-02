# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 16:22:22 2015

@author: 3300200
"""

import random
from soccersimulator import pyglet
from soccersimulator import Vector2D
from soccersimulator import SoccerAction
from soccersimulator import SoccerBall
from soccersimulator import SoccerStrategy
from soccersimulator import SoccerTeam
from soccersimulator import SoccerPlayer
from soccersimulator import SoccerBattle,PygletObserver,ConsoleListener,LogListener

'''
Stratégie Vide
Le joueur ne fait rien
'''

class VideS(SoccerStrategy):
    def __init__(self):
        pass
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        return SoccerAction()
    def copy(self):
        return VideS()
    def create_strategy(self):
        return VideS()

'''
Stratégie de mouvement
Le joueur se déplacera vers le point indiqué
'''

class AllerVersBallon(SoccerStrategy):
    def __init__(self):
        pass
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        mouvement = state.ball.position - player.position
        return SoccerAction(vitesse)
    def copy(self):
        return AllerVersBallon()
    def create_strategy(self):
        return AllerVersBallon()
        
        
'''Fenêtre de test de partie'''

team1=SoccerTeam("team1")
team2=SoccerTeam("team2")
team1.add_player(SoccerPlayer("t1j1",AllerVersBallon()))
team2.add_player(SoccerPlayer("t2j1",VideS()))
battle=SoccerBattle(team1,team2)
obs=PygletObserver()
obs.set_soccer_battle(battle)
pyglet.app.run()