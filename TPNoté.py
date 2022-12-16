#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 08:17:38 2022

@author: virgile broillet p2103804 & marie graff p2101141

TP Noté Statistiques

"""

import numpy as np
import matplotlib.pyplot as plt 
import pandas as pan
import statsmodels.api as sm 
import scipy.stats as st

Air=pan.read_csv('http://tinyurl.com/y39an7ef/Data100461.csv', sep="\t", na_values="-")

#Séparateurs pour cacher les exercices non voulus :
#'''


print('############## EXERCICE A ##############')
print(" ")

print("Les index sont des variables quantitatives discrètes, les dates sont des variables ordinales, car celles-ci sont ranger par ordre croissant, et l'intégralité des mesures sont des variables quantitatives continues, car elles sont sur l'interval ]-∞, +∞[")
print(" ")
newAir=Air.dropna()

print("nombre de Jours d'étude :",len(Air))

print("en tout il y a eu ",max(newAir.index)+1,"jours où toutes les valeurs on été mesuré")
print(" ")

x = newAir['Sud lyonnais / Feyzin ZI Benzène']
z = newAir['Lyon Centre Benzène']
y = newAir['Date']

plt.plot(y,x,color="green")
plt.plot(y,z,color="red")
plt.show()

FEYZIN_BENZÈNE_HORS_NAN = newAir['Sud lyonnais / Feyzin ZI Benzène']
print("La moyenne empirique hors jour de non-observation du Benzène à Feyzin : ",round(np.mean(FEYZIN_BENZÈNE_HORS_NAN), 2))
print(" ")
print("La variance empirique hors jour de non-observation du Benzène à Feyzin : ",round(np.var(FEYZIN_BENZÈNE_HORS_NAN), 2))
print(" ")
Q3 = np.percentile(FEYZIN_BENZÈNE_HORS_NAN, 75)
print("Le quartile à 75%, hors jour de non-observation du Benzène à Feyzin : ",round(Q3,2))

i=2
compteur=2
valeur=49
valeur1 = 0;valeur2 = 0;valeur3 = 0;valeur4 = 0;valeur5 = 0;valeur6 = 0;valeur7 = 0;valeur8 = 0;valeur9 = 0;valeur10 = 0;valeur11 = 0;valeur12 = 0;
print("il y a : 49 non-observation(s) pour la semaine : 1")
liste_Lyon_benzène = []
liste_Lyon_so2 = []
liste_feyzin_so2 = []
liste_feyzin_benzène = []
liste_feyzin_ethane = []
liste_feyzin_propane = []
liste_feyzin_propène = []
liste_SF_co2 = []
liste_vernaison_benzène = []
liste_vernaison_ethane = []
liste_vernaison_propane = []
liste_vernaison_propène = []
moyenn_geo = []

geo_feyzin_benzen=[]
geo_feyzin_ethane=[]
geo_feyzin_propane=[]
geo_feyzin_propene=[]
geo_feyzin_benzen=[]
geo_vernaison_benzen=[]
geo_vernaison_ethane=[]
geo_vernaison_propane=[]
geo_vernaison_propene=[]

geo_feyzin_benzen.append(float('nan'))
geo_feyzin_ethane.append(float('nan'))
geo_feyzin_propane.append(float('nan'))
geo_feyzin_propene.append(float('nan'))
geo_vernaison_benzen.append(float('nan'))
geo_vernaison_ethane.append(float('nan'))
geo_vernaison_propane.append(float('nan'))
geo_vernaison_propene.append(float('nan'))


while i < max(Air.index):  
    ligne = Air.iloc[[i+1,i+2,i+3,i+4,i+5,i+6,i+7]]
    print("il y a : ",ligne.isnull().sum().sum()," non-observation(s) pour la semaine : ",compteur)
    valeur = valeur + ligne.isnull().sum().sum()
    
    if np.isnan(ligne.loc[i+1, "Lyon Centre Benzène"]):
        if np.isnan(ligne.loc[i+2, "Lyon Centre Benzène"]):
            if np.isnan(ligne.loc[i+3, "Lyon Centre Benzène"]):
                if np.isnan(ligne.loc[i+4, "Lyon Centre Benzène"]):
                    if np.isnan(ligne.loc[i+5, "Lyon Centre Benzène"]):
                        if np.isnan(ligne.loc[i+6, "Lyon Centre Benzène"]):
                            if np.isnan(ligne.loc[i+7, "Lyon Centre Benzène"]):
                                valeur1 = 1
                                liste_Lyon_benzène.append(compteur)
    
    if np.isnan(ligne.loc[i+1, "Lyon Centre Dioxyde soufre"]):
        if np.isnan(ligne.loc[i+2, "Lyon Centre Dioxyde soufre"]):
            if np.isnan(ligne.loc[i+3, "Lyon Centre Dioxyde soufre"]):
                if np.isnan(ligne.loc[i+4, "Lyon Centre Dioxyde soufre"]):
                    if np.isnan(ligne.loc[i+5, "Lyon Centre Dioxyde soufre"]):
                        if np.isnan(ligne.loc[i+6, "Lyon Centre Dioxyde soufre"]):
                            if np.isnan(ligne.loc[i+7, "Lyon Centre Dioxyde soufre"]):
                                valeur2 = 2
                                liste_Lyon_so2.append(compteur)

    if np.isnan(ligne.loc[i+1, "Sud lyonnais / Feyzin ZI Dioxyde soufre"]):
        if np.isnan(ligne.loc[i+2, "Sud lyonnais / Feyzin ZI Dioxyde soufre"]):
            if np.isnan(ligne.loc[i+3, "Sud lyonnais / Feyzin ZI Dioxyde soufre"]):
                if np.isnan(ligne.loc[i+4, "Sud lyonnais / Feyzin ZI Dioxyde soufre"]):
                    if np.isnan(ligne.loc[i+5, "Sud lyonnais / Feyzin ZI Dioxyde soufre"]):
                        if np.isnan(ligne.loc[i+6, "Sud lyonnais / Feyzin ZI Dioxyde soufre"]):
                            if np.isnan(ligne.loc[i+7, "Sud lyonnais / Feyzin ZI Dioxyde soufre"]):
                                valeur3 = 3
                                liste_feyzin_so2.append(compteur)
                                
    if np.isnan(ligne.loc[i+1, "Sud lyonnais / Feyzin ZI Benzène"]):
        if np.isnan(ligne.loc[i+2, "Sud lyonnais / Feyzin ZI Benzène"]):
            if np.isnan(ligne.loc[i+3, "Sud lyonnais / Feyzin ZI Benzène"]):
                if np.isnan(ligne.loc[i+4, "Sud lyonnais / Feyzin ZI Benzène"]):
                    if np.isnan(ligne.loc[i+5, "Sud lyonnais / Feyzin ZI Benzène"]):
                        if np.isnan(ligne.loc[i+6, "Sud lyonnais / Feyzin ZI Benzène"]):
                            if np.isnan(ligne.loc[i+7, "Sud lyonnais / Feyzin ZI Benzène"]):
                                valeur4 = 4
                                liste_feyzin_benzène.append(compteur)
    
    if np.isnan(ligne.loc[i+1, "Sud lyonnais / Feyzin ZI Ethane"]):
        if np.isnan(ligne.loc[i+2, "Sud lyonnais / Feyzin ZI Ethane"]):
            if np.isnan(ligne.loc[i+3, "Sud lyonnais / Feyzin ZI Ethane"]):
                if np.isnan(ligne.loc[i+4, "Sud lyonnais / Feyzin ZI Ethane"]):
                    if np.isnan(ligne.loc[i+5, "Sud lyonnais / Feyzin ZI Ethane"]):
                        if np.isnan(ligne.loc[i+6, "Sud lyonnais / Feyzin ZI Ethane"]):
                            if np.isnan(ligne.loc[i+7, "Sud lyonnais / Feyzin ZI Ethane"]):
                                valeur5 = 5
                                liste_feyzin_ethane.append(compteur)
                                
    if np.isnan(ligne.loc[i+1, "Sud lyonnais / Feyzin ZI Propane"]):
        if np.isnan(ligne.loc[i+2, "Sud lyonnais / Feyzin ZI Propane"]):
            if np.isnan(ligne.loc[i+3, "Sud lyonnais / Feyzin ZI Propane"]):
                if np.isnan(ligne.loc[i+4, "Sud lyonnais / Feyzin ZI Propane"]):
                    if np.isnan(ligne.loc[i+5, "Sud lyonnais / Feyzin ZI Propane"]):
                        if np.isnan(ligne.loc[i+6, "Sud lyonnais / Feyzin ZI Propane"]):
                            if np.isnan(ligne.loc[i+7, "Sud lyonnais / Feyzin ZI Propane"]):
                                valeur6 = 6
                                liste_feyzin_propane.append(compteur)
    
    if np.isnan(ligne.loc[i+1, "Sud lyonnais / Feyzin ZI Propène"]):
        if np.isnan(ligne.loc[i+2, "Sud lyonnais / Feyzin ZI Propène"]):
            if np.isnan(ligne.loc[i+3, "Sud lyonnais / Feyzin ZI Propène"]):
                if np.isnan(ligne.loc[i+4, "Sud lyonnais / Feyzin ZI Propène"]):
                    if np.isnan(ligne.loc[i+5, "Sud lyonnais / Feyzin ZI Propène"]):
                        if np.isnan(ligne.loc[i+6, "Sud lyonnais / Feyzin ZI Propène"]):
                            if np.isnan(ligne.loc[i+7, "Sud lyonnais / Feyzin ZI Propène"]):
                                valeur7 = 7
                                liste_feyzin_propène.append(compteur)
                                
    if np.isnan(ligne.loc[i+1, "sud lyonnais / Saint-Fons Dioxyde soufre"]):
        if np.isnan(ligne.loc[i+2, "sud lyonnais / Saint-Fons Dioxyde soufre"]):
            if np.isnan(ligne.loc[i+3, "sud lyonnais / Saint-Fons Dioxyde soufre"]):
                if np.isnan(ligne.loc[i+4, "sud lyonnais / Saint-Fons Dioxyde soufre"]):
                    if np.isnan(ligne.loc[i+5, "sud lyonnais / Saint-Fons Dioxyde soufre"]):
                        if np.isnan(ligne.loc[i+6, "sud lyonnais / Saint-Fons Dioxyde soufre"]):
                            if np.isnan(ligne.loc[i+7, "sud lyonnais / Saint-Fons Dioxyde soufre"]):
                                valeur8 = 8
                                liste_SF_co2.append(compteur)

    if np.isnan(ligne.loc[i+1, "Vernaison ZI Benzène"]):
        if np.isnan(ligne.loc[i+2, "Vernaison ZI Benzène"]):
            if np.isnan(ligne.loc[i+3, "Vernaison ZI Benzène"]):
                if np.isnan(ligne.loc[i+4, "Vernaison ZI Benzène"]):
                    if np.isnan(ligne.loc[i+5, "Vernaison ZI Benzène"]):
                        if np.isnan(ligne.loc[i+6, "Vernaison ZI Benzène"]):
                            if np.isnan(ligne.loc[i+7, "Vernaison ZI Benzène"]):
                                valeur9 = 9
                                liste_vernaison_benzène.append(compteur)
                                
    if np.isnan(ligne.loc[i+1, "Vernaison ZI Ethane"]):
        if np.isnan(ligne.loc[i+2, "Vernaison ZI Ethane"]):
            if np.isnan(ligne.loc[i+3, "Vernaison ZI Ethane"]):
                if np.isnan(ligne.loc[i+4, "Vernaison ZI Ethane"]):
                    if np.isnan(ligne.loc[i+5, "Vernaison ZI Ethane"]):
                        if np.isnan(ligne.loc[i+6, "Vernaison ZI Ethane"]):
                            if np.isnan(ligne.loc[i+7, "Vernaison ZI Ethane"]):
                                valeur10 = 10
                                liste_vernaison_ethane.append(compteur)
                                
    if np.isnan(ligne.loc[i+1, "Vernaison ZI Propane"]):
        if np.isnan(ligne.loc[i+2, "Vernaison ZI Propane"]):
            if np.isnan(ligne.loc[i+3, "Vernaison ZI Propane"]):
                if np.isnan(ligne.loc[i+4, "Vernaison ZI Propane"]):
                    if np.isnan(ligne.loc[i+5, "Vernaison ZI Propane"]):
                        if np.isnan(ligne.loc[i+6, "Vernaison ZI Propane"]):
                            if np.isnan(ligne.loc[i+7, "Vernaison ZI Propane"]):
                                valeur11 = 11
                                liste_vernaison_propane.append(compteur)
                                
    if np.isnan(ligne.loc[i+1, "Vernaison ZI Propène"]):
        if np.isnan(ligne.loc[i+2, "Vernaison ZI Propène"]):
            if np.isnan(ligne.loc[i+3, "Vernaison ZI Propène"]):
                if np.isnan(ligne.loc[i+4, "Vernaison ZI Propène"]):
                    if np.isnan(ligne.loc[i+5, "Vernaison ZI Propène"]):
                        if np.isnan(ligne.loc[i+6, "Vernaison ZI Propène"]):
                            if np.isnan(ligne.loc[i+7, "Vernaison ZI Propène"]):
                                valeur12 = 12
                                liste_vernaison_propène.append(compteur)
         

    val=Air["Sud lyonnais / Feyzin ZI Benzène"]
    geo_feyzin_benzen.append(st.gmean([val[i+1],val[i+2],val[i+3],val[i+4],val[i+5],val[i+6],val[i+7]]))
    
    val=Air["Sud lyonnais / Feyzin ZI Ethane"]
    geo_feyzin_ethane.append(st.gmean([val[i+1],val[i+2],val[i+3],val[i+4],val[i+5],val[i+6],val[i+7]]))
    
    val=Air["Sud lyonnais / Feyzin ZI Propane"]
    geo_feyzin_propane.append(st.gmean([val[i+1],val[i+2],val[i+3],val[i+4],val[i+5],val[i+6],val[i+7]]))
    
    val=Air["Sud lyonnais / Feyzin ZI Propène"]
    geo_feyzin_propene.append(st.gmean([val[i+1],val[i+2],val[i+3],val[i+4],val[i+5],val[i+6],val[i+7]]))
    
    val=Air["Vernaison ZI Benzène"]
    geo_vernaison_benzen.append(st.gmean([val[i+1],val[i+2],val[i+3],val[i+4],val[i+5],val[i+6],val[i+7]]))
    
    val=Air["Vernaison ZI Ethane"]
    geo_vernaison_ethane.append(st.gmean([val[i+1],val[i+2],val[i+3],val[i+4],val[i+5],val[i+6],val[i+7]]))
    
    val=Air["Vernaison ZI Propane"]
    geo_vernaison_propane.append(st.gmean([val[i+1],val[i+2],val[i+3],val[i+4],val[i+5],val[i+6],val[i+7]]))
    
    val=Air["Vernaison ZI Propène"]
    geo_vernaison_propene.append(st.gmean([val[i+1],val[i+2],val[i+3],val[i+4],val[i+5],val[i+6],val[i+7]]))
    
    i=i+7
    compteur=compteur+1
    
    
if valeur1 == 1:
    print(" ")
    print("Il n'y a aucune mesure de Benzène à Lyon Centre durant les semaines : ",liste_Lyon_benzène)
if valeur2 == 2:
    print(" ")
    print("Il n'y a aucune mesure de Soufre à Lyon Centre durant les semaines : ",liste_Lyon_so2)
if valeur3 == 3:
    print(" ")
    print("Il n'y a aucune mesure de Soufre à Feyzin ZI durant les semaines : ",liste_feyzin_so2)
if valeur4 == 4:
    print(" ")
    print("Il n'y a aucune mesure de Benzène à Feyzin ZI durant les semaines : ",liste_feyzin_benzène)
if valeur5 == 5:
    print(" ")
    print("Il n'y a aucune mesure d'Ethane à Feyzin ZI durant les semaines : ",liste_feyzin_ethane)
if valeur6 == 6:
    print(" ")
    print("Il n'y a aucune mesure de Propane à Feyzin ZI durant les semaines : ",liste_feyzin_propane)
if valeur7 == 7:
    print(" ")
    print("Il n'y a aucune mesure de Propène à Feyzin ZI durant les semaines : ",liste_feyzin_propène)
if valeur8 == 8:
    print(" ")
    print("Il n'y a aucune mesure de Dioxyde de Soufre à Feyzin ZI durant les semaines : ",liste_SF_co2)
if valeur9 == 9:
    print(" ")
    print("Il n'y a aucune mesure de Benzène à Vernaison ZI durant les semaines : ",liste_vernaison_benzène)
if valeur10 == 10:
    print(" ")
    print("Il n'y a aucune mesure d'Ethane à Vernaison ZI durant les semaines : ",liste_vernaison_ethane)
if valeur11 == 11:
    print(" ")
    print("Il n'y a aucune mesure de Propane à Vernaison ZI durant les semaines : ",liste_vernaison_propane)
if valeur12 == 12:
    print(" ")
    print("Il n'y a aucune mesure de Propène à Vernaison ZI durant les semaines : ",liste_vernaison_propène)
        
print("En tous, il y a un total de ",valeur," non-observation(s)")

'''
Il faut créer un dataframe composé des semaines 2 à 16 + la semaine 18; puis des semaines 20 à 38; puis des semaines 40 à 50 + 52 + 53
Donc des Index 3 à 107 + 115 à 121 + 129 à 261 + 269 à 345 + 353 à 366 de Air
'''
nb = 1
ar = []
while nb < 106:
    ar.append(nb)
    nb=nb+1

    

dfh = pan.DataFrame(geo_feyzin_benzen, index = ar, columns = ['Moyenne Géométrique Fezyin Benzene'])
dfh.insert(1, 'M-Gé Fezyin Ethane', geo_feyzin_ethane) #insertion des colonnes supplémentaires
dfh.insert(2, 'M-Gé Fezyin Propane', geo_feyzin_propane)
dfh.insert(3, 'M-Gé Fezyin Propene', geo_feyzin_propene)
dfh.insert(4, 'M-Gé Vernaison Benzène', geo_vernaison_benzen)
dfh.insert(5, 'M-Gé Vernaison Ethane', geo_vernaison_ethane)
dfh.insert(6, 'M-Gé Vernaison Propane', geo_vernaison_propane)
dfh.insert(7, 'M-Gé Vernaison Propene', geo_vernaison_propene)

print(" ")
print("Le DataFrame 'dfh' a été crée, l'index représente la i-ème semaine, puis on trouve les valeurs des moyennes géométriques des 8 mesures complète.")


#'''
#Séparateurs pour cacher les exercices non voulus :
#'''

print(" ")
print('############## EXERCICE B ##############')
print(" ")
