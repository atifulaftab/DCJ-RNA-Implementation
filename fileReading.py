# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 15:15:55 2018

@author: atifu
"""

import csv
import numpy as np

def readFile(filename):
    data = []
    with open(filename, 'rt') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            data.append(row)

    data = np.array(data,dtype= np.float)
    
    
    return data