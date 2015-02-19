# coding=utf-8
from soccersimulator import Vector2D, SoccerBattle, SoccerPlayer, SoccerTeam, SoccerAction, SoccerStrategy, SoccerState
from soccersimulator import PygletObserver,ConsoleListener,LogListener
from soccersimulator import PLAYER_RADIUS, BALL_RADIUS, GAME_WIDTH, GAME_HEIGHT
import outils
import random
import pdb


'''
Stratégie Vide
Le joueur ne fait rien
'''

class VideS(SoccerStrategy):
    def __init__(self):
        pass
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        return SoccerAction()
    def create_strategy(self):
        return VideS()

'''
Stratégie de mouvement
Se déplace vers un point indiqué
'''
class AllerVersLoc(SoccerStrategy):
    def __init__(self, localisation):
        self.loc = localisation        
        pass
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        mouvement = self.loc - player.position
        return SoccerAction(mouvement)
    def create_strategy(self):
        return AllerVersLoc()
        
        
'''
Stratégie de mouvement
Le joueur se déplacera vers le point indiqué
'''

class AllerVersBallon(SoccerStrategy):
    def __init__(self):
        self.strat= AllerVersLoc(Vector2D())
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        self.strat.loc= state.ball.position
        #mouvement = state.ball.position - player.position
        return self.strat.compute_strategy(state,player,teamid)
    def create_strategy(self):
        return AllerVersBallon()

"""
Stratégie de mouvement
Le joueur se place entre le ballon et son but
"""

class AllerButBallon(SoccerStrategy):
    def __init__(self):
        self.strat= AllerVersLoc(Vector2D())
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        self.strat.loc = state.ball.position + state.get_goal_center(teamid)
        self.strat.loc.product = self.strat.loc.product(0.5)
        #mouvement = state.ball.position - player.position
        return self.strat.compute_strategy(state,player,teamid)
    def create_strategy(self):
        return AllerButBallon()

"""
Stratégie de tir
Le joueur frappe le ballon en face de lui dans un angle aléatoire
"""
class Degagement(SoccerStrategy):
    def __init__(self):
        pass
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        tir = Vector2D.create_polar(player.angle + 2.5, 100)
        return SoccerAction(Vector2D(0,0), tir)
    def create_strategy(self):
        return Degagement()


"""
Stratégie de tir
Le joueur dribble de façon imprévisible
"""  
class Dribble(SoccerStrategy):
    def __init__(self):
        pass
    def start_battle(self,state):
        elf.strat.locpass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
            dri = state.get_goal_center(outils.IDTeamOp(teamid)) - player.position
            drib = Vector2D.create_polar(dri.angle + random.random()*2-1,1)
            return SoccerAction(Vector2D(0,0), drib)
    def create_strategy(self):
        return Dribble()


"""
Stratégie de frappe
Le joueur tire vers le but
"""     
        
        
class Tir(SoccerStrategy):
    def __init__(self):
        pass
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        tir = state.get_goal_center(outils.IDTeamOp(teamid)) - player.position
        return SoccerAction(Vector2D(0,0), tir)
    def create_strategy(self):
        return Tir()
   
"""
Fusionne deux starts, une de tir et une de mouvement
"""
class CompoStrat(SoccerStrategy):
    def __init__(self, strat1, strat2):
        self.s1 = strat1
        self.s2 = strat2
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        move = self.s1.compute_strategy(state, player, teamid)
        shot = self.s2.compute_strategy(state, player, teamid)
        return SoccerAction(move.acceleration, shot.shoot)
    def create_strategy(self):
        return CompoStrat()
"""
Stratégie fonceurVideS
Utilise stratégie AllerVersBallon
"""

class Fonceur(SoccerStrategy):
    def __init__(self):
        self.fonceur = CompoStrat(AllerVersBallon(), Tir())
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        return self.fonceur.compute_strategy(state,player,teamid)
    def create_strategy(self):
        return Fonceur()


"""
Stratégie défenseur
Se place entre le ballon et le but et dégage le ballon
"""

class Defonceur(SoccerStrategy):
    def __init__(self):
        self.defense = CompoStrat(AllerButBallon(), Degagement())
        self.urgence = Fonceur()
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        distance = state.ball.position - player.position
        if(distance.norm < 10):
            return self.urgence.compute_strategy(state,player,teamid)
        else:
            return self.defense.compute_strategy(state,player,teamid)
    def create_strategy(self):
        return Defenceur()


"""
Stratégie défenseurv0.1
Se place entre le ballon et le but et dégage le ballon
"""

class Defenseur(SoccerStrategy):
    def __init__(self):
        self.defense = CompoStrat(AllerButBallon(), Degagement())
        self.urgence = Intercepteur()
        self.out = Outils()
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        distance = state.ball.position - state.get_goal_center(teamid)
        ball = state.ball.position - player.position
        if(self.out.nbadvbalbut(state, outils.IDTeamOp(teamid), player) <= 1):
            return self.urgence.compute_strategy(state,player,teamid)
        else:
            return self.defense.compute_strategy(state,player,teamid)
    def create_strategy(self):
        return Defenseur()
        

