import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input,Output,State

import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv(r'C:\Users\3780183\Projects\PersonalDevelopment\pythonDash\Data\gapminderDataFiveYear.csv')

#print(df.head())

#print(df.shape)

app = dash.Dash()

app.layout = html.Div([

    html.H1(title = 'GDP Per Capital vs Life Expectancy for Different countries',
            style = {'textAlign':'center'}),
    html.Div([
        dcc.Graph(id = 'myGraph')
    ]),
    html.Div([
        html.Label('select the year'),
        dcc.Dropdown(id = 'myDropDown' ,
                     options = [{'label':i,'value':i} for i in df.year.unique()],
                     value = df.year.unique()[0]
                    ),
        html.Button(id = 'dropdown-button',
                   children = 'Submit',
                   n_clicks = 0)
    ])
])

@app.callback(Output(component_id = 'myGraph',
                     component_property = 'figure'),
              [Input(component_id = 'dropdown-button',
                     component_property = 'n_clicks')],
              [State(component_id = 'myDropDown',
                      component_property = 'value')])
def updateFigure(n_clicks,Input_year):
    df_year = df[df.year == Input_year]

    data = [go.Scatter(x=df_year[df_year.continent == cont].gdpPercap,
                       y=df_year[df_year.continent == cont].lifeExp,
                       name = cont,
                       mode = 'markers',
                       marker = {'size':15}) for cont in df_year.continent.unique() ]

    layout = go.Layout(title = 'GDP vs LifeExp by continents',
                       xaxis = {'title':'GDP per Capital','type':'log'},
                       yaxis = {'title':'Life Expectancy'})

    return(go.Figure(data=data,layout = layout))

if __name__ == '__main__':
    app.run_server()
