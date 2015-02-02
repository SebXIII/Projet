# coding=utf-8
from soccersimulator import Vector2D, SoccerBattle, SoccerPlayer, SoccerTeam, SoccerAction, SoccerStrategy
from soccersimulator import PygletObserver,ConsoleListener,LogListener
from soccersimulator import PLAYER_RADIUS, BALL_RADIUS
import outils
import random

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
        mouvement = self.loc - player.position
        return SoccerAction(mouvement)
    def copy(self):
        return AllerVersLoc()
    def create_strategy(self):
        return AllerVersLoc()
        
        
'''
Stratégie de mouvement
Le joueur se déplacera vers le point indiqué
'''

class AllerVersBallon(SoccerStrategy):
    def __init__(self):
        self.strat= AllerVersLoc(Vector2D())
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        self.strat.loc= state.ball.position
        #mouvement = state.ball.position - player.position
        return self.strat.compute_strategy(state,player,teamid)
    def copy(self):
        return AllerVersBallon()
    def create_strategy(self):
        return AllerVersBallon()

"""
Stratégie de mouvement
Le joueur se place entre le ballon et son but
"""

class AllerButBallon(SoccerStrategy):
    def __init__(self):
        self.strat= AllerVersLoc(Vector2D())
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        self.strat.loc = state.ball.position + state.get_goal_center(teamid)
        self.strat.loc.product = self.strat.loc.product(0.5)
        #mouvement = state.ball.position - player.position
        return self.strat.compute_strategy(state,player,teamid)
    def copy(self):
        return AllerButBallon()
    def create_strategy(self):
        return AllerButBallon()

"""
Stratégie de tir
Le joueur frappe le ballon en face de lui dans un angle aléatoire
"""
class Degagement(SoccerStrategy):
    def __init__(self):
        pass
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        tir = Vector2D.create_polar(player.angle + random()*4-2, 1)
        return SoccerAction(Vector2D(0,0), tir)
    def copy(self):
        return Degagement()
    def create_strategy(self):
        return Degagement()



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
        tir = state.get_goal_center(outils.IDTeamOp(teamid)) - player.position
        return SoccerAction(Vector2D(0,0), tir)
    def copy(self):
        return Tir()
    def create_strategy(self):
        return Tir()
   
"""
Fusionne deux starts, une de tir et une de mouvement
"""
class CompoStrat(SoccerStrategy):
    def __init__(self, strat1, strat2):
        self.s1 = strat1
        self.s2 = strat2
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        move = self.s1.compute_strategy(state, player, teamid)
        shot = self.s2.compute_strategy(state, player, teamid)
        return SoccerAction(move.acceleration, shot.shoot)
    def copy(self):
        return CompoStrat()
    def create_strategy(self):
        return CompoStrat()
"""
Stratégie fonceur
Utilise stratégie AllerVersBallon
"""

class Fonceur(SoccerStrategy):
    def __init__(self):
        self.fonceur = CompoStrat(AllerVersBallon(), Tir())
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        return self.fonceur.compute_strategy(state,player,teamid)
    def copy(self):
        return Fonceur()
    def create_strategy(self):
        return Fonceur()


"""
Stratégie défenseur
Se place entre le ballon et le but et dégage le ballon
"""

class Defenseur(SoccerStrategy):
    def __init__(self):
        self.defense = CompoStrat(AllerButBallon(), Degagement())
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        return self.defense.compute_strategy(state,player,teamid)
    def copy(self):
        return Defenseur()
    def create_strategy(self):
        return Defenseur()