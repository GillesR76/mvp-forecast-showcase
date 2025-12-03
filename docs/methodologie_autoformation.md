# Méthodologie d’auto-formation - Vers un moteur prédictif PME en 6 semaines
<br>

# Executive Summary

De début septembre jusqu’au 20 novembre 2025, j’ai suivi un programme intensif d’auto-formation qui m’a conduit de l’acquisition progressive des fondamentaux data à la conception, l’industrialisation et la publication d’un MVP complet de moteur de prévision dédié aux PME. Ce MVP s'inscrit dans une vision plus large qui prendra forme lors d'une phase 2: construire une solution IA prête à l'emploi au service des PME. Mon parcours auto-formation/MVP a été organisé en 5 étapes: 
fondamentaux Python/EDA, machine learning supervisé, séries temporelles, industrialisation du pipeline, puis Capstone orienté MVP (release v0.1.0).

L’apprentissage a reposé sur une combinaison méthodique de trois piliers:
- Jupyter pour l’expérimentation concrète,
- Obsidian pour une documentation vivante (112 notes structurées),
- Un projet ChatGPT persistant utilisé comme assistant d’ingénierie, dans une posture active et critique (relectures, corrections, détection de fuites, refactorings). L’IA a servi de copilote: toutes les décisions architecturales, validations et implémentations finales ont été réalisées manuellement.

Le pivot du Jour 13 (Fenêtrage ML) a transformé la formation en un véritable projet logiciel: naissance des modules make_supervised(), evaluate_walkforward(), introduction des baselines, artefacts normalisés, validation temporelle stricte, puis CLI Typer, CI GitHub Actions, interface Streamlit et AutoML-lite.

Ce parcours a permis de maîtriser l’ensemble du cycle d’un moteur prédictif moderne: préparation des données, validation temporelle, architecture Python modulaire, reproductibilité, tests, industrialisation et restitution métier.
Le résultat final est un MVP complet, reproductible et aligné avec les standards professionnels — première étape du futur moteur industrialisable (Phase 2).  
<br>

---


# 1. Progression en 5 étapes

J'ai initialement structuré mon apprentissage autour d'un programme académique détaillé par semaines et par jours. Cependant, ma progression réelle ne s'est pas alignée strictement sur ce découpage. J'ai donc fait évoluer ce programme vers un système de paliers d'apprentissage articulés autour de cinq étapes.

## Étape 1 — Fondamentaux Python, Statistiques et EDA

Durée réelle: environ 10 à 12 jours

Objectif: reconstruire un socle solide pour manipuler efficacement les données.

Contenus travaillés:
- Pandas, NumPy, Matplotlib
- Statistiques descriptives appliquées (moyenne, variance, distributions, corrélations)
- Nettoyage: valeurs manquantes, outliers, doublons
- Visualisation avancée (Seaborn, Plotly)
- Mini-projets d’exploration de données sur un dataset de ventes

Production notable:
- Premiers notebooks (ex. `Jour1_Matin_Python_Data.ipynb`)
- Structuration initiale d’Obsidian: notes, tags, premières synthèses
- Mise en place des guides pivot (préprocessing, métriques, validation)

## Étape 2 — Apprentissage supervisé et premiers modèles

Durée réelle: environ 10 à 12 jours

Objectif: comprendre les modèles fondamentaux et la logique des pipelines sklearn.

Contenus travaillés:

- Régression linéaire simple et multiple
- Régressions régularisées (Ridge, Lasso, ElasticNet)
- Arbres de décision et RandomForest
- Split train/test et validation croisée
- Métriques: MAE, RMSE, R²
- Cas pratique de maintenance prédictive
    
Cette étape a été plus longue qu’initialement prévu, car j’y ai approfondi les hyperparamètres, l’interprétation des résultats et les comportements des modèles sur différents jeux de données.


## Étape 3 — Séries temporelles et pivot vers le MVP

Durée réelle: environ une semaine

