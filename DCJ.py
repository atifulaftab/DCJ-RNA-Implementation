# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 23:14:58 2018

@author: atifu
"""
import itertools
import numpy as np

def dcj(firstPermutation,secondPermutation,chr_a,chr_d,chr_i,chr_del):
    firstPermutation=firstPermutation.tolist()
    secondPermutation=secondPermutation.tolist()
    
    
    adjacency=["tell","head"]
    
    firstAdjacency=[]
    secondAdjacency=[]
    for firstPermutation in itertools.product(firstPermutation,adjacency):
        firstAdjacency.append(firstPermutation)
    
    for secondPermutation in itertools.product(secondPermutation,adjacency):     
        secondAdjacency.append(secondPermutation)
      
    
    
            
    print("Adjacency Repesentation of first permutation:\n",firstAdjacency)
    print("Adjacency Repesentation of second permutation:\n",secondAdjacency)
    
    temp=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    count=0
    if(len(chr_i)!=0):
        count=1  
    for x in range(0,len(secondAdjacency),1):
        for y in range(0,len(firstAdjacency),1):
            if(secondAdjacency[x]==firstAdjacency[y]):
                if((y-1>0) and (y+1!=len(firstAdjacency)) and (x+1!=len(secondAdjacency))):
                    if(secondAdjacency[x-1]!=firstAdjacency[y-1]):
                        count=count+1
                        for z in range(0,len(firstAdjacency),1):
                            if(firstAdjacency[z]==secondAdjacency[x-1]):
                                temp[z]=firstAdjacency[z]
                                firstAdjacency[y-1]=temp[z]                              
                    if(secondAdjacency[x+1]!=firstAdjacency[y+1]):
                        count=count+1
                        for z in range(0,len(firstAdjacency),1):
                            if(firstAdjacency[z]==secondAdjacency[x+1]):
                                temp[z]=firstAdjacency[z]
                                firstAdjacency[y+1]=temp[z]
    
                                     
      
    print("No of rearrangement operation: ",count)
    
        
    