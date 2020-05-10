import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input,Output,State

app = dash.Dash()

app.layout = html.Div([
             html.H1('Trying to controll the callbacks '),
             dcc.Input(id = 'my-input',
                        value = 0,
                        style = {'font':{'size':24}}),
             html.Button(id = 'my-button',
                         n_clicks = 0,
                         children = 'Submit',
                         style = {'font':{'size':24}}),
             html.Div(id = 'text-output',
                      style = {'color':'black'})
])


app.callback(Output('text-output','children'),
             [Input('my-button','n_clicks')],
             [State('my-input','value')])
def return_output(n_clicks,input_values):
        return(input_values)


if __name__=='__main__':
    app.run_server()
