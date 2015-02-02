# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 16:22:22 2015

@author: 3300200
"""

import random
import outils
from soccersimulator import pyglet
from soccersimulator import Vector2D
from soccersimulator import SoccerAction
from soccersimulator import SoccerBall
from soccersimulator import SoccerStrategy
from soccersimulator import SoccerTeam
from soccersimulator import SoccerPlayer
from soccersimulator import SoccerBattle,PygletObserver,ConsoleListener,LogListener

'''
Stratégie de mouvement
Se déplace vers un point indiqué
'''
class AllerVersLoc(SoccerStrategy):
    def __init__(self, localisation):
        self.loc = localisation        
        pass
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        mouvement = loc - player.position
        return SoccerAction(mouvement)
    def copy(self):
        return AllerVersLoc()
    def create_strategy(self):
        return AllerVersLoc()

        
'''Fenêtre de test de partie'''

team1=SoccerTeam("team1")
team2=SoccerTeam("team2")
team1.add_player(SoccerPlayer("t1j1",AllerVersLoc(Vector2D(0,0))))
team2.add_player(SoccerPlayer("t2j1",AllerVersLoc(Vector2D(5,20))))
battle=SoccerBattle(team1,team2)
obs=PygletObserver()
obs.set_soccer_battle(battle)
pyglet.app.run()