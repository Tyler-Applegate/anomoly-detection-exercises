# This is my Data Exploration Module for Anomoly Detection

# Imports
import pandas as pd
import numpy as np
from pydataset import data
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import display, display_html


# This function will work on a single column

def get_lower_and_upper_bounds(df, col, k=1.5):
    '''
    This function takes in a dataframe and returns the upper and lower bounds based on the argument of k
    '''
    # Find the lower and upper quartiles
    q_25, q_75 = df[col].quantile([0.25, 0.75])
    # Find the Inner Quartile Range
    q_iqr = q_75 - q_25
    # Find the Upper Bound
    q_upper = q_75 + (k * q_iqr)
    # Find the Lower Bound
    q_lower = q_25 - (k * q_iqr)
    # Identify outliers
    outliers = df[df[col] < q_lower]
    outliers = df[df[col] > q_upper]
    
    return q_lower, q_upper, outliers

############## Child Functions for IQR / Outliers ###########################

        
def get_plot_iqr_stats(df, col, k=1.5):
    '''
    This function will take in a pandas Series and plot a histogram and boxplot, with whiskers set based on value of k.
    '''
    
    # Find the lower and upper quartiles
    q_25, q_75 = df[col].quantile([0.25, 0.75])
    # Find the Inner Quartile Range
    q_iqr = q_75 - q_25
    # Find the Upper Bound
    q_upper = q_75 + (k * q_iqr)
    # Find the Lower Bound
    q_lower = q_25 - (k * q_iqr)
    # Identify outliers
    outliers_lower = df[df[col] < q_lower]
    outliers_upper = df[df[col] > q_upper]
    outliers_all = pd.concat([outliers_lower, outliers_upper], axis=0)
    
    print(f'''
{col}

K: {k}
IQR: {q_iqr}
Lower Fence: {q_lower}
Upper Fence: {q_upper}
''')
    print(f'{col} Lower Outliers')
    display(outliers_lower)
    print(f'{col} Upper Outliers')
    display(outliers_upper)
    print(f'{col} All Outliers')
    display(outliers_all)
    
    plt.figure(figsize=(16,4))
    plt.subplot(1, 2, 1)
    sns.histplot(data = df, x = col, kde=True)
    plt.axvline(x = q_lower, color = 'orange')
    plt.axvline(x = q_upper, color= 'orange')
    plt.title(col)
    plt.subplot(1, 2, 2)
    sns.boxplot(x=df[col], data=df, whis=k)
    plt.title(col)
    plt.show()

        


def whole_df_iqr(df, k=1.5):
    col_list = list(df.select_dtypes(include=['int', 'float'], exclude='O'))
    
    for col in col_list:
        get_plot_iqr_stats(df, col, k=k)
        
    return df.info()


################ zscore functions ###########################################

def add_zscore_cols(df):
    
    col_list = list(df.select_dtypes(include=['int', 'float'], exclude='O'))
    
    for col in col_list:
        z_scores = pd.Series((df[col] - df[col].mean()) / df[col].std())
        df[f'{col}_zscore'] = z_scores
        
    return df
    

def get_zscore_info(df, sigma=2):
    
    col_list = list(df.select_dtypes(include=['int', 'float'], exclude='O'))
    
    for col in col_list:
        
    
    
########################## Way too Rabbit-Holey ##############################

# This function will take in an entire dataframe, and operate on a list of columns...

def get_low_and_up_bounds_df(df, k=1.5, sort_values=False):
    '''
    This function takes in a pandas dataframe, list of columns, and k value, and will print out upper and lower bounds for each column.
    It takes in a default argument of the col_list being all numeric columns, and the k value=1.5
    '''
    col_list=list(df.select_dtypes(include=['int', 'float'], exclude='O'))
    
    if sort_values == False:
                                   
        for col in col_list:

            # Find the lower and upper quartiles
            q_25, q_75 = df[col].quantile([0.25, 0.75])
            # Find the Inner Quartile Range
            q_iqr = q_75 - q_25
            # Find the Upper Bound
            q_upper = q_75 + (k * q_iqr)
            # Find the Lower Bound
            q_lower = q_25 - (k * q_iqr)
            # Identify outliers
            outliers_lower = df[df[col] < q_lower]
            outliers_upper = df[df[col] > q_upper]
            outliers_all = pd.concat([outliers_lower, outliers_upper], axis=0)
            
            print('')
            print(col)
            print(f'K: {k}')
            print(f'Lower Fence: {q_lower}')
            print(f'Upper Fence: {q_upper}')
            print('')
            print(f'Lower Outliers in {col}')
            print('')
            print(outliers_lower)
            print('')
            print(f'Upper Outliers in {col}')
            print('')
            print(outliers_upper)
            print('')
            print(f'All Outliers in {col}')
            print('')
            print(outliers_all)
            plt.figure(figsize=(16,4))
            plt.subplot(1, 2, 1)
            sns.histplot(data = df, x = col, kde=True)
            plt.title(col)
            plt.subplot(1, 2, 2)
            sns.boxplot(x=df[col], data=df, whis=k)
            plt.title(col)
            plt.show()
            print('-------------------------------------------------------------------')
            
    else:
        
        for col in col_list:

            # Find the lower and upper quartiles
            q_25, q_75 = df[col].quantile([0.25, 0.75])
            # Find the Inner Quartile Range
            q_iqr = q_75 - q_25
            # Find the Upper Bound
            q_upper = q_75 + (k * q_iqr)
            # Find the Lower Bound
            q_lower = q_25 - (k * q_iqr)
            # Identify outliers
            outliers_lower = df[df[col] < q_lower].sort_values(by=col)
            outliers_upper = df[df[col] > q_upper].sort_values(by=col)
            outliers_all = pd.concat([outliers_lower, outliers_upper], axis=0).sort_values(by=col)

            print('')
            print(col)
            print(f'K: {k}')
            print(f'Lower Fence: {q_lower}')
            print(f'Upper Fence: {q_upper}')
            print('')
            print(f'Lower Outliers in {col}')
            print('')
            print(outliers_lower)
            print('')
            print(f'Upper Outliers in {col}')
            print('')
            print(outliers_upper)
            print('')
            print(f'All Outliers in {col}')
            print('')
            print(outliers_all)
            plt.figure(figsize=(16,4))
            plt.subplot(1, 2, 1)
            sns.histplot(data = df, x = col, kde=True)
            plt.title(col)
            plt.subplot(1, 2, 2)
            sns.boxplot(x=df[col], data=df, whis=k)
            plt.title(col)
            plt.show()
            print('-------------------------------------------------------------------')