Le programme initial prévoyait une exploration panoramique des séries temporelles (ARIMA, ETS, Prophet, etc.).  
Cependant, le travail effectué dans le notebook de fenêtrage ML du jour 13 a constitué un tournant décisif.

Ce notebook a représenté un premier marqueur: il a fait évoluer ma progression qui était jusque là purement académique vers une orientation produit. Cela m'a amené à générer une note de réorganisation que j'ai intégrée dans le fond documentaire du projet Chatgpt afin de restructurer toutes les étapes à venir sur la construction du MVP. 

Travaux réalisés:

- Transformation de séries temporelles en dataset supervisé (lags, rollings)
- Tests approfondis sur plusieurs modèles
- Analyse des erreurs et stabilité temporelle
- Détection et correction de leakage
- Premiers invariants temporels (index cohérents, alignements, causalité)
- Exploration de la modularité future du pipeline
    
## Étape 4 — Industrialisation du pipeline

Durée réelle: environ une semaine

Objectif: transformer les expérimentations du jour 13 en un moteur modulaire et réutilisable.

Travaux réalisés:

- Extraction du code des notebooks vers des modules structurés (`src/`)
- Développement de `make_supervised()` (lags, rollings, exogènes)
- Création de `evaluate_walkforward()` (validation temporelle stricte)
- Intégration systématique des baselines
- Normalisation des métriques (MAE, sMAPE, MASE)
- Heuristique robuste pour `train_min`
- Premiers artefacts: `summary.csv`, `details.csv`
- Début de la logique d’AutoML-lite
- Pré-intégration Streamlit (upload CSV, évaluation, visualisation)
    
C’est dans cette étape que s’opère la transition la plus marquante du parcours: je ne travaille plus uniquement en notebook, mais je commence à construire les briques du moteur de prévision avec pour objectif la mise en place d'un pipeline industrialisé. 

## Étape 5 — Capstone MVP

Durée réelle: environ une semaine et demie

Objectif: transformer le pipeline industrialisé en un MVP complet, reproductible et démontrable.

Travaux réalisés:

- Packaging (structure `src/`, `pyproject.toml`)
- Validation de schémas (Pydantic/Pandera)
- Développement d’une CLI Typer (évaluation, sélection modèle, prédiction)
- Mise en place de la CI GitHub Actions 
- Et validation systématique de la CI après chaque push
- Export d’artefacts enrichis: `model_card.json`, `run_info.json`
- Finalisation AutoML-lite
- Amélioration de l’intégration exogène
- Interface Streamlit fonctionnelle
- Documentation technique et utilisateur
- Release officielle `v0.1.0`

Cette étape clôt la Phase 1 avec un pipeline reproductible, traçable, équipé d’artefacts normalisés, et prêt à évoluer vers une Phase 2 orientée API, déploiement et monitoring.
<br></br>

---

# 2. Exemple concret: notebook sur le fenêtrage ML 

Le jour 13 a constitué un tournant décisif dans la progression. Alors que le programme prévoyait une simple introduction au fenêtrage ML pour séries temporelles, j'ai souhaité approfondir l'apprentissage et la mise en pratique en utilisant un dataset plus fournit et complexe que celui proposé pour l'exercice. Cela m'a amené à travailler beaucoup plus longtemps que prévu sur ce notebook, mais c'est ce travail qui a servit de pivot vers le futur moteur de prévision: il a initié le passage d’une approche exploratoire en notebook à la construction des premières briques du moteur de prévision. 

Dans ce notebook j'ai: 

**1. Transformé la série temporelle en dataset supervisé complet**
- Création de lags multiples
- Premières rolling features causales (moyenne, min, max)
- Alignement strict des index temporels
- Gestion des valeurs manquantes introduites par le fenêtrage
    

**2. Mené des expérimentations approfondies sur les modèles ML**
- Entraînement et tuning d’un RandomForestRegressor
- Comparaison avec des modèles linéaires régularisés
- Evaluation des performances vs baseline naïve
- Tests successifs de différentes combinaisons de features
    

