# -*- coding: utf-8 -*-

from sklearn.tree import DecisionTreeClassifier
from soccersimulator import TreeIA
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
    t=strats.Outils(state,teamid,state.get_player(teamid,playerid))
    return np.array([t.distball().norm, t.distadvballon(), t.distallballon(), t.quart(), t.hautterrain(), t.nbadvbalbut(True), t.nbadvbalbut(False), int(t.equipeballo()), int(t.equiperbal()), int(t.ballmoncote()), t.quartadv()])    
    #return np.array([f(state,teamid,playerid) for f in list_fun_features])

def Apprentissage():
    treeia=TreeIA(gen_feature_simple)
    treeia.learn(fn="botatk1.pkl")
    treeia.save("arbrebotatk1.pkl")    
    treeia.to_dot("arbrebotdatk1.dot")
    treeia=TreeIA(gen_feature_simple)
    treeia.learn(fn="botdef1.pkl")
    treeia.save("arbrebotdef1.pkl")
    treeia.to_dot("arbrebotdef1.dot")
    print "end"
    """ dot -Tpdf nom -o nom.pdf"""
    
#Apprentissage()