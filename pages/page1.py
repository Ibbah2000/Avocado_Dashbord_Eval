"""
Page 1 - Comparaison des quantités vendues
Layout : graphique fixe (6 régions) + badge + select + graphique filtrable
"""

import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import pandas as pd

# Enregistrement de la page
dash.register_page(__name__, path="/", name="Comparaison entre région")

# Chargement des données
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
df = pd.read_csv(os.path.join(BASE_DIR, "datas", "avocado.csv"))

# Régions fixes du premier graphique
REGIONS_FIXES = ["MidSouth", "Northeast", "SouthCentral", "Southeast", "TotalUS", "West"]

# Options pour le select
region_options = [{"label": r, "value": r} for r in sorted(df["region"].unique())]

layout = dbc.Container([
    dbc.Card([
        # Header de la card
        dbc.CardHeader(
            html.H4("Quantités vendues (Total Volume)", className="text-white m-0"),
            style={"backgroundColor": "#1a6ebd"},
        ),
        # Body de la card
        dbc.CardBody([
            dbc.Row([
                # Colonne 1 : graphique fixe
                dbc.Col([
                    dcc.Graph(id="graph-regions-fixes"),
                ], xs=12, md=6),

                # Colonne 2 : badge + select + graphique filtrable
                dbc.Col([
                    # Badge
                    dbc.Badge(
                        "Sélectionnez une région:",
                        color="primary",
                        className="mb-2 w-100 p-2",
                        style={"fontSize": "14px"},
                    ),
                    # Select
                    dcc.Dropdown(
                        id="select-region",
                        options=region_options,
                        value=region_options[0]["value"],
                        clearable=False,
                        className="mb-3",
                    ),
                    # Graphique filtrable
                    dcc.Graph(id="graph-region-selectionnee"),
                ], xs=12, md=6),
            ]),
        ]),
    ], className="shadow-sm"),
], fluid=True)