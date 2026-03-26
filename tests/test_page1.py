import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pages.page1_cb import update_graph_fixe, update_graph_region

# Test 1 : Vérifier que le graphique fixe contient bien les 6 régions
def test_graphique_fixe_contient_6_regions():
    fig = update_graph_fixe("Albany")
    regions_dans_fig = [trace.name for trace in fig.data]
    assert len(regions_dans_fig) == 6
    print("✅ Test 1 réussi : 6 régions dans le graphique fixe")

# Test 2 : Vérifier que les bonnes régions sont dans le graphique fixe
def test_graphique_fixe_bonnes_regions():
    fig = update_graph_fixe("Albany")
    regions_dans_fig = [trace.name for trace in fig.data]
    assert "TotalUS" in regions_dans_fig
    assert "West" in regions_dans_fig
    assert "Northeast" in regions_dans_fig
    print("✅ Test 2 réussi : bonnes régions présentes")

# Test 3 : Vérifier que le graphique filtrable change selon la région
def test_graphique_region_titre():
    fig = update_graph_region("Albany")
    assert "Albany" in fig.layout.title.text
    print("✅ Test 3 réussi : titre contient la région sélectionnée")

# Test 4 : Vérifier qu'une autre région fonctionne aussi
def test_graphique_autre_region():
    fig = update_graph_region("Atlanta")
    assert "Atlanta" in fig.layout.title.text
    print("✅ Test 4 réussi : fonctionne avec une autre région")