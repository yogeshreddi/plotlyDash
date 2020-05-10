import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

import dash
import dash_core_components as dcc
import dash_html_components as html
import json
from dash.dependencies import Output,Input
import base64


df = pd.read_csv('../data/wheels.csv')
print(df.head)

def encode_image(image_file):
    encoded = base64.b64encode(open(image_file, 'rb').read())
    return 'data:image/png;base64,{}'.format(encoded.decode())


data = [go.Scatter(x = df.color,
               y = df.wheels,
               dy=1,
               mode = 'markers',
               marker = {'size':10,
                         'color':'green',
                         'line':{'width':2,
                                 'color':'black'}})]


layout = go.Layout(title = 'Hovering over the dots will show magic',
                    xaxis = {'title':'color'},
                    yaxis = {'title':'# of wheels'},
                    hovermode = 'closest')

fig = go.Figure(data=data,layout=layout)



app = dash.Dash()

app.layout = html.Div([

                html.Div(
                    dcc.Graph(id = 'wheels-plot',
                              figure = fig),
                    style = {'width':'30%','float':'left'}
                ),
                html.Div(
                    html.Img(id = 'hover-image',src = 'children',height = '400'),
                    #html.Pre(id = 'hover-data',style = {'paddingtop':35}),
                    style = {'width':'30%'}
                )
])


@app.callback(Output('hover-data','children'),
              [Input('wheels-plot','hoverData')])

def callback_image(hoverData):
    wheel=hoverData['points'][0]['y']
    color=hoverData['points'][0]['x']
    path = '../data/images/'
    return encode_image(path+df[(df['wheels']==wheel) & \
    (df['color']==color)]['image'].values[0])

if __name__ == '__main__':
    app.run_server()
