import dash
#import dash_core_components as dcc
from dash import dcc
#import dash_html_components as html
from dash import html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc


import plotly.express as px
import plotly.graph_objects as go

import numpy as np
import pandas as pd
import json

# Before read data, you must run prepare_data.py
try:
  df_states = pd.read_csv("states.csv")
  df_brasil = pd.read_csv("brasil.csv")
except FileNotFoundError:
  raise SystemExit("Before run the Dashboard, you must run 'prepare_data.py'.")

df_states_ = df_states[df_states["data"] == "2020-05-13"]

brazil_states = json.load(open("geojson/brazil_geo.json", "r"))


# ============================================================
# Map Configuration
# ============================================================
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

fig = px.choropleth_mapbox(df_states_, locations="estado", color="casosNovos",
            center={"lat": -16.95, "lon": -47.78}, zoom=4,
            geojson=brazil_states, color_continuous_scale="Redor", opacity=0.4,
            hover_data={"casosAcumulado": True, "casosNovos": True, "obitosNovos": True, "estado": True})

fig.update_layout(
  paper_bgcolor = "#242424",
  autosize = True,
  margin = go.Margin(l=0, r=0, t=0, b=0),
  showlegend = False,
  mapbox_style = "carto-darkmatter"
)


app.layout = dbc.Container(
  dbc.Row([
    dbc.Col([
      dcc.Graph(id="choropleth-map", figure=fig)
    ])
  ])
)



if __name__ == "__main__":
  app.run_server(debug=True)
