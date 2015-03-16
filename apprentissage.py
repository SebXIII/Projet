# -*- coding: utf-8 -*-

from sklearn.tree import DecisionTreeClassifier
import numpy as np
import pickle
import os
import strats

"""
Created on Mon Mar 16 11:12:23 2015

@author: 3300200
"""


#list_fun_features=[distance_ball,distance_mon_but,distance_autre_but,distance_ball_mon_but,distance_ball_autre_but]

def gen_feature_simple(state,teamid,playerid):
    t=strats.Outils(state,teamid,playerid)
    return np.array([t.distadvballon(), t.distallballon(), t.nbadvbalbut(True), t.nbadvbalbut(False), int(t.equipeballo()), int(t.equiperbal()), t.distball().norm, int(t.demoncote()), int(t.ballmoncote())])    
    #return np.array([f(state,teamid,playerid) for f in list_fun_features])
    
