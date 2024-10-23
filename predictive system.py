# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 12:15:18 2024

@author: AKIN-JOHNSON
"""

import numpy as np
import pickle

# loading the logistic trained model
with open("C:/Users/AKIN-JOHNSON/Desktop/Student performance data/Jamb_pred_lr.sav", 'rb') as file:
    lr_model = pickle.load(file)
# loading the KNN trained model
with open("C:/Users/AKIN-JOHNSON/Desktop/Student performance data/Jamb_pred_knn.sav", 'rb') as file:
    knn_model = pickle.load(file)
