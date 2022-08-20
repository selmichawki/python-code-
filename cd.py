""": Résolution de problème d’ordonnancement d’ateliers de type flow Shop à n produits et m machines   """

""" comme exemple n = 4 et m = 5 """

import numpy as np
exp=np.array([[2,3,2,0],
    [0,5,1,10],
    [3,7,5,5],
    [1,4,6,8],
    [5,2,9,4]])

m=list(sum(exp[:,:]))
C=[[1000,0,0]]
u=0
for i in range(1,len(exp)):
  u=u+1
  p1=[]
  p2=[]
  spt=[]
  lpt=[]
  m1=list(sum(exp[:i,:]))
  m2=list(sum(exp[len(exp)-i:,:]))
  a1=m1.copy()
  a2=m2.copy()
  for j in range(len(m)):
    if a1[j]<=a2[j]:
      p1.append(a1[j])
      a2[j]="-"
    else:
      p2.append(a2[j])
  trip1=sorted(p1)
  trip2=sorted(p2, reverse=True)

  for e in range(len(trip1)):
    for c in range(len(m1)):
      if trip1[e]==a1[c]:
        spt.append(c)
        a1[c]="-"
        break
  for e in range(len(trip2)):
    for c in range(len(m2)):
      if trip2[e]==a2[c]:
        lpt.append(c)
        a2[c]="-"
        break



        
  S=spt+lpt
#Calcul de Cmax de la séquence optimale
  A=np.zeros([2,len(m)])
  for j in range(len(m)):
      A[0][j]=m1[S[j]]
      A[1][j]=m2[S[j]]
  for i in range(len(m)):
    A[1][0]=A[1][0]+A[0][0]
    A[0][i]=A[0][i]+A[0][i-1]
    A[1][i]=A[1][i]+max(A[1][i-1],A[0][i])
  if A[-1][-1]<=C[0][0]:
       C[0]=[A[-1][-1],S,u]
       
A=np.zeros([len(exp),len(m)])
for i in range(len(exp)):
  for j in range(len(m)):
    A[i][j]=exp[i][C[0][1][j]]

for j in range(1,len(m)):    
    A[0][j]=A[0][j]+A[0][j-1]
for i in range(1,len(A)):    
  A[i][0]=A[i][0]+A[i-1][0]
for i in range(1,len(A)):
  for j in range(1,len(m)):

    A[i][j]=A[i][j]+max(A[i][j-1],A[i-1][j])

#Affichage        
for i in range(len(C[0][1])):
  C[0][1][i]+=1
print('Cmax=',A[-1][-1],', k=',C[0][2])  
print("Séquence:\n",*C[0][1], sep='-')
