
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import csv
import os
import bokeh
from bokeh.io import output_notebook
output_notebook()


# In[2]:


from bokeh.io import show
from bokeh.plotting import figure, show, output_file
from bokeh.models import ColumnDataSource, ColorBar


# In[3]:


nba = pd.read_csv(r"C:\users\olabo\Desktop\csv\NBA_STATS.csv", index_col='YEAR')
nba.head()


# In[4]:


nba.loc[2019].PTS.head()


# In[5]:


p = figure(
    height=300, x_range=(0, 100), y_range=(0, 15))
p.circle(x=nba.loc[2015].W, y=nba.loc[2015].PM)

show(p)


# In[6]:


p.xaxis


# In[7]:


from bokeh.models import ColumnDataSource
source = ColumnDataSource(dict(
    x=nba.loc[2019].W,
    y=nba.loc[2019].PM,
    pa=nba.loc[2019].PA,
    team=nba.loc[2019].TEAM,
    PTS=nba.loc[2019].PTS,
    AST=nba.loc[2019].AST,
    REGION=nba.loc[2019].REGION
))


# In[8]:


source.data['team']
source.data['pa']


# In[9]:


PLOT_OPTS = dict(
    height=500, x_range=(0,100),
    y_range=(0,15)
)


# In[10]:



from bokeh.models import HoverTool


# In[11]:


hover = HoverTool(tooltips='@pa, @team', show_arrow=False)
p = figure(tools=[hover], **PLOT_OPTS)
p.circle(x='x', y='y',source=source)
show(p)


# In[12]:


from bokeh.models import ColumnDataSource
from bokeh.palettes import Spectral6
Spectral6

source = ColumnDataSource(dict(
    x=nba.loc[2019].W,
    y=nba.loc[2019].PM,
    pa=nba.loc[2019].PA,
    team=nba.loc[2019].TEAM,
    PTS=nba.loc[2019].PTS,
    AST=nba.loc[2019].AST,
    REGION=nba.loc[2019].REGION
    
))
source.column_names

list(nba.REGION.unique())

source = ColumnDataSource(nba.loc[2019])
source.column_names


# In[13]:


from bokeh.models import LinearInterpolator, CategoricalColorMapper
from bokeh.palettes import Spectral6
Spectral6

from ipywidgets import interact

from bokeh.io import push_notebook

def update(YEAR):
    new_nba = dict(
        x=nba.loc[YEAR].W,
        y=nba.loc[YEAR].PM,
        pa=nba.loc[YEAR].PA,
        AST=nba.loc[YEAR].AST,
        PTS=nba.loc[YEAR].PTS,
        BLK=nba.loc[YEAR].BLK,
        REGION=nba.loc[YEAR].REGION,
        team=nba.loc[YEAR].TEAM,
    )
    source.data = new_nba
    p.title.text = str(YEAR)
    push_notebook()
    
interact(update, YEAR=(2014, 2019, 1))

size_mapper = LinearInterpolator(
    x=[nba.AST.min(), nba.AST.max()],
    y=[0,100]
)

color_mapper = CategoricalColorMapper(
     factors=list(nba.REGION.unique()),
     palette=Spectral6,
)

p = figure(
    title=str(2018),
    x_axis_label='GamesWon',
    y_axis_label='3PointsMade%',
    tools=[HoverTool(tooltips='@team, @pa', show_arrow=False)], 
    **PLOT_OPTS)
p.circle(
    x='x', y='y',
    size={'field': 'AST', 'transform': size_mapper},
    color={'field': 'REGION', 'transform': color_mapper},
    alpha=0.6, 
    source=source,
    legend='REGION'
)

p.right.append(p.legend[0])
show(p, notebook_handle=True)


# In[14]:


list(nba.REGION.unique())

