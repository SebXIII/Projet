# coding=utf-8
from soccersimulator import Vector2D, SoccerBattle, SoccerPlayer, SoccerTeam, SoccerAction, SoccerStrategy, SoccerState
from soccersimulator import PygletObserver,ConsoleListener,LogListener
from soccersimulator import PLAYER_RADIUS, BALL_RADIUS, GAME_WIDTH, GAME_HEIGHT, GAME_GOAL_HEIGHT
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
        return SoccerAction(mouvement, Vector2D(0,0))
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
        self.strat.loc= state.ball.position + state.ball.speed
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
        test = Outils(state, teamid, player)
        if(test.canshoot()):
            tir = Vector2D.create_polar(player.angle + 2.5, 100)
        else:
            tir = Vector2D(0,0)
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
        self.strat.locpass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        dri = state.get_goal_center(outils.IDTeamOp(teamid)) - player.position
        test = Outils(state, teamid, player)
        if(test.canshoot()):
            drib = Vector2D.create_polar(dri.angle + random.random()*2-1,1)
        else:
            drib = Vector2D(0,0)
        return SoccerAction(Vector2D(0,0), drib)
    def create_strategy(self):
        return Dribble()
        
"""
Stratégie de frappe
Le joueur tire vers le but de façon vicieuse
"""     
        
        
class Tirv(SoccerStrategy):
    def __init__(self):
        pass
    def start_battle(self,state):
        pass
    def begin_battles(self,state,count,max_step):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        test = Outils(state, teamid, player)
        tir = Vector2D(0,0)
        tir = state.get_goal_center(outils.IDTeamOp(teamid)) - player.position
        if(test.goalsupmid()):
            tir.x = tir.x - (GAME_GOAL_HEIGHT / 2) * 0.75
            tir.y = tir.y - (GAME_GOAL_HEIGHT / 2)*0.75
        else:
            tir.x = tir.x + (GAME_GOAL_HEIGHT / 2)*0.75
            tir.y = tir.y + (GAME_GOAL_HEIGHT / 2)*0.75
        if(test.canshoot()):
            return SoccerAction(Vector2D(0,0), tir)
        else:
            return SoccerAction(Vector2D(0,0),Vector2D(0,0))
    def create_strategy(self):
        return Tirv()


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
        test = Outils(state, teamid, player)
        tir = state.get_goal_center(outils.IDTeamOp(teamid)) - player.position
        if(test.canshoot()):
            return SoccerAction(Vector2D(0,0), tir)
        else:
            return SoccerAction(Vector2D(0,0),Vector2D(0,0))
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
    def begin_battles(self,state,count,max_step):
        self.s1.begin_battles(state, count, max_step)
        self.s2.begin_battles(state, count, max_step)
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        move = self.s1.compute_strategy(state, player, teamid)
        shot = self.s2.compute_strategy(state, player, teamid)
        return SoccerAction(move.acceleration, shot.shoot)
    def create_strategy(self):
        return CompoStrat()
"""
Stratégie fonceur
Utilise stratégie AllerVersBallon
"""

class Fonceur(SoccerStrategy):
    def __init__(self):
        self.fonceur = CompoStrat(AllerVersBallon(), Tirv())
    def start_battle(self,state):
        pass
    def begin_battles(self,state,count,max_step):
        self.fonceur.begin_battles(state, count, max_step)
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
    def begin_battles(self,state,count,max_step):
        self.urgence.begin_battles(state, count, max_step)
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
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        out = Outils(state, teamid, player)
        distance = state.ball.position - state.get_goal_center(teamid)
        ball = state.ball.position - player.position
        if(out.nbadvbalbut(False) <= 1):
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
        pass
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        out = Outils(state, teamid, player)
        goal = state.get_goal_center(outils.IDTeamOp(teamid))
        yadv = out.jpro().y
        yme = player.position.y
        if(yadv > yme):
            dire = goal - player.position
            go = Vector2D.create_polar(dire.angle - 0.35, 2)
        else:           
            dire = goal - player.position
            go = Vector2D.create_polar(dire.angle + 0.35, 2)
        if(out.canshoot()):
            return SoccerAction(Vector2D(0,0), go)
        else:
            return SoccerAction(Vector2D(0,0), Vector2D(0,0))
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
    def start_battle(self,state):
        pass
    def begin_battles(self,state,count,max_step):
        self.aballon = 0
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        test = Outils(state, teamid, player)
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
        self.inter = CompoStrat(Interception(), Degagement())
        self.atck = CompoStrat(AllerVersBallon(), Esquive())
        self.fonceur = CompoStrat(AllerVersBallon(), Tirv())
        self.attente = random.random() * 100 + 150
    def start_battle(self,state):
        self.attente = random.random() * 100 + 150
    def begin_battles(self,state,count,max_step):
        self.attente = random.random() * 100 + 150
        self.inter.begin_battles(state, count, max_step)
        self.atck.begin_battles(state, count, max_step)
        self.fonceur.begin_battles(state, count, max_step)
        self.attente = random.random() * 100 + 150
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        test = Outils(state, teamid, player)
        dist = state.ball.position - player.position
        but = state.get_goal_center(outils.IDTeamOp(teamid)) - player.position
        butx = state.get_goal_center(outils.IDTeamOp(teamid)).x - player.position.x
        if(test.nbadvbalbut(True) == 1 and self.attente >= 1):
            self.attente = self.attente - 1                
            return self.inter.compute_strategy(state, player, teamid)
        if((test.nbadvbalbut(True) == 1 or self.attente < 1) and abs(butx) > 15):
            return self.atck.compute_strategy(state, player, teamid)
        else:
            return self.fonceur.compute_strategy(state,player,teamid)
    def create_strategy(self):
        return Intercepteur()

