# Décisions Architecturales — Démonstrateur Prédictif PME

Ce document présente les grands principes d’architecture qui ont guidé la construction du moteur de prévision utilisé dans ce démonstrateur.  
Aucun détail interne du MVP réel n’est exposé: seuls les choix conceptuels sont documentés.



## 1. Validation temporelle: walk-forward strict

**Raison du choix**
- Les données PME sont temporelles et sujettes aux ruptures (saisonnalité, promotions, fériés)
- Le walk-forward est la méthode la plus fiable pour mesurer la stabilité d’un modèle dans le temps
- Il évite les fuites temporelles grâce au découpage chronologique et au gap

**Alternatives non retenues**
- Cross-validation classique → leakage assuré
- Train_test_split simple → trop éloigné des conditions réelles d’utilisation



## 2. AutoML-lite (plutôt qu’AutoML complet)

**Motivation**
- Transparence indispensable dans un contexte PME
- Coût calculatoire faible
- Facilité d’audit, reproduction et explication
- Modèles simples mais robustes (Ridge, baselines)

**Approche retenue**
- Tests multi-modèles
- Scoring principal: MASE (référence à une baseline naïve)
- Tie-breakers: MAE, RMSE, stabilité inter-splits
- Sélection automatique du candidat le plus fiable



## 3. Artefacts normalisés et reproductibles

**Objectifs**
- Rejouer un run à l’identique
- Comprendre précisément ce qui a été évalué
- Préparer la Phase 2 (monitoring, audit, API)

**Artefacts (conceptuels)**
- Summary global
- Détails par split
- Model card (hyperparamètres, features, métriques, contexte)
- Run info (hash dataset, configuration, versions)
- Visualisations clés



## 4. Séparation claire des couches: moteur → CLI → interface

**Raison**
- Le moteur doit être réutilisable dans n’importe quel environnement:
  - scripts batch
  - CLI Typer
  - API future (FastAPI)
  - interface Streamlit
  - orchestrateurs externes (Airflow, CRON, etc.)

**Principes**
- Le moteur ne dépend d’aucune UI
- La CLI n’ajoute aucune logique métier: elle orchestre uniquement
- L’interface est une couche "exposition métier" sans calcul interne



## 5. Simplicité des modèles (Phase 1)

**Pourquoi ?**
- Historique limité dans les PME
- Besoin d’explicabilité forte
- Robustesse prioritaire
- Maintenance et intégration facilitée

**Conséquence**
- Ridge, baselines, RandomForest
- Pas de deep learning en Phase 1
- Extension progressive prévue en Phase 2



## 6. Préparation à l’industrialisation (Phase 2)

Le design Phase 1 prépare déjà:
- Un endpoint `/predict` (API)
- Une prévision multi-horizon (récursif)
- Un monitoring du drift
- Des runs historisés et comparables
- Une gestion multi-séries
- Une intégration exogène enrichie (météo, calendrier, business)
- Une orchestration planifiée

Ces évolutions s’appuient sur les choix fondamentaux de reproductibilité et modularité réalisés en Phase 1.


