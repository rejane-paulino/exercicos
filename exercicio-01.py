#!/usr/bin/env python
# coding: utf-8

# In[7]:


#Exercicio 01

import numpy as np

#Séries de Entrada
s1 = [168, 398, 451, 337, 186, 232, 262, 349, 189, 204, 220, 220, 207, 239, 259, 258,
242, 331, 251, 323, 106, 1055, 170]

s2 = [168, 400, 451, 300, 186, 200, 262, 349, 189, 204, 220, 220, 207, 239, 259, 258,
242, 331, 251, 180, 106, 1055, 200]

#Array
#Matriz 1 por 23
a = np.array(s1)
b = np.array(s2)

print('Array s1:\n',a)
print('\t')
print('Array s2:\n',b)
print('\t')

#Distância Euclidiana
##Decomposição da Distância Euclidiana
sub_array = b - a
pot_array = sub_array ** 2
somat_array = np.sum(pot_array)
dist_euclid = np.sqrt(somat_array)

print('Distância Euclidiana','='*50)
print(dist_euclid)
print('\t')

#Série temporal com os valores médios entre s1 e s2
##Decomposição da Média
soma_array = a + b
media_array = soma_array/2

print('Série Temporal - Média','='*48)
print(media_array)
print('\t')

#Série temporal com os valores máximos entre s1 e s2
maximos_array = np.maximum(a,b)

print('Série Temporal - Máximos','='*46)
print(maximos_array)
print('\t')

#Série temporal com os valores mínimo entre s1 e s2
minimos_array = np.minimum(a,b)

print('Série Temporal - Minimos','='*46)
print(minimos_array)
print('\t')

plt.show()


# In[ ]:




