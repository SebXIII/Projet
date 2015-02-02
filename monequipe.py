from soccersimulator import SoccerBattle, SoccerPlayer, SoccerTeam
from soccersimulator import PygletObserver,ConsoleListener,LogListener
from soccersimulator import pyglet
from strats import AllerVersBallon, Tir, VideS, AllerVersLoc, CompoStrat, Fonceur, AllerButBallon, Degagement, Defenseur

team1=SoccerTeam("1v1")
team1.add_player(SoccerPlayer("t1j1",AllerVersBallon()))

team2=SoccerTeam("2v2")
team2.add_player(SoccerPlayer("t1j1",Fonceur()))
team2.add_player(SoccerPlayer("t1j2",Defenseur()))

team3=SoccerTeam("4v4")
team3.add_player(SoccerPlayer("t1j1",VideS()))
team3.add_player(SoccerPlayer("t1j2",AllerVersBallon()))
team3.add_player(SoccerPlayer("t1j3",AllerVersBallon()))
team3.add_player(SoccerPlayer("t1j4",AllerVersBallon()))

teams =[team1,team2,team3]