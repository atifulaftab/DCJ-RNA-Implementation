# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 18:43:16 2018

@author: atifu
"""

"""Implementation of DCJ-RNA Proposed By Badr et al. By Atif Ul Aftab """

 # -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 12:34:38 2018

@author: atifu
"""

"implementation of dcj-rna by Badr et al."

import numpy as np
from fileReading import readFile
from allignComponents import allignComponents
from result import result

structure_1=readFile('Cyano-1.txt')
structure_2=readFile('Flavo-1.txt')
no_inter_first=len(structure_1)
no_inter_second=len(structure_2)
structure_1=structure_1.transpose()
structure_2=structure_2.transpose()

opening_bracket_fs=structure_1[0:1,]
closing_bracket_fs=structure_1[1:2,]
length_first=structure_1[2:3,]

opening_bracket_ss=structure_2[0:1,]
closing_bracket_ss=structure_2[1:2,]
length_second=structure_2[2:3,]
   
wp=1
wd=1
sl=1

opening_bracket_fs=np.array(opening_bracket_fs)
closing_bracket_fs=np.array(closing_bracket_fs)
opening_bracket_ss=np.array(opening_bracket_ss)
closing_bracket_ss=np.array(closing_bracket_ss)
length_first=np.array(length_first)
length_second=np.array(length_second)

allignment=[]
allignment=np.array(allignment)
allignment=allignComponents(opening_bracket_fs,closing_bracket_fs,opening_bracket_ss,closing_bracket_ss,wp,wd,sl,no_inter_first,no_inter_second,length_first,length_second)
print("Allignement Similarity between two structure :\n",allignment)
result(allignment,no_inter_first,no_inter_second)