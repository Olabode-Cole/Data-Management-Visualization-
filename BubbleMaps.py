
# coding: utf-8

# In[62]:


import numpy as np
import pandas as pd
import csv
import matplotlib
import plotly.plotly as py
import plotly.graph_objs as go


# In[63]:


nba = pd.read_csv(r"C:\users\olabo\Desktop\csv\NBA_Franchise_Record.csv", index_col='From')
nba.head()


# In[80]:


nba['text'] = nba['name'] + '<br>Wins' + (nba['Wins']).astype(str)
limits = [(0,2),(3,10),(11,20),(21,50),(50,3000)]
colors = ["rgb(0,116,217)","rgb(255,65,54)","rgb(133,20,75)","rgb(255,133,27)","lightgrey"]
cities = []
scale = 3000

for i in range(len(limits)):
    lim = limits[i]
    nba_sub = nba[lim[0]:lim[1]]
    city = dict(
        type = 'scattergeo',
        locationmode = 'USA-states',
        lon = nba_sub['Lon'],
        lat = nba_sub['Lat'],
        text = nba_sub['text'],
        marker = dict(
            size = nba_sub['Playoffs'],
            # sizeref = 2. * max(df_sub['pop']/scale) / (25 ** 2),
            color = colors[i],
            line = dict(width=0.5, color='rgb(40,40,40)'),
            sizemode = 'area'
        ),
        name = '{0} - {1}'.format(lim[0],lim[1]) )
    cities.append(city)
    


layout = dict(
        title = 'NBA Teams Total Wins <br>(Click legend to toggle traces)',
        showlegend = True,
        geo = dict(
            scope='usa',
            projection=dict( type='albers usa' ),
            showland = True,
            landcolor = 'rgb(217, 217, 217)',
            subunitwidth=1,
            countrywidth=1,
            subunitcolor="rgb(255, 255, 255)",
            countrycolor="rgb(255, 255, 255)"
        ),
    )

fig = dict(data=cities, layout=layout)
py.iplot(fig, validate=False, filename='d3-bubble-map-populations')

