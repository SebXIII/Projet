# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 16:47:36 2015

@author: 3300200
"""
from soccersimulator import Vector2D, SoccerBattle, SoccerPlayer, SoccerTeam, SoccerAction, SoccerStrategy
from soccersimulator import PygletObserver,ConsoleListener,LogListener
from soccersimulator import PLAYER_RADIUS, BALL_RADIUS
import outils
import random
import pdb
 
def IDTeamOp(id):
    if (id == 1):
        return 2  
    else:
        return 1
