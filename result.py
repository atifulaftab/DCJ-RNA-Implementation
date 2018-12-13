# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 17:22:35 2018

@author: atifu
"""
import numpy as np
from numpy import unravel_index
from DCJ import dcj

def result(allignment,no_inter_first,no_inter_second):
    sortArray=np.zeros((3,no_inter_second+1))
    threshhold=.6
    firstPermutation=[]
    secondPermutation=[]
    chr_a=[]
    for  w in range(1,no_inter_first+1,1):
        chr_a.append(w)
    chr_d=[]
    chr_i=[]
    chr_del=[]
    count=0
    for x in range(0,3,1): 
        for y in range(0,no_inter_second+1,1):
            if(x==0):
                if(y==0):
                    sortArray[0,0]=no_inter_first 
                elif(y>0):
                     for a in range(0,len(allignment),1): 
                         for b in range(0,len(allignment[0]),1):
                               if(allignment.max() > threshhold):
                                   data=np.unravel_index(allignment.argmax(),allignment.shape)
                                   data=np.array(data)
                                   row=data[0:1,]
                                   row=row[0]
                                   column=data[1:2,]
                                   column=column[0]
                                   for d in range(0, len(allignment) ,1):
                                       allignment[d,column] = 0
                                   for e in range(0, len(allignment[0]) ,1):
                                       allignment[row,e] = 0
                                   sortArray[0,column+1]=row+1
                                   
            elif(x==1):
                if(y>0):
                    for f in range(0,no_inter_second+1,1):
                        if(sortArray[0,f]==0):
                            sortArray[0,f]=no_inter_first+f
                            sortArray[2,1+count]=no_inter_first+f
                            chr_i.append(no_inter_first+f)
                            count=count+1
                    
            elif(x==2):
                sortArray[2,0]=count
                sortArray
    for w in range(1, len(sortArray[0]),1):
        chr_d.append(sortArray[0,w])

    chr_a=np.array(chr_a)
    chr_d=np.array(chr_d)
    chr_i=np.array(chr_i)
    chr_del=np.array(chr_del)
    #chr_del=np.append(chr_del,(np.delete(chr_a,chr_d)))
    chr_a=chr_a.tolist()
    chr_d=chr_d.tolist()
    chr_del=chr_del.tolist()
    chr_del=list(set(chr_a) - set(chr_d))

    firstPermutation=np.array(firstPermutation)                
    firstPermutation=np.concatenate((chr_a,chr_i), axis=0)
    firstPermutation=firstPermutation.astype(int)
    #firstPermutation=np.sort(firstPermutation, axis=0)
    secondPermutation=chr_d+chr_del
    secondPermutation=np.array(secondPermutation)
    secondPermutation=secondPermutation.astype(int)
    chr_a=np.array(chr_a)
    chr_d=np.array(chr_d)
    chr_i=np.array(chr_i)
    chr_del=np.array(chr_del)
    
    chr_d=chr_d.astype(int)
    sortArray[1,0]=len(chr_del)
    for l in range(1,len(chr_del),1):
        sortArray[1,l]=chr_del[l]
    sortArray=sortArray.astype(int)
    print("Sort Array:\n",sortArray)
    print("Actual Structure: ",chr_a)
    print("Inserted Component: ",chr_i)
    print("Desired Structure: ",chr_d)
    print("Deleted Components: ",chr_del)
    print("First Permutation: ",firstPermutation)
    print("Second Permutation: ",secondPermutation)
    
    #print(secondPermutation)
    #print(sortArray)                  
    
    dcj(firstPermutation,secondPermutation,chr_a,chr_d,chr_i,chr_del)
