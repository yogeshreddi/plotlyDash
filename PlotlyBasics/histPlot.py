
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('C:/Users/3780183/Projects/PersonalDevelopment/pythonDash/Data/mpg.csv')

data = [go.Histogram(x = df.mpg,
                     xbins = dict(start=0,end=25,size=1.25))]
layout = go.Layout(title = 'Histogram of mpg')
fig = go.Figure(data=data,layout=layout)
pyo.plot(fig,filename = 'plots/histPlot.html')
