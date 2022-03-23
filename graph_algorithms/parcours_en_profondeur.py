# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 13:17:25 2021

@author: yacin
"""

import numpy as np
import pandas as pd

graph=pd.Series(np.array([["s", "v"], ["r", "w"], ["u", "w", "x"], ["t", "x", "y"], ["r"], ["s", "t", "x"], ["t", "u", "w", "y"], ["u", "x"]], dtype=object),\
                index=["r", "s", "t", "u", "v", "w", "x", "y"])

    
def parcours_en_profondeur(graph, date=0):
    couleur=pd.Series(np.array([], dtype=str), index=[])
    parent=pd.Series(np.array([], dtype=str), index=[])
    debut=pd.Series(np.array([], dtype=str), index=[])
    fin=pd.Series(np.array([], dtype=str), index=[])
    for i in range(0, graph.size):
        couleur=couleur.append(pd.Series(np.array(["blanc"], dtype=str), index=[graph.index[i]]))
        debut=debut.append(pd.Series({graph.index[i]: None}))
        fin=fin.append(pd.Series({graph.index[i]: None}))
        parent=parent.append(pd.Series({graph.index[i]: None}))
    for i in range(0, graph.size):
        if couleur[graph.index[i]] == "blanc":
            visiter_pp(graph.index[i], graph, couleur, parent, debut, fin, date)
            
    return pd.Series({"couleur":couleur, "parent":parent, "debut":debut, "fin":fin})

def visiter_pp(sommet, graph, couleur, parent, debut, fin, date):
    couleur[sommet] = "gris"
    date+=1
    debut[sommet]=date
    for i in range(0, np.size(graph[sommet])):
        if couleur[graph[sommet][i]] == "blanc":
            parent[graph[sommet][i]]=sommet
            visiter_pp(graph[sommet][i], graph, couleur, parent, debut, fin, date)
    date+=1
    fin[sommet]=date
    couleur[sommet]="noir"
    
def trouver_chemin(s, v, parent):
    if s == v:
        print(s)
    elif parent[v] == None:
        print("Aucun chemin défini entre ", s, "et ", v)
    else:
        trouver_chemin(s, parent[v], parent)
        print("->", v)
def imprimer_chemin(graph, s, v):
    p_p=parcours_en_profondeur(graph)
    parent=p_p["parent"]
    trouver_chemin(s, v, parent)

imprimer_chemin(graph, "s", "y")


