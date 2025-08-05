
# coding: utf-8

# In[13]:


import pandas as pd
import plotly
import numpy as np 
import matplotlib 
plotly.tools.set_credentials_file(username='OlabodeCole', api_key='xHrwhnfuK6HEqj3Nnhcd')


# In[14]:


nba = pd.read_csv('C:/Users/olabo/Desktop/csv/playoff_shots.csv', sep=',')
nba


# In[15]:


shots_df = nba[(nba.Player_Name == 'Stephen Curry') | #Goldenstate
                        (nba.Player_Name == 'Kevin Durant') |
                        (nba.Player_Name == 'DeMarcus Cousins') |
                        (nba.Player_Name == 'Klay Thompson') |
                        (nba.Player_Name == 'Draymond Green')| 
                        (nba.Player_Name == 'Kevin Love') | #Caveliers 
                        (nba.Player_Name == 'Anthoney Davis') | #NewOrleans Pelicans
                        (nba.Player_Name == 'Kyrie irving') | #Boston Celtic
                        (nba.Player_Name == 'Al Horford') | 
                        (nba.Player_Name == 'LeBron James') | #LA Lakers
                        (nba.Player_Name == 'John Wall') |
                        (nba.Player_Name == 'LaMarcus Aldridge') | #SanAntonio Spurs
                        (nba.Player_Name == 'Demar DeRozen') |
                        (nba.Player_Name == 'Russel Westbrook') | # Oklahoma Thunder
                        (nba.Player_Name == 'Andre Drummond') | #Detroit Pistons
                        (nba.Player_Name == 'Giannis Antetokounmpo') | #Milwaukee Bucks
                        (nba.Player_Name == 'Joel Embiid') | #Philly
                        (nba.Player_Name == 'Jimmy Butler') |
                        (nba.Player_Name == 'James Harden') | #Houson Rocket
                        (nba.Player_Name == 'Karl-Anthony Towns')] #Minnesota Timberwolves 
                                                
shots_df


# In[16]:


shots_df.columns


# In[17]:


shots_df.Player_Name.unique()


# In[22]:


court_shapes = []

#Outer Lines
outer_lines_shape = dict(
    type='rect',
    xref='x',
    yref='y',
    x0='-250',
    y0='-47.5',
    x1='250',
    y1='422.5',
    line=dict(
        color='rgba(10, 10, 10, 1)',
        width=1
    )
)

court_shapes.append(outer_lines_shape)

#Hoop Shape
hoop_shape = dict(
    type='circle',
    xref='x',
    yref='y',
    x0='7.5',
    y0='7.5',
    x1='-7.5',
    y1='-7.5',
    line=dict(
        color='rgba(10, 10, 10, 1)',
        width=1
    )
)
 
court_shapes.append(hoop_shape)

#Basket Backboard
backboard_shape = dict(
    type='rect',
    xref='x',
    yref='y',
    x0='-30',
    y0='-7.5',
    x1='30',
    y1='-6.5',
    line=dict(
        color='rgba(10, 10, 10, 1)',
        width=1
    ),
    fillcolor='rgba(10, 10, 10, 1)'
)
 
court_shapes.append(backboard_shape)

#Outer Box of Three-Second Area
outer_three_sec_shape = dict(
    type='rect',
    xref='x',
    yref='y',
    x0='-80',
    y0='-47.5',
    x1='80',
    y1='143.5',
    line=dict(
        color='rgba(10, 10, 10, 1)',
        width=1
    )
)
 
court_shapes.append(outer_three_sec_shape)

#Inner Box of Three-Second Area
inner_three_sec_shape = dict(
    type='rect',
    xref='x',
    yref='y',
    x0='-60',
    y0='-47.5',
    x1='60',
    y1='143.5',
    line=dict(
        color='rgba(10, 10, 10, 1)',
        width=1
    )
)
 
court_shapes.append(inner_three_sec_shape)

#Three Point Line (Left)
left_line_shape = dict(
    type='line',
    xref='x',
    yref='y',
    x0='-220',
    y0='-47.5',
    x1='-220',
    y1='92.5',
    line=dict(
        color='rgba(10, 10, 10, 1)',
        width=1
    )
)
 
court_shapes.append(left_line_shape)

#Three Point Line (Right)
right_line_shape = dict(
    type='line',
    xref='x',
    yref='y',
    x0='220',
    y0='-47.5',
    x1='220',
    y1='92.5',
    line=dict(
        color='rgba(10, 10, 10, 1)',
        width=1
    )
)
 
court_shapes.append(right_line_shape)

#Three Point Line Arc
three_point_arc_shape = dict(
    type='path',
    xref='x',
    yref='y',
    path='M -220 92.5 C -70 300, 70 300, 220 92.5',
    line=dict(
        color='rgba(10, 10, 10, 1)',
        width=1
    )
)
 
