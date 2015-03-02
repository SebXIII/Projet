from soccersimulator import SoccerBattle, SoccerPlayer, SoccerTeam
from soccersimulator import PygletObserver,ConsoleListener,LogListener
from soccersimulator import pyglet
from strats import AllerVersBallon, Esquive, Attaquant, Tir, TeamIntercepteur, VideS, AllerVersLoc, CompoStrat, Fonceur, DefMove, AllerButBallon, Degagement, Defonceur, Defenseur, Dribble, Dribbleur, SurIntercepteur ,Interception, Intercepteur

team1=SoccerTeam("Team Solo Mid 1v1")
team1.add_player(SoccerPlayer("Dyrus",Intercepteur()))

team4=SoccerTeam("Fnatic 2v2")
team4.add_player(SoccerPlayer("t1j1",DefMove()))
team4.add_player(SoccerPlayer("t1j2",SurIntercepteur()))

team3=SoccerTeam("SK 2v2")
team3.add_player(SoccerPlayer("t1j1",SurIntercepteur()))
team3.add_player(SoccerPlayer("t1j2",Attaquant()))

team6=SoccerTeam("Versus Trying 2")
team6.add_player(SoccerPlayer("Bot 1",VideS()))
team6.add_player(SoccerPlayer("Bot 2",Fonceur()))

team0=SoccerTeam("Versus Trying")
team0.add_player(SoccerPlayer("Bot 1",VideS()))
team0.add_player(SoccerPlayer("Bot 2",Defonceur()))

team5=SoccerTeam("Unicorn of Love 4v4")
team5.add_player(SoccerPlayer("t1j1",Defonceur()))
team5.add_player(SoccerPlayer("t1j2",DefMove()))
team5.add_player(SoccerPlayer("t1j3",Defenseur()))
team5.add_player(SoccerPlayer("t1j4",TeamIntercepteur()))

teams =[team1, team3, team4, team5]