

import numpy as np
import pandas as pd

import itertools
import os


# Plusieurs méthodes ont été proposées dans la littérature pour la subdivision en cellules, nous
# verrons dans ce cours :
# - La méthode de Kusiak  
# Ces méthodes visent à trouver des groupes de pièces spécifiques à certains groupes de
# machines.

# ### Méthode de Kusiak : recherche d’une décomposition parfaite

# #### Exemple : Atelier de 7 machines pour usiner 8 pieces

# #### Dans cette partie on va importer les données d'un fichier EXEL

# In[2]:
Piece=np.array(['P1','P2','P3','P4','P5','P6','P7','P8'])
Machine=np.array(['M1','M2','M3','M4','M5','M6','M7'])

PM=np.array([[0,1,1,0,1,0,0,0],
             [1,0,0,0,0,1,0,0],
             [0,0,0,1,0,0,1,0],
             [0,0,0,0,0,1,0,0],
             [0,0,0,0,0,0,0,1],
             [0,0,0,1,0,0,0,0],
             [0,0,1,0,1,0,0,1]],dtype=int)

# In[3]:


""""# Matrices de Pieces
Piece=np.array(['P1','P2','P3','P4','P5','P6','P7','P8'])

# Matrice des machines
Machine=np.array(['M1','M2','M3','M4','M5','M6','M7'])

# Matrice de piece associe au machine,aij = 1 si la machine i usine la pièce j, 0 sinon.

PM=np.array([[0,1,1,0,1,0,0,0],
             [1,0,0,0,0,1,0,0],
             [0,0,0,1,0,0,1,0],
             [0,0,0,0,0,1,0,0],
             [0,0,0,0,0,0,0,1],
             [0,0,0,1,0,0,0,0],
             [0,0,1,0,1,0,0,1]],dtype=int)"""


# #### Cette fonction permet de parcourir la premier ligne (Piece 1) et extraire les "1" rencontrée.

# In[4]:


def Int(PM,K):
    P=np.array([],dtype=int)
    for j in range(len(Piece)):
        if(PM[K][j]==1):
            P=np.append(P,int(j))
    
    return P


# #### Cette fonction permet de parcourir les colonnes au "1" recontrées par la fonction precédente.

# In[5]:


def MACHINE(PM,P):
    M=np.array([],dtype=int)
    for j in P:
        for i in range(len(Machine)):
            if(PM[i][int(j)]==1):
                M=np.append(M,int(i))
    M=np.unique(M)
   
    return M


# #### Cette fonction permet de parcourir les lignes  au "1" recontrées par la fonction precédente.

# In[6]:


def PIECE(PM,M,P):
    for i in M:
        for j in range(len(Piece)):
            if(PM[int(i)][j]==1):
                P=np.append(P,int(j))
    P=np.unique(P)
    
    return P
        


# #### Cette fonction prend come input la matrice PM est result comme output 2 tableau (ILOT(Machine,Piece) + 2 tableau  machine,piece sans les machines,les pieces allouées.

# In[7]:


def ILOT(PM,piece,machine):
    # Deux variable pour comparait les tailles des matrices p et m dans le boucle while.
    k1=k2=0
    Bool=True
    #initialisation de matrice machine et piece
    p=m=[]
    
    i = Machine.tolist().index(machine[0]) # i will return index of 2
    
    p=Int(PM,i)
    m=MACHINE(PM,p)
    p=PIECE(PM,m,p)
    
    #ilot=np.array([])
    #Boucler dans la matrice jusqu'a le parcour de tout les "1".
    while(Bool):
        k1=len(p)+len(m)
    
        m=MACHINE(PM,p)
        p=PIECE(PM,m,p)
        k2=len(p)+len(m)
        
        if(k2!=k1):
            
            continue
        else:
            
            Bool=False
    #print("m" ,m)
    #ilot=np.append(ilot,m)
    #print("ILOT :",ilot)
    # Suppression des machine et des pieces
    
    
    for j in range (len(p)):
        
        piece=np.delete(piece,np.where(piece==('P'+str(int(p[j]+1)))))
        #piece=np.delete(piece,int(p[j]-j))
    
        
    
    for j in range (len(m)):
        
        machine=np.delete(machine,np.where(machine==('M'+str(int(m[j]+1)))))
        #machine=np.delete(machine,int(m[j]-j))
        

    for i in p:
        for j in range(len(Machine)):
            PM[j][i]=0
    for i in m:
        for j in range(len(Piece)):
            PM[i][j]=0
            
    return m,p,piece,machine

#ILOT(PM)
    
    
    


# In[8]:


def main_Kusiak():
    M=P=np.array([],dtype=int)
    m1=[]
    p1=[]
    pm=PM.copy()
    m,p,piece,machine=ILOT(pm,Piece,Machine)

    M=np.append(M,m+1)
    P=np.append(P,p+1)
    m1.append((m+1).tolist())
    p1.append((p+1).tolist())
    k=2
    while(len(piece)>=1):

        m,p,piece,machine=ILOT(pm,piece,machine)

        M=np.append(M,m+1)
        P=np.append(P,p+1)
        m1.append((m+1).tolist())
        p1.append((p+1).tolist())
        k+=1
    
    return M,P,m1,p1


# In[9]:


M,P,m,p=main_Kusiak()


# #### Cette fonction permet de trier la matrice PM selon l'ordre des ilots

# In[10]:


def Tri(PM,T1,T2):
    #Tri sur ligne
    PM1=np.zeros(PM.shape,dtype=int)
    for i in range(len(T1)):
        PM1[i]=PM[T1[i]-1]
    #Tri sur colonne
    PM2=PM1.T
    PM3=np.zeros(PM.T.shape,dtype=int)
    for j in range(len(T2)):
        PM3[j]=PM2[T2[j]-1]
    return PM3.T



#Creation de la matrice trier 
df1=Tri(PM,M,P)
print(df1)

# In[ ]:





# In[ ]:




