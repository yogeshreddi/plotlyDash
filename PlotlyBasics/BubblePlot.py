import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('C:/Users/3780183/Projects/PersonalDevelopment/pythonDash/Data/mpg.csv')
#print(df.head())
#print(df.columns)


data = [go.Scatter(x = df.horsepower,
                   y = df.mpg,
                   text = df.name,
                   mode = 'markers',
                   marker = dict(size = df.weight/90,
                                 color = df.cylinders,
                                 showscale = True)
                 )
        ]

layout = go.Layout(title = 'mpg vs horsepower',
                   xaxis = dict(title = 'horsepower'),
                   yaxis = dict(title = 'mpg'))

fig = go.Figure(data = data, layout = layout)

pyo.plot(fig,filename = 'plots/bubbleplot.html')
