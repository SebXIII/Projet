from soccersimulator import SoccerBattle, SoccerPlayer, SoccerTeam
from soccersimulator import PygletObserver,ConsoleListener,LogListener, InteractStrategy
from soccersimulator import pyglet
from strats import *


team1=SoccerTeam("Team Solo Mid 1v1")
team1.add_player(SoccerPlayer("Dyrus",Intercepteur()))

#team7=SoccerTeam("Cloud 9 1v1")
#team7.add_player(SoccerPlayer("Hai", Follow()))

team4=SoccerTeam("Fnatic 2v2")
team4.add_player(SoccerPlayer("Reignover",Follow()))
team4.add_player(SoccerPlayer("Steeelback",SurIntercepteur()))

team3=SoccerTeam("SK 2v2")
team3.add_player(SoccerPlayer("Fredy122",SurIntercepteur()))
team3.add_player(SoccerPlayer("Fox",Defenseur()))

team6=SoccerTeam("Versus Trying 2")
team6.add_player(SoccerPlayer("Bot 1",Defenseur()))

team0=SoccerTeam("Versus Trying")
team0.add_player(SoccerPlayer("Bot 2",Follow()))
team0.add_player(SoccerPlayer("Bot 1",VideS()))

team9=SoccerTeam("Versus Trying 3")
team9.add_player(SoccerPlayer("Bot 2",Defenseur()))
team9.add_player(SoccerPlayer("Bot 1",VideS()))

team5=SoccerTeam("Unicorn of Love 4v4")
team5.add_player(SoccerPlayer("Vizicsacsi",Fonceur()))
team5.add_player(SoccerPlayer("Kikis",Fonceur()))
team5.add_player(SoccerPlayer("PowerOfEvil",Defenseur()))
team5.add_player(SoccerPlayer("Vardags",TeamIntercepteur()))

team9 = SoccerTeam("App")
list_key_player1=['a','z', 'e', 'r', 't', 'y']
list_strat_player1=[AppFonceur(),AppDefenseur(),AppSuivre(), AppInterception(), AppDribble(), AppPasse()]
inter_strat_player1=InteractStrategy(list_key_player1,list_strat_player1,"tent3.2.pkl")
team9.add_player(SoccerPlayer("Robot", inter_strat_player1))
team9.add_player(SoccerPlayer("Robocop",TreeStrat()))

team10 = SoccerTeam("Tree")
team10.add_player(SoccerPlayer("Truc",Fonceur()))
team10.add_player(SoccerPlayer("Robotbis",TreeStrat()))
teams =[team1, team3, team4, team5, team9, team10]