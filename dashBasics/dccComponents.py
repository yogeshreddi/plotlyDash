import dash
import dash_html_components as html
import dash_core_components as dcc
from datetime import datetime as dt

app = dash.Dash()

states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]



app.layout = html.Div(children = [
                       html.H1('My first Header'),
                       dcc.Markdown(''' [Click here](http://127.0.0.1:8050/)
                       This querry will give us most expensive book purchased in any store of \'Tennessee\',\'Arkansas\',\'Mississippi\' together.
                       But if we are looking for most expensive book purchased in each of \'Tennessee\',\'Arkansas\',\'Mississippi\' individual, we just need to add a \"partition by  S.State\" condition in the window function
                       Similarly if we are looking for most expensive book purchased in each store, we would add \"partition by P.StoreNum\" to the window function.
                       '''),
                       html.Div('Second Division',
                                style = {'color':'blue',
                                         'border':'2px yellow solid'}),
                       html.Label('dropdown'),
                       dcc.Dropdown(
                                    options=[
                                            #{'label': 'Montréal', 'value': 'MTL'},
                                            #{'label': 'New York City', 'value': 'NYC'},
                                            #{'label': 'San Francisco', 'value': 'SF'}
                                            {'label': i, 'value': i} for i in states
                                            ],
                                    value='MTL',
                                    multi=True,
                                    style = {'color':'black',
                                            'border':'2px black solid'
                                            }
                                ),
                        html.Label('calander'),
                        dcc.DatePickerSingle(
                                    id='date-picker-single',
                                    date=dt(2020, 5, 10)
                                ),
                        html.P(html.Label('Slider')),
                        dcc.Slider(
                                    marks={i: 'Label {}'.format(i) for i in range(-5, 7)},
                                    min=-5,
                                    max=6,
                                    value=[-3, 4]
                                ),
                        html.P(html.Label('Some Radio Button')),
                        dcc.RadioItems(
                                     options=[
                                             {'label': 'Montréal', 'value': 'MTL'},
                                             {'label': 'New York City', 'value': 'NYC'},
                                             {'label': 'San Francisco', 'value': 'SF'}
                                             ],
                                     value='MTL',
                                     style = {'color':'black',
                                             'border':'2px black solid'
                                             }
                                             )
                    ],style = {'color':'orange',
                               'border':'3px green solid'})

if __name__ == '__main__':
    app.run_server()
