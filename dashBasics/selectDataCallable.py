import pandas as pd
import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

import dash
import dash_core_components as dcc
import dash_html_components as html
import json
from dash.dependencies import Output,Input
import base64

np.random.seed(10)
x1 =  np.linspace(0.1,5,50)
x2 =  np.linspace(5.1,10,50)
y = np.random.randint(0,50,50)

df1 = pd.DataFrame({'x':x1,'y':y})
df2 = pd.DataFrame({'x':x1,'y':y})
df3 = pd.DataFrame({'x':x2,'y':y})

df = pd.concat([df1,df2,df3])

def encode_image(image_file):
    encoded = base64.b64encode(open(image_file, 'rb').read())
    return 'data:image/png;base64,{}'.format(encoded.decode())


data = [go.Scatter(x = df.x,
               y = df.y,
               dy=1,
               mode = 'markers',
               marker = {'size':10,
                         'color':'green',
                         'line':{'width':2,
                                 'color':'black'}})]


layout = go.Layout(title = 'Selected the area in the plot to see the density of points in that area',
                    xaxis = {'title':'color'},
                    yaxis = {'title':'# of wheels'},
                    hovermode = 'closest')

fig = go.Figure(data=data,layout=layout)



app = dash.Dash()

app.layout = html.Div([

                html.Div(
                    dcc.Graph(id = 'scatter-data',
                              figure = fig),
                    style = {'width':'30%','float':'left'}
                ),
                html.Div(
                    #html.Img(id = 'select-image',src = 'children',height = '300'),
                    html.Pre(id = 'density',style = {'paddingtop':35}),
                    style = {'width':'30%','float':'left'}
                )
])

@app.callback(Output('density','children'),
              [Input('scatter-data','selectedData')])
def find_density(selectedData):
    pts = len(selectedData['points'])
    selectedArea = (max(selectedData['range']['x'])-min(selectedData['range']['x']))*(max(selectedData['range']['y'])-min(selectedData['range']['y']))
    return 'Density {:.2f}'.format(pts*1.0/selectedArea)

if __name__ == '__main__':
    app.run_server()
