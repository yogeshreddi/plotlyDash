import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go


df = pd.read_csv('C:/Users/3780183/Projects/PersonalDevelopment/pythonDash/Data/2018WinterOlympics.csv')

# COlumns =    Rank                NOC  Gold  Silver  Bronze  Total


data = [go.Bar(x = df.NOC,y = df[medal],name = medal) for medal in ['Gold','Silver','Bronze']]


layout0 = go.Layout(title = 'Medals won by different countries in Winter olypics 2018',
                    xaxis = dict(title = 'Country'),
                    yaxis = dict(title = 'Medal Colunt'))

layout1 = go.Layout(title = 'Medals won by different countries in Winter olypics 2018',
                    xaxis = dict(title = 'Country'),
                    yaxis = dict(title = 'Medal Colunt'),
                    barmode = 'stack')

fig = go.Figure(data = data,layout = layout0)
pyo.plot(fig,filename = 'plots/barplot.html')

fig = go.Figure(data = data,layout = layout1)
pyo.plot(fig,filename = 'plots/barplotStacked.html')
