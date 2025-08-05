
# coding: utf-8

# In[12]:


import pandas as pd
import numpy as np
import csv
import os
from bokeh.plotting import figure, output_file, show


# In[2]:


pwd


# In[3]:


nba = pd.read_csv(r"C:\users\olabo\Desktop\nba_2017_br.csv")
nba.head()


# In[16]:


nba[['Player','Pos','Tm','AST','3P%','FT%']]


# In[31]:


nba.iloc[0:10]

