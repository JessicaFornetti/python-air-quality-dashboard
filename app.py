import dash
from dash import dash_table
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import pymongo

app = dash.Dash(__name__)

client = pymongo.MongoClient()
db = client.test
names = ["Paris", "London", "Madrid", "Berlin", "Amsterdam", "Moscow", "Shanghai", "Beijin", "Tokyo", "Seoul", "Hong Kong", "Singapore", "New York", "Chicago", "Boston", "LA", "Toronto", "Melbourne", "Sydney",] 

d = db.CO2.find({}, { "_id": 0, "data.city.name": 1, "data.aqi": 1})
df = pd.DataFrame(d)
df['data'] = df['data'].astype("string")
df = df.dropna()
df = df.rename(columns={"data": "requete"})
df['aqi'] = df['requete']
df['city'] = df['requete']

df2 = df.requete.str.split(':')
#print(df2)

for i in df.index:
    df['aqi'][i] = df2[i][1]
    df['city'][i] = df2[i][3]
    
df2 = df.aqi.str.replace(', \'city\'', '')
df3 = df.city.str.replace('}}', '')
    
for i in df.index:
    df['aqi'][i] = df2[i]
    df['city'][i] = df3[i]
    
df['aqi'] = df['aqi'].astype("int")

fig = px.bar(df, x="city", y="aqi", barmode="group")

app.layout = html.Div(children=[
    html.Div([
        dcc.Graph(
            id='graph1',
            figure=fig
        ),  
    ]),
    html.Div([
        dash_table.DataTable(df.to_dict('records'))
    ]),
])

if __name__ == '__main__':
    app.server.run(port=8500, host='192.168.4.38')

