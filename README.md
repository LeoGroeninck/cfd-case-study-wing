# Mini-projet CFD — Démonstration

Ce dépôt contient un mini-projet CFD pour démonstration, illustrant les notions de base de la mécanique des fluides et de l’aérodynamique.

## Structure

- `src/demo_cfd.py` : script Python générant une courbe polaire simplifiée.  
- `notebooks/01_demo.ipynb` : notebook interactif reprenant le même calcul.  
- `figures/`, `data/`, `results/` : dossiers pour stocker résultats et figures (avec `.gitkeep`).  
- `docker/Dockerfile` : environnement Docker pour la reproductibilité.

## Installation

1. Crée un environnement virtuel Python (optionnel mais recommandé) :  
```bash
python -m venv venv
source venv/bin/activate  # sur Mac/Linux
venv\Scripts\activate     # sur Windows
