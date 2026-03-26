"""
Page 2 - Affichage des données en tableau
Layout : dropdown région + RadioItems type + badge compteur + tableau
"""

import dash
from dash import html, dcc, dash_table
import dash_bootstrap_components as dbc
import pandas as pd
import os

dash.register_page(__name__, path="/page2", name="Affichage des données")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
df = pd.read_csv(os.path.join(BASE_DIR, "datas", "avocado.csv"))

COLUMNS_TO_HIDE = ["Unnamed: 0", "4046", "4225", "4770", "Small Bags", "Large Bags", "XLarge Bags"]
DISPLAY_COLUMNS = [col for col in df.columns if col not in COLUMNS_TO_HIDE]

region_options = [{"label": r, "value": r} for r in sorted(df["region"].unique())]

layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.Label("Sélectionner une région:"),
            dcc.Dropdown(
                id="dropdown-region-p2",
                options=region_options,
                value=region_options[0]["value"],
                clearable=False,
            ),
        ], xs=12, md=5),
        dbc.Col([
            html.Label("Sélectionner un type:"),
            dcc.RadioItems(
                id="radio-type-p2",
                options=[
                    {"label": " Tous", "value": "Tous"},
                    {"label": " conventional", "value": "conventional"},
                    {"label": " organic", "value": "organic"},
                ],
                value="Tous",
                inline=True,
            ),
        ], xs=12, md=5),
        dbc.Col([
            dbc.Badge(
                id="badge-lignes",
                color="primary",
                className="mt-3 p-2",
            ),
        ], xs=12, md=2, className="d-flex align-items-center"),
    ], className="mb-3"),

    dash_table.DataTable(
        id="data-table-p2",
        columns=[{"name": col, "id": col} for col in DISPLAY_COLUMNS],
        data=df[DISPLAY_COLUMNS].to_dict("records"),
        page_size=10,
        sort_action="native",
        style_header={
            "backgroundColor": "#1a6ebd",
            "color": "white",
            "fontWeight": "bold",
        },
        style_cell={
            "textAlign": "left",
            "padding": "8px",
        },
        style_data_conditional=[
            {
                "if": {"row_index": "odd"},
                "backgroundColor": "#f8f9fa",
            }
        ],
    ),
], fluid=True)