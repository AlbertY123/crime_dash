import dash
from dash import html
import dash_bootstrap_components as dbc
from utils.consts import LINKEDIN_PROFILE
from dash import Dash, Input, Output, callback, dcc, html,State

dash.register_page(
    __name__,
    path='/',
    title="Welcome",
    # name="Home",
    # image="metatag-image.png",
    description="Dash app to explore victorial crime data."
)

layout = html.Div([
    html.Div([
        dbc.Row([
            dbc.Col(className="col-sm-0 col-md-1 col-lg-1"),
            dbc.Col(className="col-sm-11 col-md-11 col-lg-10", children=[
                html.Div(
                    className="mb-md-0 mb-4 card-chart-container",
                    children=[
                        dbc.Row([
                            dbc.Col(
                                className="col-lg-6",
                                children=[
                                    html.Div(
                                        className="card-header card-m-0 me-2 pb-3",
                                        children=[
                                            html.H2(
                                                ["Victoria Crime Dashboard"],
                                                style={"font-size": "2vw"},
                                            ),
                                            html.Span(
                                                "stats from crimestatistics.vic.gov.au",
                                                style={
                                                    "color": "LightSeaGreen",
                                                    "font-size": "1.5vw",
                                                },
                                            ),
                                        ],
                                    ),
                                    html.Div(
                                        [
                                            html.P(
                                                "Welcome to victoria crime dashboard!",
                                                className="mt-1",
                                            ),
                                            html.P(
                                                "Here, we utilize data from Crime Statistics Agency (www.crimestatistics.vic.gov.au) to reveal crime trends cross all LGAs in Victoria, Australia where data is available.",
                                                className="mt-1",
                                                style={"textAlign": "justify"},
                                            ),
                                            html.P(
                                                [
                                                    "Learn more about the data from ",
                                                    html.A(
                                                        "Crime Statistics Agency",
                                                        href="https://www.crimestatistics.vic.gov.au/about-the-data",
                                                        target="_blank",
                                                    ),
                                                ],
                                                className="mt-1",
                                            ),
                                        ],
                                        className="me-4 mb-0 mt-4",
                                    ),
                                    html.P(
                                        [
                                            "If you have any questions or need assistance, please don't hesitate to reach out to ",
                                            html.A(
                                                "Mena Ning Wang",
                                                href=LINKEDIN_PROFILE,
                                                target="_blank",
                                            ),
                                        ],
                                        className="me-4 mb-0 mt-4",
                                    ),
                                    html.Br(),
                                ],
                            ),
                            dbc.Col(
                                className="col-lg-3 col-md-4 col-sm-5",
                                children=[
                                    html.Img(
                                        src="./assets/images/crime_stopper.gif",
                                        className="img-fluid",
                                    ),
                                ],
                            ),
                        ]),
                    ],
                    id="wel",
                ),
            ]),
        ]),
    ]),
], style={"padding-top": "40px"})


@callback(
   Output("wel", "style"),
   Input("color_bg", 'data'),
)

def toggle_theme(data):
    return {'background-color': str(data)}