"""
Strategie d'intercepteur
Se place devant le ballon et le prend au joueur adverse V2.0
"""
class SurIntercepteur(SoccerStrategy):
    def __init__(self):
        self.inter = CompoStrat(Interception(), Degagement())
        self.atck = CompoStrat(AllerVersBallon(), Esquive())
        self.fonceur = CompoStrat(AllerVersBallon(), Tirv())
        self.attente = random.random() * 100 + 150
    def start_battle(self,state):
        self.attente = random.random() * 100 + 150
    def begin_battles(self,state,count,max_step):
        self.attente = random.random() * 100 + 150
        self.fonceur.begin_battles(state, count, max_step)
        self.inter.begin_battles(state, count, max_step)
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        test = Outils(state, teamid, player)
        dist = state.ball.position - player.position
        but = state.get_goal_center(outils.IDTeamOp(teamid)) - player.position
        butx = state.get_goal_center(outils.IDTeamOp(teamid)).x - player.position.x
        if(test.nbadvbalbut(True) == 2 and self.attente >= 1):
            self.attente = self.attente - 1            
            return self.inter.compute_strategy(state, player, teamid)
        if((test.nbadvbalbut(True) == 1 or self.attente < 1) and abs(butx) > 15):
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
        self.inter = CompoStrat(Interception(), Tirv())
        self.atck = CompoStrat(AllerVersBallon(), Esquive())
        self.fonceur = CompoStrat(AllerVersBallon(), Tirv())
        self.attente = random.random() * 100 + 150
    def start_battle(self,state):
        self.attente = random.random() * 100 + 150
    def begin_battles(self,state,count,max_step):
        self.attente = random.random() * 100 + 150
        self.fonceur.begin_battles(state, count, max_step)
        self.inter.begin_battles(state, count, max_step)
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        test = Outils(state, teamid, player)        
        dist = state.ball.position - player.position
        but = state.get_goal_center(outils.IDTeamOp(teamid)) - player.position
        butx = state.get_goal_center(outils.IDTeamOp(teamid)).x - player.position.x
        if(test.nbadvbalbut(True) == 4 and self.attente >= 1):
            self.attente = self.attente - 1            
            return self.inter.compute_strategy(state, player, teamid)
        if((test.nbadvbalbut(True) >= 1 or self.attente < 1) and abs(butx) > 15):
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
        self.revanche = CompoStrat(AllerVersBallon(), Tirv())
        self.adefendu = False
    def start_battle(self,state):
        pass
    def begin_battles(self, state,count,max_step):
        self.adefendu = False
        self.subti.begin_battles(state, count, max_step)
        self.revanche.begin_battles(state, count, max_step)
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        out = Outils(state, teamid, player)
        distance = out.distadvballon()
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
'''
Stratégie de mouvement
Suit l'allié le plus proche
'''
class Suivre(SoccerStrategy):
    def __init__(self):       
        pass
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        outil = Outils(state, teamid, player)
        loc1 = outil.moncopain().copy()
        loc2 = state.get_goal_center(teamid).copy()
        loc1.scale(0.9)
        loc2.scale(0.1)
        mouvement = loc1 + loc2 - player.position
        return SoccerAction(mouvement, Vector2D(0,0))
    def create_strategy(self):
        return Suivre()

