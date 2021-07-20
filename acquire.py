# This is my Anomaly Detection Date Acquisition module

import pandas as pd
import numpy as np
import os
from env import host, user, password

# general framework / template
def get_connection(db, user=user, host=host, password=password):
    '''
    This function uses my env file to create a connection url to access
    the Codeup database.
    '''
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

def get_cohort_data():
    df = pd.read_sql('SELECT * FROM cohorts;', get_connection('curriculum_logs'))
    return df.set_index('customer_id')