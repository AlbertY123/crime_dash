import dash
from dash import dcc, html
import dash_bootstrap_components as dbc

dash.register_page(
    __name__,
    path='/summary',
    title="Summary",
)

layout = dbc.Container(
    dbc.Row([ 
        dbc.Col(className="col-md-0 col-lg-1"),
        dbc.Col([ 
            html.Br(), html.Br(),
            html.H3("App Toc"),
            html.Hr(),

            dcc.Markdown('''            
            
            The app consists of five sections:
            - `Welcome`: Welcome page.
            - `Crime Trend`: Crime trend across LGAs in Victoria.
            - `Insights`: Ranking of LGAs with the most increase and decrease in crime. 
            - `Summary`: This section offers a summary of the app. You are here 😎
            - `About`: Who are we?

            '''),

            html.Br(),

            html.H5("References:"),

            html.Hr(),

            dcc.Markdown(link_target="_blank" ,
           children=[ '''
           - Template originaly come from [Ivan Abboud](https://www.linkedin.com/in/ivan-abboud-737b2120a/) with is project [Fifa Worldcup Dashboard](http://ivan96.pythonanywhere.com/)
           - Data source: [Crime Statistics Agency](https://www.crimestatistics.vic.gov.au/about-the-data)
                     ''']
           )
        ])
    ])
)
