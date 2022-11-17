import pandas as pd 
import dash
from dash.dependencies import Input, Output
from dash import dcc
from dash import html
import plotly.graph_objs as go
# urlfile = 'https://github.com/otieno-okoko/ontario_groundwater/blob/main/southontario_gw.csv'
# df = pd.read_csv(urlfile, sep=',', encoding = 'latin1')
urlfile ='https://raw.githubusercontent.com/otieno-okoko/ontario_groundwater/main/southontario_gw.csv'
df = pd.read_csv(urlfile, error_bad_lines=False, encoding='latin-1')
# df = pd.read_csv("D:/my_dash_app/Ontario_GW_data.csv")

app = dash.Dash()
features = df.columns 

app.layout = html.Div([
html.Div([
dcc.Dropdown(id= 'xaxis', options=[{'label': i, 'value':i} for i in features],
value ='Rock_elevation_mASL')
], style={'width':'48%','display':'inline-block'}),
html.Div([dcc.Dropdown(id= 'yaxis', options=[{'label': i, 'value':i} for i in features],
value ='pH') ],style={'width':'48%','display':'inline-block'}), dcc.Graph(id = 'feature-graphic')
], style={'padding':10})


@app.callback(Output('feature-graphic', 'figure'),
[Input('xaxis', 'value'), Input('yaxis', 'value')])
def update_graph(xaxis_name, yaxis_name):
    return{'data':[go.Scatter(x=df[xaxis_name], y= df[yaxis_name], 
    text=df['Sample'], mode = 'markers',marker={'size': 15})], 
    'layout': go.Layout (title = 'Ambient Groundwater Geochemical Data for Southern Ontario,2007–2019', 
    xaxis={'title':xaxis_name},yaxis={'title':yaxis_name})}

if __name__ == '__main__':
    app.run_server()
