from soccersimulator import SoccerBattle, SoccerPlayer, SoccerTeam
from soccersimulator import PygletObserver,ConsoleListener,LogListener
from soccersimulator import pyglet
from strats import AllerVersBallon, Tir, VideS, AllerVersLoc, CompoStrat, Fonceur, AllerButBallon, Degagement, Defenseur, Dribble, Dribbleur, Interception, Intercepteur

team1=SoccerTeam("Panda 1v1")
team1.add_player(SoccerPlayer("t1j1",Dribbleur()))

team2=SoccerTeam("Dragon 2v2")
team2.add_player(SoccerPlayer("t1j1",Intercepteur()))
team2.add_player(SoccerPlayer("t1j2",Defenseur()))

team4=SoccerTeam("Versus Trying")
team4.add_player(SoccerPlayer("t1j1",Fonceur()))
team4.add_player(SoccerPlayer("t1j2",Dribbleur()))

team3=SoccerTeam("Unicorn of Love 4v4")
team3.add_player(SoccerPlayer("t1j1",Defenseur()))
team3.add_player(SoccerPlayer("t1j2",Fonceur()))
team3.add_player(SoccerPlayer("t1j3",Dribbleur()))
team3.add_player(SoccerPlayer("t1j4",Intercepteur()))

teams =[team1,team2,team3, team4]