#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 14:42:49 2021

@author: cheikhtoure
"""
import altair as alt



def plot_Facies(data,Name='SHRIMPLIN',col_toDrop=['Formation','Well Name','RELPOS','NM_M2','Facies','IdxFacies']):
    
    '''
    inputs: data: pandas dataframe
            Name: (string) name of well
            col_toDrop: columns to drop
            
    output:
            altair plot
    
    '''
    
   
    
    A=data[data['Well Name']==Name].drop(col_toDrop,axis=1).melt('Depth',var_name='Category',value_name='valeur')
    char1=alt.Chart(A).mark_line().transform_filter(
    alt.datum.Category!='Facies_Name').encode(
            x=alt.X('valeur:Q', scale=alt.Scale(zero=False), axis=alt.Axis(title=None)),
            y=alt.Y('Depth:Q',scale=alt.Scale(zero=False,reverse=True)),
            color=alt.Color('Category:N',legend=None),
            column='Category:N',
            order='index:Q'
    ).properties(height=400, width=50, title='Well: '+ Name).resolve_scale(x='independent')
    
    
    
    facies_colors = ['#F4D03F', '#F5B041','#DC7633','#6E2C00','#1B4F72','#2E86C1', '#AED6F1', '#A569BD', '#196F3D']
    domain=['SS','CSiS','FSiS', 'SiSH','MS','WS','D','PS','BS']
    
    

    B=data[data['Well Name']==Name]
    char2=alt.Chart(B).mark_bar().encode(
          x=alt.X('count()',axis=alt.Axis(title=None,labels=False,grid=False)),
          y=alt.Y('Depth:Q',scale=alt.Scale(reverse=True), axis=alt.Axis(title=None,labels=False)),
          color=alt.Color('Facies_Name:N',scale=alt.Scale(domain=domain,range=facies_colors))
            ).properties(height=400, width=100)

    return alt.hconcat(char1,char2).resolve_scale(color='independent')

        
    