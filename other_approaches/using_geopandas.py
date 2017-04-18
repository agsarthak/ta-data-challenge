
# coding: utf-8

# In[30]:

import geopandas as gpd
import pandas as pd
from shapely.geometry import Point
import matplotlib.pyplot as plt


# In[7]:

user_data = pd.read_csv('data/sample_data.csv')
airport_data = pd.read_csv('data/optd-sample-20161201.csv')


# In[32]:

airport_data


# In[16]:

# stations = pd.read_csv('../data/stations.csv')
user_data['geometry'] = user_data.apply(lambda z: Point(z.geoip_latitude, z.geoip_longitude), axis=1)
user_data = gpd.GeoDataFrame(user_data)


# In[19]:

airport_data['geometry'] = airport_data.apply(lambda z: Point(z.latitude, z.longitude), axis=1)
airport_data = gpd.GeoDataFrame(airport_data)


# In[31]:

airport_data.plot()
plt.show()


# In[22]:

aa = user_data.distance(airport_data)


# In[27]:

aa

