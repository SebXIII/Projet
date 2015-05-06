# -*- coding: utf-8 -*-
from soccersimulator import *
from strats import *
from apprentissage import gen_feature_simple

#team666=SoccerTeam("Satan")
#team666.add_player(SoccerPlayer("Satan",Hero()))

team999=SoccerTeam("Naja testeur")
team999.add_player(SoccerPlayer("Naja",Fonceur()))




team1=SoccerTeam("Team Solo Mid 1v1")
team1.add_player(SoccerPlayer("Dyrus",Intercepteur()))

#team7=SoccerTeam("Cloud 9 1v1")
#team7.add_player(SoccerPlayer("Hai", Follow()))

team666=SoccerTeam("SATAN NAJA")
team666.add_player(SoccerPlayer("Satan",Fonceurdelaboue()))
team666.add_player(SoccerPlayer("Naja",SurIntercepteur()))


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

"""
team9=SoccerTeam("Versus Trying 3")
team9.add_player(SoccerPlayer("Bot 2",Defenseur()))
team9.add_player(SoccerPlayer("Bot 1",VideS()))
"""

team5=SoccerTeam("Unicorn of Love 4v4")
team5.add_player(SoccerPlayer("Vizicsacsi",Fonceur()))
team5.add_player(SoccerPlayer("Kikis",Fonceur()))
team5.add_player(SoccerPlayer("PowerOfEvil",Defenseur()))
team5.add_player(SoccerPlayer("Vardags",TeamIntercepteur()))

team9 = SoccerTeam("App")
list_key_player1=['a','z', 'e', 'r',]
#Ancienne liste de nom
list_strat=[AppFonceur(),AppDefenseur(),AppSuivre(), AppPasse(), AppAttente(), AppContourne(), AppDegagement(), AppFrappe()]
list_nom=["fonceur", "defenseur", "suivre", "passe", "attente", "contourne", "degagement", "frappe"]
#Nouvelle liste de nom
list_strat2=[AppAttaque(),AppDefenseur(), AppAttente(), AppInterception()]
list_nom2=["fonceur", "defenseur", "attente", "interception"]

list_strat_player1=list(list_strat2)
inter_strat_player1=InteractStrategy(list_key_player1,list_strat_player1,"songicefire.pkl")
team9.add_player(SoccerPlayer("Bot ATK", inter_strat_player1))
team9.add_player(SoccerPlayer("Co Fonceur",Defenseur()))

'''
list_key_player2=['q', 's', 'd', 'f', 'g', 'h', 'j', 'k']
list_strat_player2=list(list_strat)
inter_strat_player2=InteractStrategy(list_key_player1,list_strat_player1,"botdef1.pkl")
team9.add_player(SoccerPlayer("Bot DEF",inter_strat_player2))
'''

### Apprentissage
team_tree = SoccerTeam("Team Tree")
treeia=TreeIA(gen_feature_simple,dict(zip(list_nom,list_strat)))

fn=os.path.join(os.path.dirname(os.path.realpath(__file__)),"arbresongicefire.pkl")
treeia.load(fn)
TreeST=TreeStrategy("IA atk",treeia)

'''treeia2=TreeIA(gen_feature_simple,dict(zip(list_nom,list_strat)))
fn=os.path.join(os.path.dirname(os.path.realpath(__file__)),"arbrebotdef1.pkl")
treeia2.load(fn)
TreeST2=TreeStrategy("IA def",treeia2)'''
team_tree.add_player(SoccerPlayer("Robot de la boue", TreeST))
'''team_tree.add_player(SoccerPlayer("Robot DEF", TreeST2))'''
team_tree.add_player(SoccerPlayer("Co Fonceur",Defenseur()))


teams =[team9, team3, team4, team666, team_tree, team5]