"""
Page 3 - Présentation Dash via Tabs
Affiche le contenu des fichiers expli1.md, expli2.md, expli3.md
"""

import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import os

dash.register_page(__name__, path="/page3", name="Aide en ligne")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_markdown(filename):
    """Charge le contenu d'un fichier Markdown."""
    filepath = os.path.join(BASE_DIR, "datas", filename)
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

# Chargement des fichiers Markdown
md1 = load_markdown("expli1 (1).md")
md2 = load_markdown("expli2.md")
md3 = load_markdown("expli3.md")

layout = dbc.Container([
    dbc.Card([
        # Header
        dbc.CardHeader(
            html.H4("Présentation de Dash", className="text-white m-0"),
            style={"backgroundColor": "#6b1a1a"},
        ),
        # Body avec Tabs
        dbc.CardBody([
            dbc.Tabs([
                dbc.Tab(
                    dcc.Markdown(md1),
                    label="Accueil",
                    tab_id="tab-1",
                ),
                dbc.Tab(
                    dcc.Markdown(md2),
                    label="Layout",
                    tab_id="tab-2",
                ),
                dbc.Tab(
                    dcc.Markdown(md3),
                    label="CallBack",
                    tab_id="tab-3",
                ),
            ], active_tab="tab-1"),
        ]),
    ], className="shadow-sm"),
], fluid=True)