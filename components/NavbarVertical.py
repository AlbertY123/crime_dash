from dash import html
import dash_bootstrap_components as dbc

sidebar = html.Div(
    [
        html.Div(
            [
                html.Img(src="./assets/images/crime_stopper.gif", style={"width": "4rem"}),
                html.H4(" Crime Dash", className="m-0"),
            ],
            className="sidebar-header",
        ),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink(
                    [
                        html.I(className="menu-icon tf-icons bx bx-home"), 
                        html.Span("Welcome")],
                    href="/",
                    active="exact",
                    className="pe-4",
                ),
                dbc.NavLink(
                    [
                        html.I(className="menu-icon tf-icons bx bx-bar-chart-square"),
                        html.Span("Crime Trend"),
                    ],
                    href="/trend",
                    active="exact",
                    className="pe-4"
                ), 
                dbc.NavLink(
                    [
                        html.I(className="menu-icon tf-icons bx bx-bulb"),
                        html.Span("Insights"),
                    ],
                    href="/insights",
                    active="exact",
                    className="pe-4"
                ),             
                dbc.NavLink(
                    [
                        html.I(className="menu-icon tf-icons bx bxs-file"),
                        html.Span("Summary"),
                    ],
                    href="/summary",
                    active="exact",
                    className="pe-4",
                ),
                dbc.NavLink(
                    [
                        html.I(className="menu-icon tf-icons bx bx-info-circle"),
                        html.Span("About"),
                    ],
                    href="/about",
                    active="exact",
                    className="pe-4",
                ),
                
                dbc.NavItem(html.A(
                                html.Img(
                                    id='theme-btn',
                                    n_clicks=0,
                                    src="./assets/images/moon.svg", height="20px",
                                    style={"margin": "14px"},
                                ),
                            ),
                        ),
                dbc.Tooltip("Dark Theme", target="theme-btn",placement='right',id='L_tip',),                
            ],
            vertical=True,
            pills=True,
        ),
    ],
    id="bg_id",
    className="sidebar",
)

