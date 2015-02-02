from soccersimulator import SoccerBattle, SoccerPlayer, SoccerTeam
from soccersimulator import PygletObserver,ConsoleListener,LogListener
from soccersimulator import pyglet
from strats import AllerVersBallon, Tir, VideS

team1=SoccerTeam("1v1")
team1.add_player(SoccerPlayer("t1j1",AllerVersBallon()))

team2=SoccerTeam("2v2")
team1.add_player(SoccerPlayer("t1j1",AllerVersBallon()))
team1.add_player(SoccerPlayer("t1j2",AllerVersBallon()))

team3=SoccerTeam("4v4")
team1.add_player(SoccerPlayer("t1j1",AllerVersBallon()))
team1.add_player(SoccerPlayer("t1j2",AllerVersBallon()))
team1.add_player(SoccerPlayer("t1j3",AllerVersBallon()))
team1.add_player(SoccerPlayer("t1j4",AllerVersBallon()))

teams =[team1,team2,team3]