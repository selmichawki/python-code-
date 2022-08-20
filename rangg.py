# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 21:08:05 2020

@author: user
"""

import numpy as np
from scipy import *

m=np.array([[0,3,1,0,0,2,4,5,6],
           [1,5,0,3,2,0,4,6,7],
           [1,3,0,2,0,0,4,5,0],
           [1,5,0,3,2,4,0,6,7]])
def somme(m):
    t=np.zeros(9)
    s=0
    j=0
    while j<9:
        for i in range(4):
            s+=m[i][j] 
        t[j]=s
        s=0
        j+=1
    return t
def nbrang(m):
    tt=np.zeros(9)
    f=0
    j=0
    while j<9:
        for i in range(4):
            if m[i][j] != 0:
                f+=1
        tt[j]=f
        f=0
        j+=1
    return tt
somme(m)
nbrang(m)
def rang_moyen(m):
    rm=np.zeros(9)
    a=somme(m)
    b=nbrang(m)
    i=0
    while i<9:
        rm[i]=a[i]/b[i]
        i+=1
    return rm    
rang_moyen(m)
l=list(rang_moyen(m))

p=list(range(1,10))

def tri(l,p):
    l1=l.copy()
    p1=p.copy()
    for i in range(len(l1)):
        
        min = i
        for j in range(i+1, len(l1)):
            if l1[min] > l1[j]:
                min = j
        a = l1[i]
        aa=p1[i]
           
        l1[i] = l1[min]
        p1[i]=p1[min]
         
        l1[min] = a
        p1[min]= aa
            
        
    return p1
print(tri(l,p))


