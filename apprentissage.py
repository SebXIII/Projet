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
    t=strats.Outils(state,teamid,state.get_player(teamid,playerid))
    return np.array([t.distadvballon(), t.distallballon(), t.nbadvbalbut(True), t.nbadvbalbut(False), int(t.equipeballo()), int(t.equiperbal()), t.distball().norm, int(t.demoncote()), int(t.ballmoncote())])    
    #return np.array([f(state,teamid,playerid) for f in list_fun_features])

def load_interact(fn):
    states=[]
    with open(fn,"rb") as f:
        while(1):
            try:
                states+=pickle.load(f)
            except EOFError:
                break
    return states

# Apprendre un arbre a partir de la sortie de load_interact, le stocker dans le fichier fn au besoin
def learn_tree(states,fn=None):
    train_set=np.array([gen_feature_simple(s[0],s[1],s[2]) for s in states])
    label_set=np.array([s[3] for s in states])
    tree=DecisionTreeClassifier()
    tree.max_depth=5
    tree.fit(train_set,label_set)
    if fn:
        with open(fn,"wb") as f:
            pickle.dump(tree,f,-1)
    return tree

def learn():
    states=load_interact("tent3.pkl")
    learn_tree(states,"first_tree.pkl")
    
