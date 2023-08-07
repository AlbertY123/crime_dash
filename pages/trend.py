#from __future__ import annotations
import pandas as pd
import pathlib
import re
import plotly.express as px
import dash
import warnings
from dash import dcc, html, callback
from dash_bootstrap_templates import load_figure_template
import dash_bootstrap_components as dbc
import dash_loading_spinners as dls
from dash.dependencies import Input, Output


# dash.register_page(__name__, path='/', name='EDA')
dash.register_page(
    __name__,
    path='/trend',
    title="Trend",
)

load_figure_template("minty")


warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.simplefilter(action="ignore", category=pd.errors.PerformanceWarning)

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("data").resolve()

#  axis formatting
axis_font = dict(
        showline=True,
        showgrid=False,
        showticklabels=True,
        linecolor='rgb(204, 204, 204)',
        zeroline=False,
        linewidth=2,
        ticks='outside',
        tickfont=dict(
            family='San-Serif',
            size=12,
            # color='black',
        ),
    )

def wrangle_LGA(file):
    df = pd.read_excel(file, sheet_name = 'Table 01')
    df['LGA'] = df['Local Government Area']
    df['LGA'] = df['LGA'].str.strip()
    df['Incidents_Rate'] = round(df['Rate per 100,000 population'])
    wanted_fields = ['Year', 'LGA', 'Incidents_Rate']
    df = df[wanted_fields]
    df = df.drop_duplicates()
    return df

def wrangle_LGA_subdivision(file):
    df = pd.read_excel(file, sheet_name = 'Table 02' )
    df['LGA'] = df['Local Government Area']
    df['LGA'] = df['LGA'].str.strip()
    df['Offence_Division'] = df['Offence_Division'].str.strip()
    df['LGA_Population'] = 100000 * df['Incidents_Recorded']/df['LGA Rate per 100,000 population']
    df['Division_Incidents'] = df.groupby(['Year', 'LGA', 'Offence_Division'])['Incidents_Recorded'].transform('sum')
    df['Division_Incidents_Rate'] = round(100000* df['Division_Incidents']/df['LGA_Population'])
    wanted_fields = ['Year', 'LGA', 'Offence_Division', 'Division_Incidents_Rate']
    df = df[wanted_fields]
    df = df.drop_duplicates()
    return df

df = wrangle_LGA(DATA_PATH.joinpath('Data_Tables_LGA_Criminal_Incidents_Year_Ending_March_2023.xlsx'))
df2 = wrangle_LGA_subdivision(DATA_PATH.joinpath('Data_Tables_LGA_Criminal_Incidents_Year_Ending_March_2023.xlsx'))

lab_var = {x:' '.join(re.findall('[a-zA-Z][^A-Z]*', x)).title()  for x in df.columns[1:]}

layout = dbc.Container(
    [   
        # ======================= Title
        dbc.Row(
            [
                dbc.Col([
                    html.H2(
                        "Crime Trend across LGAs in Victoria",
                        style={"font-weight": "bold","color": "#B1384B"},
                        className="text-center mb-4",
                    ),
                ]
                ),
            ]
        ),
        
         # ======================  trend charts
        html.Div(
            [
                dbc.Col(className="col-md-0 col-lg-1"),
                dbc.Col(
                        [html.H4("Choose LGAs to Explore"),
                        dcc.Dropdown(
                            className="my-dropdown",
                            id='lga-dropdown',
                            options=[{'label': lga, 'value': lga} for lga in df['LGA'].unique() if lga != "Total"],
                            value=df['LGA'].unique()[0:1],
                            multi=True,),
                        dcc.Graph(id='lga-incident-graph'),
                        html.Br(),
                        html.H4("Choose Offence Division"),
                        dcc.Dropdown(
                            className="my-dropdown",
                            id = 'offence-division-dropdown',
                            options=[{'label': offence, 'value': offence} for offence in df2['Offence_Division'].unique()],
                            value=df2['Offence_Division'].unique()[0]),
                        dcc.Graph(id='division-incident-graph'),
                        ],
                        className="col-md-12 col-lg-10  card-chart-contain",
                        ),
            ],
            className="row flex-display",
        ),       
    ]
)

# ----------------------------------- Graph I on LGA Trend ---------------------------------------
@callback(
    Output('lga-incident-graph', 'figure'),
    Input('lga-dropdown', 'value')
)
def update_graph(selected_lga):
    filtered_df = df[df['LGA'].isin(selected_lga)]
    fig = px.line(filtered_df, x='Year', y='Incidents_Rate', color='LGA')
    fig.update_layout(
        yaxis_title = "Rate per 100K population",
        template = "plotly_dark",
        xaxis_title = "",
        margin = dict(b=0)
        )
    return fig

# ---------------------------------- Graph II on Incident by Division ------------------------------
@callback(
    Output('division-incident-graph', 'figure'),
    Input('lga-dropdown', 'value'),
    Input('offence-division-dropdown', 'value')
)
def update_graph(selected_lga, selected_division):
    filtered_df = df2[df2['LGA'].isin(selected_lga)]
    filtered_df = filtered_df[filtered_df['Offence_Division']==selected_division]
    fig = px.line(filtered_df, x='Year', y='Division_Incidents_Rate', color='LGA')
    fig.update_layout(
        yaxis_title = "Rate per 100K population",
        template = "plotly_dark",
        xaxis_title = "",
        margin = dict(b=0)
        )
    return fig