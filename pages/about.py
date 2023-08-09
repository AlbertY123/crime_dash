import dash
from dash import html
import utils.theme as theme
import dash_bootstrap_components as dbc
from dash import Dash, Input, Output, callback, dcc, html,State
from utils.consts import LINKEDIN_PROFILE, GITHUB_PROFILE

dash.register_page(
    __name__,
    path='/about',
    title="About",
)
about_me_p1= """
Hi, I am Mena, my two passions are 1) data science and 2) helping others. I am so grateful that both in my current role as a data scientist and in my previous role as a uni lecturer, I got to utilize my data skills to bring values to those around me, be it my students, my teams or customers. 
"""
about_me_p2="""
This hobby project is yet another attempt to enjoy working with data and in the meantime create something useful to someone. If you are also interested in crime trend in Victoria, pls feel free to reach out and advice us on things you would like to see. 
"""
about_me_p3="""
Albert is my Year7 son who volunteered to help deploy this dashboard. I am very excited for the opportunity to work with him. For more details about how it all started, please refer to 
"""
post_url = "https://www.linkedin.com/posts/mena-ning-wang_datascience4socialgood-crimetrends-dash-activity-7086267024871456768-YRGh"


layout = html.Div(
    children=[
        dbc.Row([
            dbc.Col(className="col-sm-0 col-md-1 col-lg-1"),
            dbc.Col(className="col-sm-11 col-md-11 col-lg-10", 
                children=[
                html.Div(
                    className="card", 
                    style={"margin-left": "20px"},
                    children=[
                        html.Div(className="card-body p-0", children=[
                            html.Div(className="d-flex justify-content-between", children=[
                                html.Div(
                                    className="card-info p-4",
                                    children=[
                                        html.H3(className="card-text", children=["Who are we?"]),
                                        html.H2(
                                            className="card-text m-0 p-0",
                                            children=["Mena and Albert"],
                                            style={"color": theme.COLOR_PALLETE[0]},
                                        ),
                                        html.Div(
                                            className="mb-2 mt-2",
                                            children=[
                                                html.P(
                                                    className="card-title mb-2",
                                                    children=[
                                                        html.P(about_me_p1),
                                                        html.Br(),
                                                        html.P(about_me_p2),
                                                        html.Br(),
                                                        html.P(
                                                            [
                                                                about_me_p3,
                                                                html.A(
                                                                    "this post",
                                                                    href=post_url,
                                                                    target="_blank",
                                                                ),
                                                                ".",
                                                            ],
                                                            style={
                                                                "font-size": "1rem"
                                                            },
                                                        ),
                                                    ],
                                                    style={"font-size": "1rem"},
                                                ),
                                            ],
                                        ),
                                        html.Small(className="card-text", children=[]),
                                        html.A(
                                            href=LINKEDIN_PROFILE,
                                            target="_blank",
                                            children=[
                                                html.I(
                                                    className="bx bxl-linkedin-square mt-3",
                                                    style={
                                                        "font-size": "2.5rem",
                                                        "color": "#0a66c2",
                                                    },
                                                )
                                            ],
                                        ),
                                        html.A(
                                            href=GITHUB_PROFILE,
                                            target="_blank",
                                            children=[
                                                html.I(
                                                    className="bx bxl-github mt-3",
                                                    style={
                                                        "font-size": "2.5rem",
                                                        "color": "#0a66c2",
                                                    },
                                                )
                                            ],
                                        ),
                                    ],
                                )
                            ])
                        ])
                    ],
                    id="about_id",
                )
            ]),
        ])
    ],
)


@callback(
   Output("about_id", "style"),
   Input("color_bg", 'data'),
)

def toggle_theme(data):
    return {'background-color': str(data)}