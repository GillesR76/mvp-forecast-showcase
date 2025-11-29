

# FAQ Technique — Moteur Prédictif PME

Cette FAQ répond aux questions techniques les plus fréquentes concernant la méthodologie utilisée dans le démonstrateur.

## Pourquoi utiliser la validation walk-forward ?

Parce que les données PME sont temporelles : on ne peut pas mélanger passé et futur dans les splits.  
Le walk-forward permet :
- d’évaluer la stabilité d’un modèle dans le temps,
- de mesurer l’impact des ruptures (saisonnalité, promotions, anomalies),
- d’éviter tout leakage (information du futur utilisée par erreur).

## Pourquoi un AutoML-lite plutôt qu’un AutoML complet ?

Parce que l’objectif du MVP est :
- la reproductibilité,
- la transparence,
- le contrôle,
- et un coût de calcul faible.

Un AutoML complet (Optuna, AutoSklearn…) serait excessif pour une PME.  Un AutoML-lite donne le meilleur rapport simplicité/robustesse

## Pourquoi des modèles simples (Ridge, Naïve, baselines) ?

Pour trois raisons :

1. **Les données PME sont souvent limitées** (peu d’historique)
2. **Les modèles simples sont plus stables temporellement**
3. **Ils sont interprétables** par un utilisateur métier

Une extension Phase 2 pourra intégrer des modèles non linéaires supplémentaires.

## Quelle différence entre baseline et modèle gagnant ?

- La **baseline** mesure le niveau minimal à dépasser (naïve lag-1, saisonnière).
- Le **modèle gagnant** est celui sélectionné par la procédure AutoML-lite.

Comparer les deux permet d’assurer que le moteur **apporte une vraie valeur**.

## Que contient une “model card” ?

Une *model card* est un document normalisé incluant :

- type de modèle,
- jeux de données utilisés,
- périodes / fréquences,
- variables utilisées (lags / exogènes),
- hashes, versions logicielles,
- métriques globales.

C’est une façon professionnelle de documenter un modèle en production.

## Pourquoi exporter des artefacts plutôt qu’un simple fichier de prédictions ?

Parce qu’une PME (ou un auditeur externe) doit pouvoir :

- comprendre d’où viennent les résultats,
- vérifier la stabilité,
- relire la configuration du run,
- s’assurer de la reproductibilité.

Les artefacts standardisés permettent cela.

## Quel lien avec une API future ?

Le démonstrateur produit déjà :

- un modèle sérialisé,
- une signature d’entrée,
- des artefacts normalisés,
- un workflow reproductible.

Ces fondations permettent ensuite :

- un endpoint `/predict`,
- une intégration ERP,
- un monitoring de dérive,
- un batch automatique planifié.

