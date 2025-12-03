# FAQ Technique — Moteur Prédictif PME

Cette FAQ répond aux questions techniques les plus fréquentes concernant la méthodologie utilisée dans ce démonstrateur.
Elle ne dévoile aucune logique interne du moteur.

## Pourquoi utiliser la validation walk-forward ?

Parce que les données PME sont temporelles: on ne peut pas mélanger passé et futur.

Le walk-forward permet:

* D’évaluer la stabilité du modèle dans le temps
* De mesurer l’impact des ruptures (saisonnalité, promotions, anomalies)
* D’éviter toute fuite temporelle (lags, exogènes, alignement)

C’est la méthode la plus fiable pour simuler un usage réel.



## Pourquoi un AutoML-lite plutôt qu’un AutoML complet ?

Parce que le contexte PME impose:

* Transparence
* Reproductibilité
* Coût calculatoire faible
* Auditabilité

L’AutoML-lite retenu:

* Teste plusieurs candidats simples
* Utilise MASE comme scoring principal (référence baseline)
* Applique des tie-breakers (MAE, RMSE, stabilité)
* Sélectionne automatiquement le modèle le plus fiable

Un AutoML complet (AutoSklearn, Optuna) serait disproportionné en Phase 1.



## Pourquoi des modèles simples (Ridge, Naïve, baselines) ?

Pour trois raisons clés:

* Données limitées dans les PME (peu d’historique)
* Stabilité temporelle supérieure aux modèles complexes
* Interprétabilité immédiate pour un utilisateur métier

Des modèles plus sophistiqués (XGBoost, LGBM) pourront être intégrés en Phase 2.



## Quelle différence entre baseline et modèle gagnant ?

* Baseline = seuil minimal: naïve lag-1, saisonnière
* Modèle gagnant = modèle choisi par l’AutoML-lite (MASE + stabilité)

Comparer les deux permet de vérifier que le moteur apporte une amélioration réelle.



## Que contient une “model card” ?

Une *model card* est un document standardisé décrivant:

* Type de modèle
* Hyperparamètres
* Période et fréquence du dataset
* Features utilisées (lags, exogènes)
* Métriques globales
* Versions logicielles
* Hash dataset et configuration

Elle permet d’auditer un modèle en production.



## Pourquoi exporter des artefacts plutôt qu’un simple fichier de prédictions ?

Parce qu’une PME (ou un auditeur) doit pouvoir:

* Comprendre d’où viennent les résultats
* Relire la configuration du run
* Analyser la stabilité temporelle
* Vérifier la reproductibilité

Les artefacts standardisés garantissent un niveau professionnel de traçabilité.



## Quel lien avec une API future ?

Le démonstrateur produit déjà:

* Un modèle sérialisé
* Une signature de features
* Des artefacts normalisés
* Un workflow reproductible

Ces fondations permettent ensuite:

* Un endpoint `/predict`
* L'intégration ERP
* Un monitoring de dérive
* Un batch planifié

C’est l’objectif de la Phase 2.



## Quel rôle joue l’interface Streamlit ?

Elle sert de traduction métier du moteur:

* Charge un CSV
* Lance une évaluation walk-forward
* Compare modèles vs baselines
* Génère prédictions, métriques, visualisations
* Permet de télécharger les résultats
* Lit automatiquement les artefacts exportés

L’interface n’intègre aucune logique métier: elle expose uniquement les résultats du moteur.



## Comment la reproductibilité est-elle assurée ?

À deux niveaux:

### Reproductibilité procédurale

* Summary.csv
* Details.csv
* Model_card.json
* Run_info.json
* Logs et visualisations

### Reproductibilité structurelle

* Architecture modulaire (features → model → evaluation → artefacts)
* Fonctions pures
* Moteur découplé de la CLI et de l’interface
* Signatures de features contrôlées

Cela permet de rejouer un run à l’identique, même longtemps après.

