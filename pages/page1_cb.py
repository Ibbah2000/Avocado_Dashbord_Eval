"""
Page 1 - Callbacks
Met à jour les graphiques selon la région sélectionnée
"""

from dash import Input, Output, callback
import plotly.express as px
import pandas as pd
import os

# Chemin correct vers le fichier CSV
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
df = pd.read_csv(os.path.join(BASE_DIR, "datas", "avocado.csv"))
df["Date"] = pd.to_datetime(df["Date"])

# Régions fixes du premier graphique
REGIONS_FIXES = ["Midsouth", "Northeast", "SouthCentral", "Southeast", "TotalUS", "West"]

@callback(
    Output("graph-regions-fixes", "figure"),
    Input("select-region", "value"),
)
def update_graph_fixe(region):
    """Graphique fixe avec les 6 régions principales."""
    filtered = df[df["region"].isin(REGIONS_FIXES)].sort_values("Date")
    fig = px.line(
        filtered,
        x="Date",
        y="Total Volume",
        color="region",
        title="Quantités vendues - Régions principales",
        labels={"Total Volume": "Volume total", "Date": "Date"},
    )
    fig.update_layout(margin=dict(l=40, r=20, t=50, b=40))
    return fig


@callback(
    Output("graph-region-selectionnee", "figure"),
    Input("select-region", "value"),
)
def update_graph_region(region):
    """Graphique filtrable selon la région sélectionnée."""
    filtered = df[df["region"] == region].sort_values("Date")
    fig = px.line(
        filtered,
        x="Date",
        y="Total Volume",
        title=f"Quantités vendues - {region}",
        labels={"Total Volume": "Volume total", "Date": "Date"},
    )
    fig.update_layout(margin=dict(l=40, r=20, t=50, b=40))
    return fig