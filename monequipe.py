from soccersimulator import SoccerBattle, SoccerPlayer, SoccerTeam
from soccersimulator import PygletObserver,ConsoleListener,LogListener
from soccersimulator import pyglet
from strats import GoalStrategy
from strats import GoalFixeStrategy
from strats import FonceurStrategy
from strats import ZigStrategy

team1=SoccerTeam("1v1")
team1.add_player(SoccerPlayer("t1j1",GoalStrategy()))

team2=SoccerTeam("2v2")
team1.add_player(SoccerPlayer("t1j1",GoalFixeStrategy()))
team1.add_player(SoccerPlayer("t1j2",ZigStrategy()))

team3=SoccerTeam("4v4")
team1.add_player(SoccerPlayer("t1j1",GoalStrategy()))
team1.add_player(SoccerPlayer("t1j2",GoalFixeStrategy()))
team1.add_player(SoccerPlayer("t1j3",FonceurStrategy()))
team1.add_player(SoccerPlayer("t1j4",ZigStrategy()))

teams =[team1,team2,team3]

