from river import anomaly, preprocessing, compose
import joblib

class ModelHandler:
    def __init__(self, path):
        self.model = joblib.load(path)

    def calculate_score(self, features):
        return self.model.score_one(features)

    def learn_one(self, features):
        self.model.learn_one(features)
