import pandas as pd
from sklearn.linear_model import LinearRegression
import pandas as pd

class DunkPredictor:
    def __init__(self, csv_path='biscuit_data.csv'):
        self.model = LinearRegression()
        self.train(csv_path)

    def train(self, csv_path):
        df = pd.read_csv(csv_path)
        self.df = df
        features = pd.get_dummies(df[['type', 'temperature']])
        target = df['estimated_mct']
        self.model.fit(features, target)
        self.feature_names = features.columns

    def predict(self, biscuit_type, temperature):
        input_data = pd.DataFrame([[biscuit_type, temperature]], columns=['type', 'temperature'])
        input_encoded = pd.get_dummies(input_data).reindex(columns=self.feature_names, fill_value=0)
        prediction = self.model.predict(input_encoded)[0]
        return prediction
