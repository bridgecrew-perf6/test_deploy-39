
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

def init_dashboard(server):

    # INIT DASHAPP
    dash_app = dash.Dash(server=server,
                         title="Your Dashboard",
                         routes_pathname_prefix="/dashboard/")
    server = dash_app.server

    dash_app.layout = html.Div(children=[
        html.H1(children='Dashboard'),
    ])