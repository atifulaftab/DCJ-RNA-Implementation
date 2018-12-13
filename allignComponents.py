# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 17:13:32 2018

@author: atifu
"""
import numpy as np
def allignComponents(opening_bracket_fs,closing_bracket_fs,opening_bracket_ss,closing_bracket_ss,wp,wd,sl,no_inter_first,no_inter_second,length_first,length_second):
    component_length=np.zeros((no_inter_first,no_inter_second))
    stem_length=np.zeros((no_inter_first,no_inter_second))
    alignment=np.zeros((no_inter_first,no_inter_second))
    for x in range(0,no_inter_first,1): 
        for y in range(0,no_inter_second,1):
            component_length[x,y]=1-abs(wd*(((closing_bracket_fs[0,x]-opening_bracket_fs[0,x]+length_first[0,x])- (closing_bracket_ss[0,y]-opening_bracket_ss[0,y]+length_second[0,y]))/((closing_bracket_fs[0,x]-opening_bracket_fs[0,x]+length_first[0,x])+(closing_bracket_ss[0,y]-opening_bracket_ss[0,y]+length_second[0,y]))))
            stem_length[x,y]=1-abs(sl*(((length_first[0,x])-(length_second[0,y]))/((length_first[0,x])+(length_second[0,y]))))
            alignment[x,y]=round(component_length[x,y]*stem_length[x,y],2)
    
    return alignment