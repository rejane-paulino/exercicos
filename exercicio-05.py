#!/usr/bin/env python
# coding: utf-8

# In[120]:


#Exercicio 05

import matplotlib.pyplot as plt

#Anos de Publicação
anos_public = [2016, 2017, 2018, 2019, 2020]
  
#Puplicações OLCI - Inland Water
scient_directOLCI = [8, 24, 23, 24, 16]

#Puplicações Inland Water - Remote Sensing
scient_directIWRS = [478, 635, 705, 836, 524]


plt.figure(figsize=(7, 6))

#Gráfico - Inland Water - Remote Sensing

plt.bar(anos_public, scient_directIWRS, 
        align='center', color='gray', linewidth=1, edgecolor='black')

plt.yticks([0, 150, 300, 450, 600, 750, 900])

plt.xticks(anos_public, rotation=0)

plt.plot(anos_public, scient_directOLCI,
         color="black", linestyle="--",  marker='o', linewidth=1, markersize=8)
      
plt.xticks(anos_public, rotation=0)
           
plt.title('Puplicações de pesquisas\n''Inland Water + Remote Sensing/OLCI + Inland Water (Scient Direct)')

plt.xlabel('Ano de Publicação')
plt.ylabel('N° de Puplicações');

plt.grid(b=True, color='gray', linestyle='--', linewidth=0.25);

plt.legend([r"OLCI + Inland Water",
            r"Inland Water + Remote Sensing"]);

plt.show()



# In[ ]:





# In[ ]:




