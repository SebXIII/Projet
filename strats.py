# coding=utf-8
from soccersimulator import Vector2D, SoccerBattle, SoccerPlayer, SoccerTeam, SoccerAction, SoccerStrategy
from soccersimulator import PygletObserver,ConsoleListener,LogListener
from soccersimulator import PLAYER_RADIUS, BALL_RADIUS

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
        return SoccerAction(mouvement)
    def copy(self):
        return AllerVersBallon()
    def create_strategy(self):
        return AllerVersBallon()

"""
Stratégie de frappe
Le joueur tire vers le but
"""     
        
        
class Tir(SoccerStrategy):
    def __init__(self):
        pass
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        tir = state.get_goal_center(self.get_op(teamid)) - player.position
        return SoccerAction(mouvement)
    def copy(self):
        return Tir()
    def create_strategy(self):
        return Tir()



