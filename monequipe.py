from soccersimulator import SoccerBattle, SoccerPlayer, SoccerTeam
from soccersimulator import PygletObserver,ConsoleListener,LogListener
from soccersimulator import pyglet
from strats import AllerVersBallon, Tir, TeamIntercepteur, VideS, AllerVersLoc, CompoStrat, Fonceur, DefMove, AllerButBallon, Degagement, Defonceur, Defenseur, Dribble, Dribbleur, SurIntercepteur ,Interception, Intercepteur

team1=SoccerTeam("Team Solo Mid 1v1")
team1.add_player(SoccerPlayer("t1j1",Intercepteur()))

team4=SoccerTeam("Fnatic 2v2")
team4.add_player(SoccerPlayer("t1j1",SurIntercepteur()))
team4.add_player(SoccerPlayer("t1j2",DefMove()))

team3=SoccerTeam("Tueur de fonceur 2v2")
team3.add_player(SoccerPlayer("t1j1",Intercepteur()))
team3.add_player(SoccerPlayer("t1j2",DefMove()))

team0=SoccerTeam("Versus Trying")
team0.add_player(SoccerPlayer("t1j1",DefMove()))
team0.add_player(SoccerPlayer("t1j2",Defonceur()))

team5=SoccerTeam("Unicorn of Love 4v4")
team5.add_player(SoccerPlayer("t1j1",DefMove()))
team5.add_player(SoccerPlayer("t1j2",DefMove()))
team5.add_player(SoccerPlayer("t1j3",Teamintercepteur()))
team5.add_player(SoccerPlayer("t1j4",TeamIntercepteur()))

teams =[team1, team4, team3, team5]