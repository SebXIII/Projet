from soccersimulator import SoccerBattle, SoccerPlayer, SoccerTeam
from soccersimulator import PygletObserver,ConsoleListener,LogListener
from soccersimulator import pyglet
from strats import AllerVersBallon, Tir, VideS, AllerVersLoc, CompoStrat, Fonceur, AllerButBallon, Degagement, Defenseur, Dribble, Dribbleur, Interception, Intercepteur

team8=SoccerTeam("Pandragon 1v1")
team8.add_player(SoccerPlayer("t1j1",Intercepteur()))

team9=SoccerTeam("Super Pandragon 1v1")
team9.add_player(SoccerPlayer("t1j1",Intercepteur()))

team2=SoccerTeam("Tueur de fonceur 2v2")
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

teams =[team2,team3, team4, team7, team8, team9]