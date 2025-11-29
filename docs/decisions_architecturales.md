
## Décisions Architecturales — Démonstrateur Prédictif PME

Ce document décrit les grands choix qui ont guidé la construction du moteur de prévision présenté dans ce repo vitrine. Il ne contient aucune logique interne du MVP réel, uniquement les principes.

## 1. Walk-forward comme validation centrale

#### Pourquoi ce choix ?
- Les données PME sont temporelles.
- Les ruptures sont fréquentes (jours fériés, saison, promos).
- Le walk-forward est la méthode la plus robuste pour mesurer la stabilité.
#### Alternatives envisagées
- Cross-validation classique → non pertinente pour séries temporelles.
- Train_test_split simple → insuffisamment représentatif.

## 2. AutoML-lite plutôt qu’AutoML complet

#### Pourquoi ?
- Transparence indispensable pour un contexte métier
- Faible coût calculatoire
- Facilité d’audit et d’explication
- Sélection de modèles simples mais robustes (Ridge, Naïve…)
#### Approche retenue
- tests multi-modèles
- scoring MAE
- tie-breaker stabilité (variance inter-splits)

## 3. Artefacts normalisés

#### Pourquoi ?
- Reproductibilité
- Auditabilité
- Documentation automatique
- Préparation à la Phase 2 (API + monitoring)
#### Artefacts choisis (conceptuellement)
- résumé global
- détails par split
- “model card”
- visualisations clé
- configuration du run

## 4. Séparation claire : moteur → interface

#### Objectif
Permettre :
- un moteur réutilisable dans n’importe quel environnement,
- une interface Streamlit simple,
- une API future (FastAPI),
- des scripts automatiques (batch).

Le moteur ne dépend d’aucune UI.

## 5. Simplicité des modèles (Phase 1)

#### Pourquoi pas de deep learning ou modèles complexes ?

- Historique limité dans les PME
- Besoin d’interprétation
- Notion de robustesse prioritaire
- Optimisation de la maintenance du pipeline

Des extensions plus complexes sont prévues Phase 2

## 6. Préparation à une API future

Le démonstrateur est pensé pour évoluer vers :
- un endpoint `/predict`
- un monitoring du drift
- une gestion multi-horizon
- un historique de runs
- une orchestration planifiée

Les choix Phase 1 préparent déjà ce futur.

