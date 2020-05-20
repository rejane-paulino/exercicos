#!/usr/bin/env python
# coding: utf-8

# In[26]:


#Exercicio 02

import matplotlib.pyplot as plt

#Grupos de Idade
g_idade = ['0 a 4','5 a 9','10 a 14','15 a 19','20 a 24','25 a 29','30 a 34','35 a 39','40 a 44','45 a 49','50 a 54','55 a 59','60 a 64','65 a 69','70 a 74','75 a 79','80 a 84','85 a 89','90 a 94','95 a 99','≥ 100']
  
#População Femenina
p_femenina = [6779171, 7345231, 8441348, 8432004, 8614963, 8643419, 8026854, 7121915, 6688796, 6141338, 5305407, 4373877, 3468085, 2616745, 2074264, 1472930, 998349, 508724, 211594, 66806, 16989]

x = [ x for x in range(len(g_idade))]

plt.figure(figsize=(10, 8))

plt.bar(x, p_femenina, align='center',
        color='orange', linewidth=1, edgecolor='black')

plt.yticks([ 0, 1000000, 2000000, 3000000, 4000000, 5000000, 6000000, 7000000, 8000000, 9000000],
           [ "0", "1.0 milhão", "2.0 milhões", "3.0 milhões", "4.0 milhões", "5.0 milhões", "6.0 milhões", "7.0 milhões", "8.0 milhões", "9.0 milhões"])

plt.xticks(x, g_idade, rotation=45)
           
plt.title('População Femenina - IBGE/2010')

plt.xlabel('Grupos de Idade (anos)')
plt.ylabel('População Femenina');

plt.show()
           
           


# In[ ]:




