# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 16:37:39 2017

@author: jules
"""
import os
import pandas as pd

root_path = './unclean_data'
new_path = './clean_data'
folder = os.listdir(root_path)
list_filenames = []
cleaned_columns = ['id']
string_columns = ['ethnicity', 'marital_status', 'owner_type', 'gender', 'use']
interval_columns = ['age', 'bld_val', 'credit_rating', 'year_built', 'roof_age']
boolean_columns = ['computers', 'consumer_electronics', 'frequent_remodeler']

# gets filenames of csv in folder, given root path
for file in folder:
    filepath = root_path + "/" + file
    #print(filepath) # print filepath of file in folder
    list_filenames.append(file)

    # clean each csv and copy selected columns to new location
for filename in list_filenames:
    filepath = root_path + "/" + filename
    # create dataframe from filepath
    dt = pd.read_csv(filepath, low_memory=False, usecols=['id', 'ethnicity', 'marital_status', 'owner_type', 'gender', 'use', 'age', 'bld_val', 'credit_rating', 'year_built', 'roof_age','computers', 'consumer_electronics', 'frequent_remodeler'])
    
    # clean string columns with unknown
    for label in string_columns:
        if label == 'martial_status':
            dt[label] = dt[label].fillna('Unknown or not provided')
        dt[label] = dt[label].fillna('Unknown')
        dt[label], label = dt[label].factorize()

        

        
    # clean number columns with mean
    for label in interval_columns:
        m = dt[label].mean()
        dt[label] = dt[label].fillna(int(m))
        
    # clean boolean columns with false
    for label in boolean_columns:
        dt[label] = dt[label].fillna('f')
        dt[label], label = dt[label].factorize()
        
    # create new dataframe with only cleaned columns
    cleaned_columns += string_columns + interval_columns + boolean_columns
    new_dt = dt[cleaned_columns].copy()
    
    # write new dataframe to new csv in new path
    new_filepath = new_path + '/cleaned_' + filename
    new_dt.to_csv(new_filepath, encoding='utf-8')