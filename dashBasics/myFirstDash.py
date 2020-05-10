import dash
import dash_core_components as dcc # for interactivity in your dashboard
import dash_html_components as html # layout definations (UI) in the dashboard

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


#layout = go.Layout(title = 'Population of New England States',
#                 xaxis = dict(title = 'YEAR',
#                              color = 'RED'),
#                 yaxis = dict(title = 'POPULATION',
#                              color = 'RED'))

app = dash.Dash() # initiating your app just like in a flask

colors = {'background':'#111111',
          'text' : '#7FDBFF'}

app.layout = html.Div(children = [
             html.H1('Hello Dash!',
                     style = {'textAlign':'center',
                              'color':colors['text']
                              }
             ),
             html.Div('Dash: My first dashboard in Python!'),
             dcc.Graph(id='example',
                       figure = {'data':data,
                                 'layout':{'title': 'Population of New England States',
                                           'plot_bgcolor':colors['background'],
                                           'paper_bgcolor':colors['background'],
                                           'font':{'color':colors['text']
                                                  }
                                           }
                                }
                        )
             ],style = {'backgroundColor':colors['background']}
             )

if __name__ == '__main__':
    app.run_server()
