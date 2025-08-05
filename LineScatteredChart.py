
# coding: utf-8

# In[23]:


import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

get_ipython().run_line_magic('matplotlib', 'inline')


# In[32]:


nba = pd.read_csv(r"C:\users\olabo\Desktop\NBA2018.csv", index_col='YEAR')
nba.head()


# In[36]:


sns.lmplot(x='FGM', y='FGA', data=nba)