'''
Stratégie d'attaque
Suit le possesseur du ballon, recupère le ballon s'il le perd
SI EQP BALLON ET + PROCHE => ATK
ELSE => SUIT
'''
class Follow(SoccerStrategy):
    def __init__(self):
        self.but = CompoStrat(AllerVersBallon(), Tirv())
        self.esquive = CompoStrat(AllerVersBallon(), Esquive())
        self.suivre = CompoStrat(Suivre(), Degagement())
    def start_battle(self,state):
        pass
    def begin_battles(self, state,count,max_step):
        self.but.begin_battles(state, count, max_step)
        self.esquive.begin_battles(state, count, max_step)
        self.suivre.begin_battles(state, count, max_step)
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        outil = Outils(state, teamid, player)
        allie = outil.jproall()
        dist = state.ball.position - player.position.copy()
        but = state.get_goal_center(outils.IDTeamOp(teamid)) - player.position.copy()
        dist2 = state.ball.position - allie
        if(not outil.equiperbal()):
            but = state.get_goal_center(outils.IDTeamOp(teamid)).x - player.position.copy().x
            if(abs(but) < 15 or outil.nbadvbalbut(True) < 1):
                return self.but.compute_strategy(state, player, teamid)
            else:
                return self.esquive.compute_strategy(state, player, teamid)
        else:
            return self.suivre.compute_strategy(state, player, teamid)
    def create_strategy(self):
        return Follow()

