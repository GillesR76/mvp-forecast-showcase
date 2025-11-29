from sklearn.linear_model import Ridge


class RidgePredictor:
    """
    Exemple de wrapper simplifié autour de sklearn.linear_model.Ridge.
    Le projet réel utilise une version enrichie (log, validation, etc.).
    """

    def __init__(self, alpha: float = 1.0):
        self.model = Ridge(alpha=alpha)

    def fit(self, X, y):
        self.model.fit(X, y)
        return self

    def predict(self, X):
        return self.model.predict(X)
