# Avocado Dashboard - Application Dash

Application Dash multi-pages pour l'analyse des ventes d'avocats aux États-Unis.
Projet réalisé dans le cadre du cours Dash - Université de Tours M1 MECEN 2025/2026.

## Structure du projet
```
Avocado_Dashboard_Eval/
├── app.py
├── pages/
│   ├── page1.py
│   ├── page1_cb.py
│   ├── page2.py
│   ├── page2_cb.py
│   └── page3.py
├── assets/
├── datas/
│   ├── avocado.csv
│   ├── expli1.md
│   ├── expli2.md
│   └── expli3.md
├── tests/
│   ├── test_page1.py
│   └── test_page2.py
└── README.md
```

## Installation
```bash
uv sync
```

## Lancer l'application
```bash
uv run python app.py
```

Puis ouvre : http://127.0.0.1:8050

## Lancer les tests
```bash
pytest tests/ -v
```

## Pages

| Page | URL | Description |
|------|-----|-------------|
| Comparaison entre région | `/` | Graphiques de volumes vendus |
| Affichage des données | `/page2` | Tableau filtrable |
| Aide en ligne | `/page3` | Documentation Markdown |