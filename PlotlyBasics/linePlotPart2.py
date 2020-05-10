import numpy as np
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('C:/Users/3780183/Projects/PersonalDevelopment/pythonDash/SourceData/nst-est2017-alldata.csv')

# filtering for new england state
dfEngland = df[df['DIVISION']=='1']
dfEngland.set_index('NAME',inplace = True)

#selecting only populations columns -- column name starts with POP
popColumns = [col for col in dfEngland.columns if col.startswith('POP')]
dfEngland = dfEngland[popColumns]

#print(popColumns)
#print(dfEngland.head())

data = [go.Scatter( x = popColumns,
                        y = dfEngland.loc[i],
                        mode = 'lines+markers',
                        name = i) for i in dfEngland.index ]


layout = go.Layout(title = 'Population of New England States',
                 xaxis = dict(title = 'YEAR',
                              color = 'RED'),
                 yaxis = dict(title = 'POPULATION',
                              color = 'RED'))

fig = go.Figure(data,layout)

pyo.plot(fig,filename = 'plots/linePlotPart2.html')
