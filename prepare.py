# This is my data preparation module for Anomaly Detection

import pandas as pd
import requests
import numpy as np
from datetime import timedelta, datetime

############## Cohorts and Curriculum Logs Prep ############################################

def initial_cohorts_prep(df):
    '''
    This function will take in my newly acquired cohorts table, and perform intial data preparation.
    I will be dropping the 'slack' column since it is redundant, as well as the 'deleted_at' since 
    all values are null.
    '''
    
    # Drop unneccessary columns
    df = df.drop(columns=['slack', 'deleted_at'])
    
    # convert all date columns to datetime...
    df['start_date'] = pd.to_datetime(df['start_date'])
    df['end_date'] = pd.to_datetime(df['end_date'])
    df['created_at'] = pd.to_datetime(df['created_at'])
    df['updated_at'] = pd.to_datetime(df['updated_at'])
    
    return df

def initial_curr_prep(df):
    '''
    This function will take in my newly acquired curriculum logs, and perform initial data preparation.
    At this stage, all I will be doing is converting 'date' to DateTime, and reseting it to the index.
    '''
    # convert 'date' to datetime
    df['date'] = pd.to_datetime(df['date'])
    # reset index to 'date'
    df = df.set_index(df['date'])
    
    return df

def curr_cohort_join(df1, df2, how='left'):
    '''
    This function will take in the newly prepped curriculum logs and cohorts DataFrames, and merge them.
    '''
    
    df = pd.merge(df1, df2, how='left', left_on='cohort_id', right_on='id')
    
    df = df.set_index(df['date'])
    
    return df

def initial_join_prep(df):
    '''
    This function will take in my newly merged pandas DataFrame of Curriculum Logs, and Cohorts. The intial prep will be 
    '''