@app.command("predict")
def cmd_predict(
    config: Path = typer.Option(..., "--config"),
    input_csv: Path = typer.Option(..., "--input-csv"),
    output_csv: Path = typer.Option(..., "--output-csv"),
):
    """
    Exemple ultra-simplifié de commande CLI pour lancer une prédiction.
    La version réelle du projet gère :
    - chargement de modèle exporté,
    - reconstruction des features d'inférence,
    - alignement des features avec la signature du modèle,
    - gestion des erreurs (historique insuffisant, colonnes manquantes, etc.).
    """
    # 1) Charger la config
    # 2) Charger le modèle
    # 3) Lire le CSV brut
    # 4) Construire les features pour l'inférence
    # 5) Appliquer model.predict(...)
    # 6) Sauvegarder predictions.csv
    ...
