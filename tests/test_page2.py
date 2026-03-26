import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pages.page2_cb import update_table

# Test 1 : Vérifier que le filtre par région fonctionne
def test_filtre_region():
    data, badge = update_table("Albany", "Tous")
    for ligne in data:
        assert ligne["region"] == "Albany"
    print("✅ Test 1 réussi : filtre par région fonctionne")

# Test 2 : Vérifier que le filtre par type fonctionne
def test_filtre_type():
    data, badge = update_table("Albany", "organic")
    for ligne in data:
        assert ligne["type"] == "organic"
    print("✅ Test 2 réussi : filtre par type fonctionne")

# Test 3 : Vérifier que le badge affiche le bon nombre de lignes
def test_badge_lignes():
    data, badge = update_table("Albany", "Tous")
    assert "Lignes:" in badge
    assert str(len(data)) in badge
    print("✅ Test 3 réussi : badge affiche le bon nombre")

# Test 4 : Vérifier que Tous retourne les deux types
def test_filtre_tous():
    data, badge = update_table("Albany", "Tous")
    types = set(ligne["type"] for ligne in data)
    assert len(types) == 2
    print("✅ Test 4 réussi : Tous retourne bien les 2 types")