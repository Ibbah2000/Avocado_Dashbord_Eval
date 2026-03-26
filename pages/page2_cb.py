"""
Page 2 - Callbacks
Filtre le tableau selon la région et le type sélectionnés
Met à jour le badge compteur de lignes
"""

from dash import Input, Output, callback
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
df = pd.read_csv(os.path.join(BASE_DIR, "datas", "avocado.csv"))

COLUMNS_TO_HIDE = ["Unnamed: 0", "4046", "4225", "4770", "Small Bags", "Large Bags", "XLarge Bags"]
DISPLAY_COLUMNS = [col for col in df.columns if col not in COLUMNS_TO_HIDE]


@callback(
    Output("data-table-p2", "data"),
    Output("badge-lignes", "children"),
    Input("dropdown-region-p2", "value"),
    Input("radio-type-p2", "value"),
)
def update_table(region, avocado_type):
    """Filtre le tableau et met à jour le badge."""
    filtered = df.copy()

    if region:
        filtered = filtered[filtered["region"] == region]

    if avocado_type and avocado_type != "Tous":
        filtered = filtered[filtered["type"] == avocado_type]

    nb_lignes = len(filtered)
    badge_text = f"Lignes: {nb_lignes}"

    return filtered[DISPLAY_COLUMNS].to_dict("records"), badge_text