**3. Identifié et corrigé des problèmes critiques en production**
- Apparition de fuite temporelle due à l’ordre des transformations
- Instabilité des performances entre deux fenêtres adjacentes
- Comportements différents selon la profondeur des arbres et le nombre de features
- Effets indésirables sur les rollings en présence de séries courtes
- Nécessité de définir un train_min robuste
    

**4. Renforcé ma compréhension des couches structurantes du futur moteur**
- Importance d’un module dédié `make_supervised()` pour garantir la causalité
- Confirmation que la validation classique train/test était insuffisante
- Nécessité d’un walk-forward strict pour mesurer la stabilité temporelle
- Introduction de baselines systématiques comme point d’ancrage
- Emergence du besoin d’artefacts (summary, details, graphes de performance)
<br></br>
---

# 3. Les trois piliers méthodologiques

## Pilier 1 — Jupyter: expérimentation

Chaque concept a d’abord été exploré dans un notebook. Le processus standard était: expérimenter, analyser, puis transformer en code modulaire lorsque pertinent.

Exemples:

- Stats appliquées (J1 à J3)
- Tuning de modèles ML (J9 à J12)
- Notebook pivot de fenêtrage ML (J13)
- Construction initiale du pipeline (J14 à J15)

## Pilier 2 — Obsidian: base de connaissances

A partir du travail effectué sur les notebooks et de l'approfondissement théorique, j'ai utilisé Obsidian comme mémoire technique et conceptuelle. Cette base a été fondamentale dans mon apprentissage et ma progression, en me servant de référence documentaire sur laquelle j'ai pu m'appuyer tout au long de mon parcours. 

### 1. Organisation

