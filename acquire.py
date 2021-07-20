# This is my Anomaly Detection Date Acquisition module

import pandas as pd
import numpy as np
import os
from env import host, user, password

############################## general framework / template ###############################
def get_connection(db, user=user, host=host, password=password):
    '''
    This function uses my env file to create a connection url to access
    the Codeup database.
    '''
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'


############################ Curriculum Logs ###############################################
def new_cohort_data():
    df = pd.read_sql('SELECT * FROM cohorts;', get_connection('curriculum_logs'))
    return df

def get_cohort_data():
    if os.path.isfile('cohorts.csv'):
        # If csv file exists read in data from csv file.
        df = pd.read_csv('cohorts.csv', index_col=0)
        
    else:
        # Read fresh data from db into a DataFrame
        df = new_cohort_data()
        # Cache data
        df.to_csv('cohorts.csv')

    return df  

def get_curriculum_logs():
    # create column names for the data
    colnames = ['date', 'endpoint', 'user_id', 'cohort_id', 'source_ip']
    # read the data into a pandas DataFrame
    df = pd.read_csv("anonymized-curriculum-access-07-2021.txt", 
                     sep="\s", 
                     header=None, 
                     names = colnames, 
                     usecols=[0, 2, 3, 4, 5])
    
    return df

########################### Grocery Data ###################################################

def new_groceries():
    '''
    This functions reads in three different csv files as pandas DataFrames, and merges them
    into one df. It drops unnamed columns. Cannot use with other dataframes without changing 
    the name of the csv files, and hyperparameters of how/on the tables are merged
    '''
    
    items_df = pd.read_csv('grocery_items.csv')
    stores_df = pd.read_csv('grocery_stores.csv')
    sales_df = pd.read_csv('grocery_sales.csv')
    sales_stores_df = pd.merge(sales_df, stores_df, left_on='store', right_on='store_id', how='left')
    sales_stores_items_df = pd.merge(sales_stores_df, items_df, left_on='item', right_on='item_id', how='left')
    sales_stores_items_df = sales_stores_items_df.drop(columns=['Unnamed: 0_x', 'Unnamed: 0_y', 'Unnamed: 0', 'store', 'item'])
    
    return sales_stores_items_df

def get_groceries():
    '''
    This function operates on top of the new_groceries function. It first searches locally for a csv file.
    If there is a local csv, it writes it into a pandas DataFrame. If there is no local csv, this function then
    calls the new_groceries function, and writes that df to a local csv.
    '''
    if os.path.isfile('sales_stores_items.csv'):
        # If csv file exists read in data from csv file.
        df = pd.read_csv('sales_stores_items.csv', index_col=0)
        
    else:
        # Read fresh data from db into a DataFrame
        df = new_groceries()
        # Cache data
        df.to_csv('sales_stores_items.csv')

    return df

