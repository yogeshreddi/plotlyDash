import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

np.random.seed(42)

random_x = np.random.randint(1,101,100)
random_y = np.random.randint(1,101,100)

data = [go.Scatter(x=random_x,
                   y=random_y,
                   mode='markers',
                   marker = dict(symbol='triangle-up',
                                 size=10,
                                 color='rgb(0,0,0)',
                                 line={'width':2}))]

layout = go.Layout(title = 'Hello First plot',
                    xaxis = {'title':'MY AXIS','color':'green'},
                    yaxis = dict(title='MY Y AXIS',color='red'),
                    hovermode = 'closest')

fig = go.Figure(data = data,layout = layout)

pyo.plot(fig,filename = 'plots/scatter.html')