"""
Strategie dribbleur
Essaye d'avoir un comportement imprévisible
"""

class Dribbleur(SoccerStrategy):
    def __init__(self):
        self.drib = CompoStrat(AllerVersBallon(), Dribble())
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        return self.drib.compute_strategy(state,player,teamid)
    def create_strategy(self):
        return Dribbleur()
        
"""
Strategie interception
Se dirige devant le ballon
"""

class Interception(SoccerStrategy):
    def __init__(self):
        self.strat = AllerVersLoc(Vector2D())
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        goalcen = state.get_goal_center(teamid)
        goalcen = Vector2D(goalcen.x *0.1 + state.ball.position.x*0.9,goalcen.y *0.1 + state.ball.position.y*0.9)
        self.strat.loc = goalcen
        return self.strat.compute_strategy(state,player,teamid)
    def create_strategy(self):
        return Interception()
        
        
"""
Srategie d'esquive
Tir de manière à éviter les adversaires
"""
   
class Esquive(SoccerStrategy):
    def __init__(self):
        self.out = Outils()
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        goal = state.get_goal_center(outils.IDTeamOp(teamid))
        yadv = self.out.jpro(state, teamid, player).y
        yme = player.position.y
        if(yadv > yme):
            dire = goal - player.position
            go = Vector2D.create_polar(dire.angle - 0.35, 1)
        else:           
            dire = goal - player.position
            go = Vector2D.create_polar(dire.angle + 0.35, 1)
        
        return SoccerAction(Vector2D(0,0), go)
    def create_strategy(self):
        return Esquive()

"""
Stratégie de Dribble avancé
Le joueur évite l'adversaire et se déplace de façon adapté
"""
class Attaquant(SoccerStrategy):
    def __init__(self):
        self.but = CompoStrat(AllerVersBallon(), Tir())
        self.atck = CompoStrat(AllerVersBallon(), Esquive())
        self.defen = CompoStrat(AllerVersBallon(), Degagement())
        self.aballon = 0
        self.test = Outils()
    def start_battle(self,state):
        pass
    def begin_battles(self,state,count,max_step):
        self.aballon = 0
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
    #    a = self.test.distballon(self.test, teamid, 1) #TEST DEBUG        
        dist = state.ball.position - player.position
        but = state.get_goal_center(outils.IDTeamOp(teamid)).x - player.position.x
        if(abs(but) < 15):
            return self.but.compute_strategy(state, player, teamid)
        if(dist.norm > 20):
            self.aballon = 0
        if(dist.norm < 3 or self.aballon):
            self.aballon = 1
            return self.atck.compute_strategy(state, player, teamid)
        else:
            return self.defen.compute_strategy(state,player,teamid)
    def create_strategy(self):
        return Intercepteur()

"""
Strategie d'intercepteur
Se place devant le ballon et le prend au joueur adverse
"""

class Intercepteur(SoccerStrategy):
    def __init__(self):
        self.inter = CompoStrat(Interception(), Tir())
        self.atck = CompoStrat(AllerVersBallon(), Dribble())
        self.fonceur = CompoStrat(AllerVersBallon(), Tir())
        self.aballon = 0
        self.test = Outils()
    def start_battle(self,state):
        pass
    def begin_battles(self,state,count,max_step):
        self.aballon = 0
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
    #    a = self.test.distballon(self.test, teamid, 1) #TEST DEBUG        
        dist = state.ball.position - player.position
        but = state.get_goal_center(outils.IDTeamOp(teamid)) - player.position
        if(but.norm < 25):
            return self.fonceur.compute_strategy(state, player, teamid)
        if(dist.norm > 20):
            self.aballon = 0
        if(dist.norm < 3 or self.aballon):
            self.aballon = 1
            return self.atck.compute_strategy(state, player, teamid)
        else:
            return self.inter.compute_strategy(state,player,teamid)
    def create_strategy(self):
        return Intercepteur()

"""
Strategie d'intercepteur
Se place devant le ballon et le prend au joueur adverse V2.0
"""
class SurIntercepteur(SoccerStrategy):
    def __init__(self):
        self.inter = CompoStrat(Interception(), Tir())
        self.atck = CompoStrat(AllerVersBallon(), Esquive())
        self.fonceur = CompoStrat(AllerVersBallon(), Tir())
        self.test = Outils()
        self.attente = random.random() * 100 + 150
    def start_battle(self,state):
        pass
    def begin_battles(self,state,count,max_step):
        self.attente = random.random() * 100 + 150
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        dist = state.ball.position - player.position
        but = state.get_goal_center(outils.IDTeamOp(teamid)) - player.position
        butx = state.get_goal_center(outils.IDTeamOp(teamid)).x - player.position.x
        if(self.test.nbadvbalbut(state, teamid, player) == 2 and self.attente >= 1):
            self.attente = self.attente - 1            
            return self.inter.compute_strategy(state, player, teamid)
        if((self.test.nbadvbalbut(state, teamid, player) == 1 or self.attente < 1) and abs(butx) > 15):
            return self.atck.compute_strategy(state, player, teamid)
        else:
            return self.fonceur.compute_strategy(state,player,teamid)
    def create_strategy(self):
        return SurIntercepteur()
