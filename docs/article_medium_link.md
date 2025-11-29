artifacts/
└── <run_id>/                          # un dossier par exécution du pipeline
    ├── summary.csv                    # métriques globales (agrégées)
    ├── details.csv                    # métriques par split / horizon
    ├── predictions.csv                # prédictions alignées sur la série
    ├── model_card.json                # description structurée du modèle
    ├── run_info.json                  # métadonnées du run (config, durée...)
    └── figures/                       # visuels de restitution
        ├── forecast_last_split.png
        ├── errors_by_split.png
        └── comparaison_baseline.png

Remarques :
- <run_id> peut être un timestamp ou un identifiant lisible (ex: "2025-01-15_1030").
- La structure met l'accent sur la traçabilité et la reproductibilité.
- Le contenu exact reste propre au moteur sous-jacent (non exposé ici).

# Article Medium — Démonstrateur IA Prédictive pour PME

Cet article décrit en détail la démarche ayant conduit à la construction d’un moteur de prévision adapté aux contextes PME (prévision de ventes, optimisation de
stocks, consommation énergie, etc.). Il accompagne le démonstrateur présenté dans ce repo vitrine.

## Lien vers l’article Medium

*(insérer le lien ici)*

## Contenu de l’article

- Pourquoi les PME ont besoin d’outils prédictifs simples
- Les choix méthodologiques (walk-forward, AutoML-lite)
- Comment structurer un pipeline stable et reproductible
- Retour d’expérience sur le MVP développé
- Perspectives Phase 2 (API, multi-horizon, monitoring)

## Objectif de l’article

Présenter :
- la démarche raisonnée
- la rigueur du travail
- les fondations techniques sans exposer le code
- la vision produit permettant d’aller vers un outil commercialisable



