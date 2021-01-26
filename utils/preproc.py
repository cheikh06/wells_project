#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 14:54:32 2021

@author: cheikhtoure
"""

from torch.utils.data import   TensorDataset
from imblearn.over_sampling import RandomOverSampler
from sklearn.preprocessing import StandardScaler
import torch
import numpy as np

def shift(seq, n=0): 
    a = n % len(seq) 
    return np.array(seq[-a:]+seq[:-a])



def padding_shift(inp):
    '''
    Cette fonction prend en entrée, une liste et fait le shift padding dont 
    j'ai parlé tout à l'heure.
    
    '''
    tampon=inp*np.ones((len(inp),len(inp)))
    
    for i in range(len(tampon)):
        tampon[i,:]=shift(list(tampon[i,:]),n=i)
    return tampon  




def preproc_data(df, features=['GR', 'ILD_log10', 'DeltaPHI', 'PHIND', 'NM_M2', 'RELPOS'],labels='IdxFacies',sampling=False):
    
    '''
    inputs:
            df: dataframe
            features: variable for training
            sampling (optional) default False :if True RandomOverSampling 
    outputs:
            Tensor Dataset
    
    
    '''
    
    #df['IdxFacies']=df['Facies']-1
    
    if (df.name=='df_train') & (sampling):
        # RandomOverSampling (imbalanced class)
        preproc=StandardScaler().fit_transform(df[features])
        y=df['IdxFacies'].values
        preproc,y=RandomOverSampler(random_state=0).fit_resample(preproc,y)
        
        #padding shift
        preproc=torch.tensor([padding_shift(v) for v in preproc]).unsqueeze(1)
        y=torch.tensor(y).long()
        print(1)
        
        return TensorDataset(preproc,y)
        
        
        
    else:
        preproc=StandardScaler().fit_transform(df[features])
        preproc=torch.tensor([padding_shift(v) for v in preproc]).unsqueeze(1)
        y=torch.tensor(df['IdxFacies'].values).long()
        
        
    
        return TensorDataset(preproc,y)
    
    