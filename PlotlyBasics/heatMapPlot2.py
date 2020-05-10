import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go
from plotly import tools

df1 = pd.read_csv(r'C:\Users\3780183\Projects\PersonalDevelopment\pythonDash\Data\2010SantaBarbaraCA.csv')
df2 = pd.read_csv(r'C:\Users\3780183\Projects\PersonalDevelopment\pythonDash\Data\2010SitkaAK.csv')
df3 = pd.read_csv(r'C:\Users\3780183\Projects\PersonalDevelopment\pythonDash\Data\2010YumaAZ.csv')


def returnHeatMapTrace(df):
    return(go.Heatmap(x = df['DAY'],
                      y =df['LST_TIME'],
                      z=df['T_HR_AVG'].values.tolist(),
                      colorscale = 'Jet',
                      zmin=5,
                      zmax=40))

trace1 = returnHeatMapTrace(df1)
trace2 = returnHeatMapTrace(df2)
trace3 = returnHeatMapTrace(df3)

fig = tools.make_subplots(rows =1,
                          cols=3,
                          subplot_titles = ['2010SantaBarbaraCA','2010SitkaAK','2010YumaAZ'],
                          shared_yaxes = False)

fig.append_trace(trace1,1,1)
fig.append_trace(trace2,1,2)
fig.append_trace(trace3,1,3)

pyo.plot(fig,'plots/heatMapPlot2.html')