court_shapes.append(three_point_arc_shape)

#Restraining Circle
res_circle_shape = dict(
    type='circle',
    xref='x',
    yref='y',
    x0='20',
    y0='442.5',
    x1='-20',
    y1='402.5',
    line=dict(
        color='rgba(10, 10, 10, 1)',
        width=1
    )
)
 
court_shapes.append(res_circle_shape)

#Center Circle
center_circle_shape = dict(
    type='circle',
    xref='x',
    yref='y',
    x0='60',
    y0='482.5',
    x1='-60',
    y1='362.5',
    line=dict(
        color='rgba(10, 10, 10, 1)',
        width=1
    )
)
 
court_shapes.append(center_circle_shape)



#Free Throw Circle
free_throw_circle_shape = dict(
    type='circle',
    xref='x',
    yref='y',
    x0='60',
    y0='200',
    x1='-60',
    y1='80',
    fillcolor ='rgba(255, 178, 102)',
    line=dict(
        color='rgba(10, 10, 10, 1)',
        width=1
    )
)
 
court_shapes.append(free_throw_circle_shape)

#Restricted Area
res_area_shape = dict(
    type='circle',
    xref='x',
    yref='y',
    x0='40',
    y0='40',
    x1='-40',
    y1='-40',
    line=dict(
        color='rgba(10, 10, 10, 1)',
        width=1,
        dash='dot'
    )
)
 
court_shapes.append(res_area_shape)


# In[23]:


import plotly.graph_objs as go
from plotly.offline import iplot, init_notebook_mode
init_notebook_mode(connected=True)

def updateVisibility(selectedPlayer):
    visibilityValues = []
    for player in list(shots_df.Player_Name.unique()):
        if player == selectedPlayer:
            visibilityValues.append(True)
            visibilityValues.append(True)
        else:
            visibilityValues.append(False)
            visibilityValues.append(False)
    return visibilityValues

data = []
buttons_data = []
for player in list(shots_df.Player_Name.unique()):
    shot_trace_made = go.Scatter(
        x = shots_df[(shots_df['Event_type'] == 'Made Shot') & (shots_df['Player_Name'] == player)]['Loc_X'],
        y = shots_df[(shots_df['Event_type'] == 'Made Shot') & (shots_df['Player_Name'] == player)]['Loc_Y'],
        mode = 'markers',
        marker = dict(
            size = 6,
            color = 'rgba(63, 191, 63, 0.9)',
        ), 
        name = 'Made',
        text = shots_df[(shots_df['Event_type'] == 'Made Shot') & (shots_df['Player_Name'] == player)]['Shot_Zone_Basic'],
        textposition = 'middle center',
        textfont = dict(
            color = 'rgba(75, 85, 102,0.7)'
        ),
        visible = (player =='LeBron James')
    )

    shot_trace_missed = go.Scatter(
        x = shots_df[(shots_df['Event_type'] == 'Missed Shot') & (shots_df['Player_Name'] == player)]['Loc_X'],
        y = shots_df[(shots_df['Event_type'] == 'Missed Shot') & (shots_df['Player_Name'] == player)]['Loc_Y'],
        mode = 'markers',
        marker = dict(
            size = 6,
            color = 'rgba(241, 18, 18, 0.9)',
        ), 
        name = 'Missed',
        text = shots_df[(shots_df['Event_type'] == 'Missed Shot') & (shots_df['Player_Name'] == player)]['Shot_Zone_Basic'],
        textposition = 'middle center',
        textfont = dict(
            color = 'rgba(75, 85, 102,0.7)'
        ),
        visible = (player =='LeBron James')
    )

    data.append(shot_trace_made)
    data.append(shot_trace_missed)
    
    buttons_data.append(
        dict(
            label = player,
            method = 'update',
            args = [{'visible': updateVisibility(player)}]
        )
    )
    

updatemenus = list([
    dict(active=0,
         buttons = buttons_data,
         direction = 'down',
         pad = {'r': 10, 't': 10},
         showactive = True,
         x = 0.21,
         xanchor = 'left',
         y = 1.19,
         yanchor = 'top',
         font = dict (
             size = 14
         )
    )
])

layout = go.Layout(
    title='________________ Shot Chart',
    titlefont=dict(
        size=14
    ),
    hovermode = 'closest',
    updatemenus = updatemenus,
    showlegend = True,
    height = 600,
    width = 600, 
    shapes = court_shapes,
    xaxis = dict(
        showticklabels = False
    ),
    yaxis = dict(
        showticklabels = False
    )
)
 
fig = go.Figure(data=data, layout=layout)
iplot(fig)


# In[ ]:




