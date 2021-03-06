#Importation
import random
from soccersimulator import pyglet
from soccersimulator import Vector2D
from soccersimulator import SoccerAction
from soccersimulator import SoccerBall
from soccersimulator import SoccerStrategy
from soccersimulator import SoccerTeam
from soccersimulator import SoccerPlayer
from soccersimulator import SoccerBattle,PygletObserver,ConsoleListener,LogListener


#Test avec Vec et autre
'''vec = Vector2D(1,1)
vec2 = Vector2D(2,0)
vec3 = vec + vec2
vec3.norm
vecrand = Vector2D()
vecrand.random(-1,1)
vecrand.norm
vec3 = Vector2D(2000,3)
vec3.normalize
vec3
act = SoccerAction(vecrand,vec)
laboule = SoccerBall(vecrand, vec)
laboule.angle'''

#Création de la random stratégie
class RandomStrategy(SoccerStrategy):
    def __init__(self):
        self.name="Random"
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        vitesse = Vector2D.create_random(-1,1)
        tir = Vector2D.create_random(-1,1)
        return SoccerAction(vitesse, tir)
    def copy(self):
        return RandomStrategy()
    def create_strategy(self):
        return RandomStrategy()

#Création de la fonceur stratégie
class FonceurStrategy(SoccerStrategy):
    def __init__(self):
        self.name="Fonceur"
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        vitesse = state.ball.position - player.position
        tir = state.get_goal_center(self.get_op(teamid)) - player.position
        return SoccerAction(vitesse, tir)
    def copy(self):
        return FonceurStrategy()
    def create_strategy(self):
        return FonceurStrategy()
    def get_op(self, teamid):
        if teamid == 1:
            return 2
        else:
            return 1
            
            
#Création de la fonceur stratégie
class ZigStrategy(SoccerStrategy):
    def __init__(self):
        self.name="Zig"
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        r = random.randint(1,10)
        r = r % 2
        vitesse = state.ball.position - player.position
        tir = state.get_goal_center(self.get_op(teamid)) - player.position
        angle = tir.angle
        if r == 0:
            angle = angle + 0.9
        if r == 1:
            angle == angle - 0.9
        frappe = Vector2D.create_polar(angle, 1000)
        
        return SoccerAction(vitesse, frappe)
    def copy(self):
        return ZigStrategy()
    def create_strategy(self):
        return ZigStrategy()
    def get_op(self, teamid):
        if teamid == 1:
            return 2
        else:
            return 1
            
            

class SlowStrategy(SoccerStrategy):
    def __init__(self):
        self.name="Slow"
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        vitesse = state.ball.position - player.position
        if vitesse.norm > 20:
            vitesse.product(0.0025)
        tir = state.get_goal_center(self.get_op(teamid)) - player.position
        return SoccerAction(vitesse, tir)
    def copy(self):
        return SlowStrategy()
    def create_strategy(self):
        return SlowStrategy()
    def get_op(self, teamid):
        if teamid == 1:
            return 2
        else:
            return 1
            create_polar(angle,norm)
#Création de la fonceur stratégie
class GoalStrategy(SoccerStrategy):
    def __init__(self):
        self.name="Goal"
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        dif = state.ball.position - player.position
        if dif.norm > 20:
            vitesse = state.ball.position + state.get_goal_center(teamid) - player.position  - player.position
        else:
            vitesse = state.ball.position - player.position
        tir = state.get_goal_center(self.get_op(teamid)) - player.position
        return SoccerAction(vitesse, tir)
    def copy(self):
        return GoalStrategy()
    def create_strategy(self):
        return GoalStrategy()
    def get_op(self, teamid):
        if teamid == 1:
            return 2
        else:
            return 1
            
class GoalFixeStrategy(SoccerStrategy):
    def __init__(self):
        self.name="Goal"
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        dif = state.ball.position - player.position
        if dif.norm > 40:
            vitesse = state.get_goal_center(teamid)  - player.position
        else:
            vitesse = state.ball.position - player.position
        tir = state.get_goal_center(self.get_op(teamid)) - player.position + state.get_goal_center(self.get_op(teamid)) - player.position
        return SoccerAction(vitesse, tir)
    def copy(self):
        return GoalFixeStrategy()
    def create_strategy(self):
        return GoalFixeStrategy()
    def get_op(self, teamid):
        if teamid == 1:
            return 2
        else:
            return 1
        
#lancement partie
team1=SoccerTeam("team1")
team2=SoccerTeam("team2")
team1.add_player(SoccerPlayer("t1j1",ZigStrategy()))
team2.add_player(SoccerPlayer("t2j1",FonceurStrategy()))
team1.add_player(SoccerPlayer("t1j2",GoalFixeStrategy()))
team2.add_player(SoccerPlayer("t2j2",GoalFixeStrategy()))
battle=SoccerBattle(team1,team2)
obs=PygletObserver()
obs.set_soccer_battle(battle)
pyglet.app.run()