- 112 notes réparties en quatre familles: code expliqué, synthèses, concepts, cheatsheets
- Tags hiérarchiques normalisés
- Index dynamique `.base` pour la navigation rapide
- Exemples de notes: 
    - Concepts & méthodes (Concepts & méthodes/Modèles de classification/Tuning des hyperparamètres)
    - Synthèses transversales (Synthèses transversales/Notes de synthèse/L'inférence en modélisation prédictive)

### 2. Structure

```
├──Base de connaissances
│   ├──Code expliqué
│   ├──Synthèses transversales
|   │   ├──Notes de synthèse (guides pivot)
|   │   └──Notes de raccordement
│   ├──Concepts & méthodes
|   │   ├──Modèles de régression linéaire
|   │   ├──Modèles de classification
|   │   └──Séries temporelles
|   |       └──Modèles
│   ├──Cheatsheets & fondamentaux
└──Notes de cadrage auto-formation
```

### 3. Exemple de note: Fenêtrage ML — Séries temporelles supervisées

Cette note illustre le format typique utilisé dans Obsidian pour documenter un concept clé lié au pipeline du MVP.

**1. Objectif de la note**

* Transformer une série temporelle en dataset supervisé exploitable par un modèle ML.
* Documenter les bonnes pratiques (lags, rollings, exogènes, calendrier).
* Comprendre l’impact du fenêtrage sur la causalité et la performance du modèle.
* Préparer les fondations du futur module `make_supervised()`.

**2. Concept général**

La transformation repose sur la création de **lags** (valeurs passées) et éventuellement de **rolling features**.

Extrait conceptuel de la note:

> Le fenêtrage consiste à convertir la dépendance temporelle en dépendance tabulaire.
> Chaque ligne devient une observation utilisable par un modèle supervisé.
> Respect strict de la causalité: aucune valeur future ne doit être incluse.

Schéma ASCII présenté dans la note:

```text
lag_3  lag_2  lag_1  target
  10     12     13     14
  12     13     14     17
```

**3. Implémentation (pseudo-code simplifié)**

La note contient:

* une version minimaliste pour l’exploration,
* une version “poussée” proche d’une implémentation production.

Exemple repris de la note :

```python
def make_supervised(series, lags=12):
    data = concat([series.shift(i) for i in range(1, lags+1)])
    data["target"] = series.values
    return data.dropna()
```

La version avancée introduit:

* rollings causaux (`shift(1)`)
* features calendrier (jour/semaine/mois)
* gestion d’exogènes avec éventuel `shift_exog_by`
* interrupteurs pour activer/désactiver des blocs de features (ablations)

**4. Pièges et fuites temporelles**

Cette note insiste sur les problèmes rencontrés, notamment:

* fuite due à un mauvais ordre de transformation (`rolling` non décalé)
* exploitation involontaire d’exogènes non disponibles en production
* incohérence d’index pour certaines granularités
* profondeur excessive des lags sur séries courtes

Extrait de la note:

> Toujours appliquer `.shift(1)` sur les rollings.
> Jamais utiliser une exogène à t si elle n’est pas disponible à t en production
> (ex: météo → utiliser `shift_exog_by=1` ou tester les deux variantes).

**5. Bonnes pratiques documentées**

La note fournit des recommandations paramétriques selon le cas d’usage, par exemple:

* Journalier avec saison hebdo: `n_lags=28`, `roll_windows=(7, 30)`
* Mensuel retail: `n_lags=12`, `roll_windows=(3, 12)`
* Série très volatile sans exogènes: `use_exog=False` + rollings courtes

**6. Liens avec le pipeline du MVP**

Cette note était centrale pour:

* la conception du module `make_supervised()`
* la compréhension des erreurs avant le pivot du J13
* la mise en place d’invariants temporels dans le pipeline
* la préparation du walk-forward strict

**7. Footer**

* Titre: Fenêtrage ML — Séries temporelles supervisées
* Tags: `#serie_temporelle`, `#fenetrage`, `#features`, `#supervise`, `#workflow/prevision`
* Liens: [[Métriques — Séries temporelles]], [[Validation temporelle — Walk-forward]], [[Jour 13 — Fenêtrage ML]]

## Pilier 3 — Projet ChatGPT persistant

Pour garantir la cohérence de l’ensemble du parcours et accélérer la montée en compétence, j’ai mis en place un projet dédié ChatGPT contenant les documents structurants de l’auto-formation et du développement du MVP.
Ce projet centralisait tout le contexte nécessaire pour faciliter les échanges, et permettait à ChatGPT d’agir comme un véritable assistant technique tout au long du processus.

Le projet était constitué de six documents de référence, dont:

### ● Phase 1 - Développement MVP

Contenu:
- Architecture cible du moteur
- Conventions internes
- Description des modules (features, models, evaluation, CLI)
- Objectifs techniques (no-leakage, walk-forward, reproductibilité)
- Décisions majeures validées au fil du développement

Rôle: servir de documentation référence du pipeline.

### ● Service IA – Étude de projet

Contenu:
- Besoins identifiés pour les PME
- Cas d’usage prioritaires (ventes, stocks, énergie)
- Contraintes opérationnelles
- Vision produit Phase 1 → Phase 2 → Phase 3

Rôle: maintenir l’alignement entre les choix techniques et la future solution IA

### ● Programme Auto-formation IA prédictive

Contenu:
- Structure du programme 6 semaines
- Notions clés de chaque étape
- Objectifs journaliers
- Socle de compétences à acquérir

Rôle: garder le cap pédagogique, l'alignement de chaque conversation avec le programme et mesurer l’avancement réel

### ● Guide de docstrings & commentaires

Contenu:
- Standards pour les docstrings (NumPy style)
- Conventions de commentaires (#why, #invariant, #assumption, #io)
- Règles de lisibilité et de structuration du code
- Exemples de bonnes pratiques

Rôle: mise en place d'un système harmonisé et reproductible, garantir la qualité du code du MVP et faciliter son industrialisation

### ● Notes d’alignement et décisions techniques

Contenu:
- Pivots importants (notamment à partir du Jour 13)
- Choix architecturaux discutés et justifiés
- Invariants du projet
- Contraintes temporelles et règles d’évaluation

Rôle: servir de journal de bord technique et assurer la cohérence des itérations.

### ● Fonctionnement en pratique

Le projet ChatGPT persistant permettait:
- D’éviter de répéter le contexte à chaque conversation
- De maintenir automatiquement l’alignement avec les décisions passées
- D’obtenir des recommandations cohérentes avec l’architecture du MVP
- D’itérer plus rapidement sur les choix techniques
- D'orchestrer le projet en utilisant ChatGPT comme copilote technique
<br></br>
---

# 4. Limites, précautions et bonnes pratiques dans l’utilisation de ChatGPT

L’usage de ChatGPT dans ce projet, bien que très efficace, a nécessité une vigilance constante.  Comme tout modèle génératif, ChatGPT présente des limites structurelles qui imposent un cadre d’utilisation rigoureux pour éviter les erreurs ou les dérives dans la construction de projets complexes. 

## Latence et perte progressive de contexte

Un aspect critique dans un tel projet est de ne pas perdre le fil d'une discussion, surtout lorsque l'on aborde des questions complexes. Une telle discussion peut très rapidement devenir très longue et, en fonction de l'IA générative utilisée, cela peut fortement impacter les réponses de l'IA qui peut:
- Montrer des signes de “latence cognitive” (ralentissement, réponses moins ciblées)
- Perdre certains éléments de contexte lointain
- Reformuler des points déjà validés ou revenir sur des décisions passées
- Perdre en qualité dans ses réponses
    
Pour pallier cela, j’ai:

- Régulièrement réintroduit explicitement les invariants clés du projet,
- Maintenu des documents persistant dans le projet ChatGPT (notes d’alignement, règles techniques),
- Systématiquement réorienté la discussion lorsque le modèle dérivait ou généralisait.
- Généré des discussions périphériques afin d'y aborder des questions secondaires, me permettant ainsi de maintenir la conversation principale sur les éléments essentiels
    
Cette gestion active a maintenu la cohérence des échanges sur 6 semaines.


## Risque d’erreurs dans le raisonnement ou l’implémentation

L'IA peut produire:
- Du code incorrect
- Des implémentations incomplètes
- Des approximations qui semblent crédibles mais sont fausses
- Des oublis d’invariants (causalité, no-leakage, cohérence temporelle)
    
Cela nécessite donc non seulement une compréhension totale de tout l'écosystème du projet (architecture, code, etc) mais également une relecture et un contrôle actifs systématiques des propositions que peut faire l'IA. 

Il est absolument essentiel de partir du principe que toute proposition de l'IA doit être remise en question avant d'être validée, que cela se fasse par: 
- Analyse manuelle
- Tests
- Vérification de la cohérence avec les décisions précédentes
- Cohérence avec la logique métier et statistique
- Intégration progressive dans `src/` uniquement lorsque validée
    
Cela permet de maintenir l'IA comme un outil d’accélération, où la décision finale, le design, le code et la vision du pipeline doivent rester entièrement sous contrôle humain.


## Nécessité d’un cadre documentaire stable

Pour les projets complexes, et afin de pallier à la volatilité inhérente aux modèles de langage, il est absolument essentiel de construire à la racine un cadre dédié structuré sur une base documentaire et un set d'instructions les plus détaillées et claires possibles.

C'est ce travail en amont qui permet de donner à l'IA un cadre structurant et sinon de garantir, de réduire le risque d'incohérences ou de dérives tout en assurant l'alignement et la continuité des échanges. 
<br></br>

---

# 5. Livrables finaux

En fin de Phase 1:
- 112 notes Obsidian
- 42 notebooks
- Pipeline complet (src/)
- Artefacts standardisés (CSV, JSON, PNG)
- Interface Streamlit fonctionnelle
- CLI Typer
- Tests + CI
- Documentation complète
- Release v0.1.0
<br></br>

---

# 6. Compétences acquises

Cette auto-formation m’a permis d’acquérir un socle solide en data science appliquée, en architecture logicielle et en industrialisation d’un pipeline de prévision.  
Les compétences ci-dessous reflètent ce que je suis désormais capable de comprendre, d’expliquer et de reproduire en m'appuyant sur une méthode structurée (documentation, notes techniques et IA copilote).

## Compétences data science

**Statistiques et manipulation de données**
- Analyse descriptive (distributions, tendance, variance, corrélations)
- Nettoyage: valeurs manquantes, outliers, cohérence temporelle
- Visualisations orientées diagnostic
- Construction de datasets supervisés pour séries temporelles

**Machine learning supervisé**
- Régressions linéaires et régularisées (Ridge, Lasso, ElasticNet)
- Modèles ensemblistes (RandomForest)
- Compréhension des hyperparamètres et tuning de base
- Évaluation rigoureuse par splits chronologiques

**Séries temporelles (ML supervisé)**
- Fenêtrage supervisé: lags, rollings causales
- Baselines structurantes (naïve, saisonnière)
- Analyse de stabilité temporelle par split
- Prévention des fuites temporelles (gap, train_min, contraintes causales)
- Gestion des cas limites (séries courtes, ruptures, exogènes incomplètes)

## Compétences en architecture et développement Python

**Conception d’un pipeline modulaire**
- Séparation claire des modules: features, modèles, evaluation, artefacts
- Implémentation du walk-forward strict
- Mise en place d’un AutoML-lite (sélection modèle, scoring, tie-breaker stabilité)
- Distinction exploration / production
- Pipeline reproductible de bout en bout

**Qualité de code et normes**
- Packaging Python (`pyproject.toml`, structure `src/`)
- Docstrings structurées (NumPy style)
- Conventions internes explicites (`#why`, `#invariant`, `#assumption`)
- Logging structuré et centralisé
- Validation de schémas (Pydantic, Pandera)

**Tests et intégration continue**
- Tests unitaires et d’intégration (pytest)
- Pipeline CI opérationnel (GitHub Actions)
- Tests de la CLI (sélection, évaluation, prédiction)
- Gestion explicite des edge cases

## Compétences outils et industrialisation

**CLI et automatisation**
- Développement d’une CLI Typer complète: `select`, `eval`, `train-export`, `predict`
- Validation des entrées
- Messages utilisateur clairs et cohérents

**Artefacts et reproductibilité**
- Export standardisé: `summary.csv`, `details.csv`, `predictions.csv`
- Model card complète: hyperparamètres, features, métriques, métadonnées
- Run info: hash dataset, versions libs, durée, configuration
- Reproduction d’un run à partir des artefacts exportés

**Interface utilisateur**
- Développement d’une interface Streamlit
- Visualisations: erreurs par split, comparaison baselines/modèles, prévisions
- UX simplifiée et adaptée à un public PME
- Prédiction via artefact exporté (`best_model.joblib + model_card.json`)

## Compétences transversales

**Documentation (Obsidian)**
- Système de connaissances structuré (112 notes)
- Notes thématiques, guides pivot, synthèses transversales
- Système de tags organisé
- Index dynamique pour navigation rapide
- Documentation vivante accompagnant le développement du pipeline

**Organisation et méthodologie**
- Cycle d’apprentissage structuré: concept → expérimentation → documentation → code → tests
- Décisions d’architecture explicitées et historisées
- Conception itérative orientée robustesse et reproductibilité

**Collaboration IA (copilote technique)**
- Projet ChatGPT persistant structuré (instructions + 6 documents de référence)
- Utilisation de l’IA comme assistant d’ingénierie et support technique
- Validation critique systématique (tests, relecture, cadrage humain)
- Maîtrise des choix d’architecture et des décisions finales