'''
Intercepteur 4v4
'''     
class TeamIntercepteur(SoccerStrategy):
    def __init__(self):
        self.inter = CompoStrat(Interception(), Tir())
        self.atck = CompoStrat(AllerVersBallon(), Esquive())
        self.fonceur = CompoStrat(AllerVersBallon(), Tir())
        self.test = Outils()
        self.attente = random.random() * 100 + 150
    def start_battle(self,state):
        pass
    def begin_battles(self,state,count,max_step):
        self.attente = random.random() * 100 + 150
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        dist = state.ball.position - player.position
        but = state.get_goal_center(outils.IDTeamOp(teamid)) - player.position
        butx = state.get_goal_center(outils.IDTeamOp(teamid)).x - player.position.x
        if(self.test.nbadvbalbut(state, teamid, player) == 4 and self.attente >= 1):
            self.attente = self.attente - 1            
            return self.inter.compute_strategy(state, player, teamid)
        if((self.test.nbadvbalbut(state, teamid, player) >= 1 or self.attente < 1) and abs(butx) > 15):
            return self.atck.compute_strategy(state, player, teamid)
        else:
            return self.fonceur.compute_strategy(state,player,teamid)
    def create_strategy(self):
        return TeamIntercepteur()
        
"""
Stratégie de mouvement
Attend un joueur pour lui prendre le ballon
"""
class DefMove(SoccerStrategy):
    def __init__(self):
        self.defense = CompoStrat(AllerButBallon(), VideS())
        self.subti = CompoStrat(Fonceur(), VideS())
        self.attente = CompoStrat(VideS(), VideS())
        self.aggro = CompoStrat(AllerVersBallon(), Degagement())
        self.revanche = CompoStrat(AllerVersBallon(), Tir())
        self.out = Outils()
        self.adefendu = False
    def start_battle(self,state):
        pass
    def begin_battles(self, state,count,max_step):
        self.adefendu = False
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        distance = self.out.distadvballon(state, teamid, player)
        distball = state.ball.position - player.position
        if(self.adefendu):
            return self.revanche.compute_strategy(state,player,teamid)
        elif(PLAYER_RADIUS + BALL_RADIUS > distball.norm):
            self.adefendu = True
            return self.aggro.compute_strategy(state,player,teamid)
        elif(distance < 3):
            return self.subti.compute_strategy(state,player,teamid)
        elif(distball.norm < GAME_WIDTH*0.1):
            return self.attente.compute_strategy(state, player, teamid)
        else:
            return self.defense.compute_strategy(state,player,teamid)
    def create_strategy(self):
        return DefMove()
        
############################################################################################################################################################ 
#OUTILS
############################################################################################################################################################
class Outils(SoccerState):
    def __init__(self):
        pass        
    
    def distadvballon(self, state, team, player):
        dist = 9999       
        if(team == 2):
            for p in state.team1 :
                vec = state.ball.position - p.position
                dist = min(vec.norm, dist)
        else:
            for p in state.team2 :
                vec = state.ball.position - p.position
                dist = min(vec.norm, dist)
        return dist
        
    def nbadvbalbut(self, state, team, player):
        nb = 0
        if(team == 2):
            for p in state.team1 :
                distun = state.get_goal_center(outils.IDTeamOp(team)) - p.position 
                distdeux = state.get_goal_center(outils.IDTeamOp(team)) - state.ball.position 
                if(distun.norm < distdeux.norm):
                    nb = nb + 1
        else:
            for p in state.team2 :
                distun = state.get_goal_center(outils.IDTeamOp(team)) - p.position 
                distdeux = state.get_goal_center(outils.IDTeamOp(team)) - state.ball.position
                if(distun.norm < distdeux.norm):
                    nb = nb+1
        return nb
    
    def jpro(self, state, team, player):
        dist = 9999
        vec = Vector2D(0,0)
        if(team == 2):
            for p in state.team1 :
                distmebut = state.get_goal_center(outils.IDTeamOp(team)) - player.position
                distluibut = state.get_goal_center(outils.IDTeamOp(team)) - p.position
                distmelui = p.position - player.position
                if(distluibut.norm < distmebut.norm and distmelui.norm < dist):
                    dist = distmelui.norm
                    vec = p.position
        else:
            for p in state.team2 :
                distmebut = state.get_goal_center(outils.IDTeamOp(team)) - player.position 
                distluibut = state.get_goal_center(outils.IDTeamOp(team)) - p.position
                distmelui = p.position - player.position
                if(distluibut.norm < distmebut.norm and distmelui.norm < dist):
                    dist = distmelui.norm
                    vec = p.position
        return vec
        