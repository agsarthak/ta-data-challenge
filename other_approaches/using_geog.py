
# coding: utf-8

# In[17]:

import geog
import pandas as pd
import numpy as np


# In[18]:

user_data = pd.read_csv('data/sample_data.csv')
airport_data = pd.read_csv('data/optd-sample-20161201.csv')


# In[19]:

user_data.head()


# In[20]:

user_data_np = user_data.as_matrix()
airport_data_np = airport_data.as_matrix()


# In[99]:

xx = airport_data_np[:,1:3]
xx


# In[50]:

geog.distance(zz, xx)


# In[94]:

airport_data_np[:,1:3]


# In[ ]:

dist_min =[]
for i in user_data_np:
    dist_i = geog.distance(airport_data_np[:,1:3].astype('float64'), i[1:3].astype('float64'))
    dist_min.append(np.amin(dist_i))


# In[111]:

dist_min


# In[32]:

boston = [52.516700744628906, 4.6666998863220215]
la = [-26.693170000000002, 141.0478]
geog.distance(boston, la)


# In[38]:

np.radians(141.0478)

