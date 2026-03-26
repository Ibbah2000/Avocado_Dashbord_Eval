

import dash
from dash import Dash, html
import dash_bootstrap_components as dbc

# Initialisation de l'application
app = Dash(
    __name__,
    use_pages=True,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True,
)

# Barre de navigation
navbar = dbc.Navbar(
    dbc.Container([
        dbc.NavbarBrand("Application des M1 MECEN"),
        dbc.Nav([
            dbc.NavItem(dbc.NavLink("Comparaison entre région", href="/")),
            dbc.NavItem(dbc.NavLink("Affichage des données", href="/page2")),
            dbc.NavItem(dbc.NavLink("Aide en ligne", href="/page3")),
        ], navbar=True, className="ms-auto"),
    ], fluid=True),
    color="primary",
    dark=True,
)

# Layout principal
app.layout = html.Div([
    navbar,
    dash.page_container,
])

if __name__ == "__main__":
    app.run(debug=True)