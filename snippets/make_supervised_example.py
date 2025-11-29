def make_supervised_example(df, target_col: str, n_lags: int = 3):
    """
    Exemple simplifié : construction de quelques lags pour illustrer le principe.
    Cette fonction est une version *démonstrative* utilisée dans le repo vitrine.
    """
    out = pd.DataFrame(index=df.index)

    y = df[target_col].astype(float)

    # Lags simples de la cible (principe)
    for i in range(1, n_lags + 1):
        out[f"lag_{i}"] = y.shift(i)

    # On garde aussi la cible pour entraînement
    out["target"] = y

    return out.dropna()
