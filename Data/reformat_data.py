# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 14:31:59 2022

@author: trety
"""

from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import datetime
import pandas as pd
#%% Datasets
'''load datasets'''

X_train = np.load("..\data\X_train1.npy")# population in F=1
Y_train = np.load('..\data\Y_train1.npy')#normalized to w_L


X_test = np.load('..\data\X_val1.npy') # use validation set for testing
Y_test = np.load('..\data\Y_val1.npy') # use validation set for testing
#%%




df_train = pd.DataFrame({"W_par" : Y_train[:,0], "W_ort" : Y_train[:,1]})

X_df = pd.DataFrame(X_train)

X_df.iloc[10,:].plot()