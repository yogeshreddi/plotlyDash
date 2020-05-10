import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv(r'C:\Users\3780183\Projects\PersonalDevelopment\pythonDash\Data\2010SantaBarbaraCA.csv')

#print(df.head())


data = [go.Heatmap(x = df['DAY'],
                    y = df['LST_TIME'],
                    z=df['T_HR_AVG'].values.tolist(),
                   colorscale = 'Jet')]

layout = go.Layout(title = 'Heat Map')

fig = go.Figure(data = data,layout=layout)

pyo.plot(fig,'plots/heatMapPlot.html')
