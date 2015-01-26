#Importation
from soccersimulator import pyglet
from soccersimulator import Vector2D
from soccersimulator import SoccerAction
from soccersimulator import SoccerBall
from soccersimulator import SoccerStrategy
from soccersimulator import SoccerTeam
from soccersimulator import SoccerPlayer
from soccersimulator import SoccerBattle,PygletObserver,ConsoleListener,LogListener


#Test avec Vec et autre
vec = Vector2D(1,1)
vec2 = Vector2D(2,0)
vec3 = vec + vec2
vec3.norm
vecrand = Vector2D()
vecrand.random(-1,1)
vecrand.norm
act = SoccerAction(vecrand,vec)
laboule = SoccerBall(vecrand, vec)
laboule.angle

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
class GoalStrategy(SoccerStrategy):
    def __init__(self):
        self.name="Goal"
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        dif = state.ball.position - player.position
        if dif.norm > 15:
            vitesse = state.ball.position + state.get_goal_center(teamid) - player.position  - player.position
        else:
            vitesse = state.ball.position - player.position
        tir = state.get_goal_center(self.get_op(teamid)) - player.position
        if tir.norm > BALL_RADIUS + PLAYER_RADIUS:  #calcul distance ballon
            return SoccerAction(vitesse)
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
        
#lancement partie
team1=SoccerTeam("team1")
team2=SoccerTeam("team2")
team1.add_player(SoccerPlayer("t1j1",FonceurStrategy()))
team2.add_player(SoccerPlayer("t2j1",GoalStrategy()))
team1.add_player(SoccerPlayer("t1j2",FonceurStrategy()))
team2.add_player(SoccerPlayer("t2j2",GoalStrategy()))
battle=SoccerBattle(team1,team2)
obs=PygletObserver()
obs.set_soccer_battle(battle)
pyglet.app.run()
