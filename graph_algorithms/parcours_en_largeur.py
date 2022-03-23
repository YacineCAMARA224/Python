# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 13:17:25 2021

@author: yacin
"""

import numpy as np
import pandas as pd

graph=pd.Series(np.array([["s", "v"], ["r", "w"], ["u", "w", "x"], ["t", "x", "y"], ["r"], ["s", "t", "x"], ["t", "u", "w", "y"], ["u", "x"]], dtype=object),\
                index=["r", "s", "t", "u", "v", "w", "x", "y"])

    
def parcours_en_largeur(graph, origin):
    couleur=pd.Series(np.array([], dtype=str), index=[])
    parent=pd.Series(np.array([], dtype=str), index=[])
    distance=pd.Series(np.array([], dtype=str), index=[])
    for i in range(0, graph.size):
        couleur=couleur.append(pd.Series(np.array(["blanc"], dtype=str), index=[graph.index[i]]))
        distance=distance.append(pd.Series({graph.index[i]: None}))
        parent=parent.append(pd.Series({graph.index[i]: None}))
    couleur[origin]="gris"
    distance[origin]=0
    sommets=np.array([origin], dtype=str)
    while np.size(sommets) > 0:
        sommet_actuel=sommets[0]
        for i in range(0, np.size(graph[sommet_actuel])):
            if couleur[graph[sommet_actuel][i]] == "blanc":
                couleur[graph[sommet_actuel][i]]="gris"
                distance[graph[sommet_actuel][i]]=distance[sommet_actuel]+1
                parent[graph[sommet_actuel][i]]=sommet_actuel
                sommets=np.append(sommets, graph[sommet_actuel][i])
        couleur[sommet_actuel]="noir"    
        sommets=np.delete(sommets, 0)
       
    return pd.Series({"couleur":couleur, "parent":parent, "distance":distance})
def trouver_chemin(s, v, parent):
    if s == v:
        print(s)
    elif parent[v] == None:
        print("Aucun chemin défini entre ", s, "et ", v)
    else:
        trouver_chemin(s, parent[v], parent)
        print("->", v)
def imprimer_chemin(graph, s, v):
    pl=parcours_en_largeur(graph, s)
    parent=pl["parent"]
    trouver_chemin(s, v, parent)

imprimer_chemin(graph, "s", "y")