############################################################################################################################################################
############################################################################################################################################################        
############################################################################################################################################################ 
#OUTILS
############################################################################################################################################################
############################################################################################################################################################
############################################################################################################################################################
class Outils(SoccerState):
    def __init__(self, state, team, player):
        self.team = team
        self.player = player
        self.state = state       
    '''
    Donne la distance de l'adversaire le plus proche au ballon
    '''
    def distadvballon(self):
        dist = 9999       
        if(self.team == 2):
            for p in self.state.team1 :
                vec = self.state.ball.position - p.position
                dist = min(vec.norm, dist)
        else:
            for p in self.state.team2 :
                vec = self.state.ball.position - p.position
                dist = min(vec.norm, dist)
        return dist
        
    '''
    Donne la distance de l'allié (pas soi) le plus proche au ballon
    '''
    def distallballon(self):
        dist = 9999       
        if(self.team == 1):
            for p in self.state.team1 :
                if(self.player.position != p.position):
                    vec = self.state.ball.position - p.position
                    dist = min(vec.norm, dist)
        else:
            for p in self.state.team2 :
                if(self.player.position != p.position):
                    vec = self.state.ball.position - p.position
                    dist = min(vec.norm, dist)
        return dist
        
    '''
    Donne le nombre d'adversaire entre la balle et le but (ou le nombre d'allié si adv false)
    '''
    def nbadvbalbut(self, adv):
        nb = 0
        if((self.team == 2 and adv) or (self.team == 1 and not adv)):
            for p in self.state.team1 :
                if(adv):
                    distun = self.state.get_goal_center(outils.IDTeamOp(self.team)) - p.position 
                    distdeux = self.state.get_goal_center(outils.IDTeamOp(self.team)) - self.state.ball.position
                else:
                    distun = self.state.get_goal_center(self.team) - p.position 
                    distdeux = self.state.get_goal_center(self.team) - self.state.ball.position
                if(distun.norm < distdeux.norm):
                    nb = nb + 1
        else:
            for p in self.state.team2 :
                if(adv):
                    distun = self.state.get_goal_center(outils.IDTeamOp(self.team)) - p.position 
                    distdeux = self.state.get_goal_center(outils.IDTeamOp(self.team)) - self.state.ball.position
                else:
                    distun = self.state.get_goal_center(self.team) - p.position 
                    distdeux = self.state.get_goal_center(self.team) - self.state.ball.position
                if(distun.norm < distdeux.norm):
                    nb = nb+1
        return nb
    
    
    '''
    Donne la position du joueur adverse de moi des buts
    '''
    def jpro(self):
        dist = 9999
        vec = Vector2D(0,0)
        if(self.team == 2):
            for p in self.state.team1 :
                distmebut = self.state.get_goal_center(outils.IDTeamOp(self.team)) - self.player.position
                distluibut = self.state.get_goal_center(outils.IDTeamOp(self.team)) - p.position
                distmelui = p.position - self.player.position
                if(distluibut.norm < distmebut.norm and distmelui.norm < dist):
                    dist = distmelui.norm
                    vec = p.position
        else:
            for p in self.state.team2 :
                distmebut = self.state.get_goal_center(outils.IDTeamOp(self.team)) - self.player.position 
                distluibut = self.state.get_goal_center(outils.IDTeamOp(self.team)) - p.position
                distmelui = p.position - self.player.position
                if(distluibut.norm < distmebut.norm and distmelui.norm < dist):
                    dist = distmelui.norm
                    vec = p.position
        return vec.copy()
        
    '''
    Donne la position du joueur allié le plus proche des buts
    '''
    def jproall(self):
        dist = 9999
        vec = Vector2D(0,0)
        if(self.team == 1):
            for p in self.state.team1 :
                if(p.position != self.player.position):
                    distmebut = self.state.get_goal_center(outils.IDTeamOp(self.team)) - self.player.position
                    distluibut = self.state.get_goal_center(outils.IDTeamOp(self.team)) - p.position
                    distmelui = p.position - self.player.position
                    if(distluibut.norm < distmebut.norm and distmelui.norm < dist):
                        dist = distmelui.norm
                        vec = p.position
        else:
            for p in self.state.team2 :
                if(p.position != self.player.position):
                    distmebut = self.state.get_goal_center(outils.IDTeamOp(self.team)) - self.player.position 
                    distluibut = self.state.get_goal_center(outils.IDTeamOp(self.team)) - p.position
                    distmelui = p.position - self.player.position
                    if(distluibut.norm < distmebut.norm and distmelui.norm < dist):
                        dist = distmelui.norm
                        vec = p.position
        return vec.copy()
        
    '''
    Rend la position du joueur adverse le plus proche du ballon
    '''
    def jball(self):
        dist = 9999
        vec = Vector2D(0,0)
        if(self.team == 2):
            for p in self.state.team1 :
                distlui = state.ball.position - p.position
                if(distlui.norm < dist):
                    dist = distlui.norm
                    vec = p.position
        else:
            for p in self.state.team2 :
                distlui = state.ball.position - p.position
                if(distlui.norm < dist):
                    dist = distlui.norm
                    vec = p.position
        return vec.copy()
     
    
    '''
    Rend True si son équipe a le ballon, False sinon
    '''
    def equipeballo(self):
        dist = 9999
        for p in self.state.team1 :
                distballon = self.state.ball.position - p.position
                if(distballon.norm < dist):
                    dist1 = distballon.norm
                    dist = dist1
        dist = 9999
        for q in self.state.team2 :
                distballon2 = self.state.ball.position - q.position
                if(distballon2.norm < dist):
                    dist2 = distballon2.norm
                    dist = dist2
        if(((dist1 < dist2 and self.team == 1) or (dist1 > dist2 and self.team == 2)) and (dist2 < GAME_WIDTH * 0.09 or dist1 < GAME_WIDTH * 0.09)):
            return True
        else:
            return False

    '''
    Rend True si son équipe (pas lui) a le ballon, False sinon
    '''
    def equiperbal(self):
        dist = 9999
        for p in self.state.team1 :
                if(p.position != self.player.position):
                    distballon = self.state.ball.position - p.position
                    if(distballon.norm < dist):
                        dist1 = distballon.norm
                        dist = dist1
        dist = 9999
        for q in self.state.team2 :
                if(q.position != self.player.position):              
                    distballon2 = self.state.ball.position - q.position
                    if(distballon2.norm < dist):
                        dist2 = distballon2.norm
                        dist = dist2
        if(((dist1 < dist2 and self.team == 1) or (dist1 > dist2 and self.team == 2)) and (dist2 < GAME_WIDTH * 0.09 or dist1 < GAME_WIDTH * 0.09)):
            return True
        else:
            return False
        
    '''
    Rend True si le joueur peut tirer (par défault moi)
    '''
    def canshoot(self, player=None):
        if not player:
            player = self.player
        dist = self.state.ball.position - player.position
        if(dist.norm <= PLAYER_RADIUS + BALL_RADIUS):
            return True
        else:
            return False
        
    '''
    Rend la position du defenseur adverse le plus près des buts
    '''
    
    def getgoaladv(self):
        dist = 9999
        vec = Vector2D(0,0)
        if(self.team == 2):
            for p in self.state.team1 :
                distlui = self.state.get_goal_center(2)- p.position
                if(distlui.norm < dist):
                    dist = distlui.norm
                    vec = p.position
        else:
            for p in self.state.team2 :
                distlui = self.state.get_goal_center(1)- p.position
                if(distlui.norm < dist):
                    dist = distlui.norm
                    vec = p.position
        return vec.copy()
        
    '''
    Rend True si le goal adverse est dans la partie supérieur du terrain
    '''
    def goalsupmid(self):
        lesoutilsdelavie = Outils(self.state, self.team, self.player)
        goal = lesoutilsdelavie.getgoaladv()
        if(goal.y > 0.5 * GAME_HEIGHT):
            return True
        else:
            return False
            
    '''
    Donne la position du joueur allié le plus proche de MOI
    '''
    def moncopain(self):
        dist = 9999
        vec = Vector2D(0,0)
        if(self.team == 1):
            for p in self.state.team1 :
                if(p.position != self.player.position):
                    distmelui = p.position - self.player.position
                    if(distmelui.norm < dist):
                        dist = distmelui.norm
                        vec = p.position
        else:
            for p in self.state.team2 :
                if(p.position != self.player.position):
                    distmelui = p.position - self.player.position
                    if(distmelui.norm < dist):
                        dist = distmelui.norm
                        vec = p.position
        return vec.copy()