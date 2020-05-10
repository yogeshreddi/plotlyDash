import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input,Output

app = dash.Dash()


app.layout = html.Div([
                        html.Div([dcc.Input(id = 'my-input-string',value = 'Initial Text', type = 'text'),
                                  html.Div(id = 'my-div',style = {'color':'red',
                                                                  'border':'2px red solid'}
                                          )
                                    ]
                                ),
                        html.Div([html.P(html.Label('Slider')),
                                  dcc.Slider(id = 'my-slider',
                                             marks={i: '{}'.format(i) for i in range(10)},
                                             min=0,
                                             max=9,
                                             value=0)
                                             ]
                                ),
                        html.P(
                        html.Div(id='my-slider-div',
                                 style = {'color':'red',
                                          'border':'2px red solid'}))
                      ],style = {'color':'black',
                               'border':'4px black solid'}
            )


@app.callback(Output(component_id = 'my-div',
                     component_property = 'children'),
              [Input(component_id = 'my-input-string',
                     component_property = 'value')])
def update_output_div(input_value):
    return "you entered : {}".format(input_value)


@app.callback(Output(component_id = 'my-slider-div',
                     component_property = 'children'),
              [Input(component_id = 'my-slider',
                     component_property = 'value')])
def update_slider_output_div(input_value):
    return "The squared value of {} is {}".format(input_value,input_value*input_value)

if __name__=='__main__':
    app.run_server()
