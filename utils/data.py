#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 14:39:55 2021

@author: cheikhtoure
"""
"""
Created on Mon Jan 25 14:27:42 2021

@author: cheikhtoure
"""
import pandas as pd
from sklearn.model_selection import train_test_split



Facies_Name={1:'SS',2:'CSiS',3:'FSiS', 4:'SiSH',5:'MS',6:'WS',7:'D',8:'PS',9:'BS'}
def get_data(url='facies_data.csv', Facies_Name=Facies_Name):
    '''
    Parameters
    ----------
    url : STRING, optional
        DESCRIPTION. The default is './facies_datat.csv'.
        
   Facies_Name: LIST,   Facies Name     

    Returns
    -------
    df: pandas dataframe

    '''
    df=pd.read_csv(url)
    df=df.drop_duplicates()
    
    assert ('NM_M' in df.columns)
    df=pd.get_dummies(df,columns=['NM_M'],drop_first=True,prefix_sep='')
    df['Facies_Name']=df.Facies.map(lambda v:Facies_Name[v])
    
    df['IdxFacies']=df['Facies']-1

    
    return df
    



def split_data(df):
    '''

    Parameters
    ----------
    df : Pandas Dataframe
        

    Returns
    -------
    df_train : Pandas Dataframe
        Train.
    df_test : Pandas Dataframe
        Test.
    df_val : Pandas Dataframe
        Validation

    '''
    
    assert( 'SHANKLE' in df['Well Name'].unique())
    df_val=df[df['Well Name']=='SHANKLE']
    


    df_train,df_test=train_test_split(df[df['Well Name']!='SHANKLE'],test_size=0.1,\
                                      stratify=df[df['Well Name']!='SHANKLE']['IdxFacies'],random_state=0)

    df_train.name='df_train'
    df_test.name='df_test'
    df_val.name='df_val'
    
    return df_train,df_test, df_val



    
    
    
    
    