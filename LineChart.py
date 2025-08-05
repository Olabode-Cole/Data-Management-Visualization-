
# coding: utf-8

# In[5]:


import plotly
import pandas as pd
import numpy as np
import csv
import matplotlib
plotly.tools.set_credentials_file(username='OlabodeCole', api_key='xHrwhnfuK6HEqj3Nnhcd')

nba = pd.read_csv(r"C:\users\olabo\Desktop\NBA2018.csv", index_col='YEAR')
nba.head()


# In[34]:


import plotly.plotly as py
import plotly.graph_objs as go


trace1 = go.Scatter(
    x = nba.loc[2018].TEAM,
    y = nba.loc[2018].GP,
    mode = 'markers',
    name = 'GP'

)

trace2 =  go.Scatter(
    x = nba.loc[2018].TEAM,
    y = nba.loc[2018].PTS,
    mode = 'lines+markers',
    name = 'PTS'
    

)

trace3 =  go.Scatter(
    x = nba.loc[2018].TEAM,
    y = nba.loc[2018].FGA,
    mode = 'lines',
    name = 'FGA'
    

)
data = [trace1, trace2, trace3]
py.iplot(data, filename='scatter-mode')

