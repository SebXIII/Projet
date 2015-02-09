# coding=utf-8
from soccersimulator import Vector2D, SoccerBattle, SoccerPlayer, SoccerTeam, SoccerAction, SoccerStrategy
from soccersimulator import PygletObserver,ConsoleListener,LogListener
from soccersimulator import PLAYER_RADIUS, BALL_RADIUS
import outils
import random
import pdb

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
        tir = Vector2D.create_polar(player.angle + random.random()*2-1, 1)
        return SoccerAction(Vector2D(0,0), tir)
    def create_strategy(self):
        return Degagement()


"""
Stratégie de tir
Le joueur dribble de façon imprévisible
"""  
class Dribble(SoccerStrategy):
    def __init__(self):
        pass
    def start_battle(self,state):
        elf.strat.locpass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
            dri = state.get_goal_center(outils.IDTeamOp(teamid)) - player.position
            drib = Vector2D.create_polar(dri.angle + random.random()*2-1,1)
            return SoccerAction(Vector2D(0,0), drib)
    def create_strategy(self):
        return Dribble()


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
    def create_strategy(self):
        return CompoStrat()
"""
Stratégie fonceurVideS
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
    def create_strategy(self):
        return Fonceur()


"""
Stratégie défenseur
Se place entre le ballon et le but et dégage le ballon
"""

class Defenseur(SoccerStrategy):
    def __init__(self):
        self.defense = CompoStrat(AllerButBallon(), Degagement())
        self.urgence = Fonceur()
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        distance = state.ball.position - player.position
        if(distance.norm < 20):
            return self.urgence.compute_strategy(state,player,teamid)
        else:
            return self.defense.compute_strategy(state,player,teamid)
    def create_strategy(self):
        return Defenseur()


"""
Stratégie défenseurv0.1
Se place entre le ballon et le but et dégage le ballon
"""

class Defenseurv01(SoccerStrategy):
    def __init__(self):
        self.defense = CompoStrat(AllerButBallon(), Degagement())
        self.urgence = Fonceur()
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        distance = state.ball.position - state.get_goal_center(teamid)
        if(distance.norm < 40):
            return self.urgence.compute_strategy(state,player,teamid)
        else:
            return self.defense.compute_strategy(state,player,teamid)
    def create_strategy(self):
        return Defenseurv01()
        

"""
Strategie dribbleur
Essaye d'avoir un comportement imprévisible
"""

class Dribbleur(SoccerStrategy):
    def __init__(self):
        self.drib = CompoStrat(AllerVersBallon(), Dribble())
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        return self.drib.compute_strategy(state,player,teamid)
    def create_strategy(self):
        return Dribbleur()
        
"""
Strategie interception
Se dirige devant le ballon
"""

class Interception(SoccerStrategy):
    def __init__(self):
        self.strat = AllerVersLoc(Vector2D())
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        goalcen = state.get_goal_center(teamid)
        goalcen = Vector2D(goalcen.x *0.1 + state.ball.position.x*0.9,goalcen.y *0.1 + state.ball.position.y*0.9)
        self.strat.loc = goalcen
        return self.strat.compute_strategy(state,player,teamid)
    def create_strategy(self):
        return Interception()
        
"""
Strategie d'intercepteur
Se place devant le ballon et le prend au joueur adverse
"""

class Intercepteur(SoccerStrategy):
    def __init__(self):
        self.inter = CompoStrat(Interception(), Tir())
        self.atck = CompoStrat(AllerVersBallon(), Tir())
        self.aballon = 0
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        dist = state.ball.position - player.position
        if(dist.norm < 15 or self.aballon == 1):
            self.aballon = 1
            return self.atck.compute_strategy(state, player, teamid)
        else:
            return self.inter.compute_strategy(state,player,teamid)
    def create_strategy(self):
        return Intercepteur()
