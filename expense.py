import pandas as pd
import dash
import plotly.graph_objs as go
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

data = pd.read_csv('data.csv')

print(data.head())

app = dash.Dash()
server = app.server

app.layout = html.Div([
    html.H1(children="EXPENSE ANALYSIS", style={'color': 'black', 'text-align': 'center'}),
    html.Div(children=[
        dcc.Graph(id='scatter plot',
                  figure={'data': [go.Scatter(x=data['credit'],
                                              y=data['debit'],
                                              mode='markers')],
                          'layout': go.Layout(title='scatter plot')})],
        style={'border': '1px black solid', 'float': 'left', 'width': '49%'}),
    html.Div(children=[
        dcc.Graph(id='bar plot',
                  figure={'data': [go.Bar(x=data['debit'],
                                          y=data['category'])],
                          'layout': go.Layout(title='Bar plot',
                                              xaxis={'title': 'Expense'},
                                              yaxis={'title':'category'})})
    ],
             style={'border': '1px black solid', 'float': 'left', 'width': '49%'})
])

if __name__ == '__main__':
    app.run_server()
