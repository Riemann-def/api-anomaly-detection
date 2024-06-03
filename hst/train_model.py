import time
import random
import joblib
from river import anomaly, preprocessing, compose

def simulate_data():
    data = []
    for i in range(1000):
        endpoint1_time = random.uniform(0.17, 0.23)
        endpoint2_time = random.uniform(0.27, 0.33)
        endpoint3_time = random.uniform(0.37, 0.43)
        
        # Artificially introduce an anomaly
        if i % 200 == 0:
            endpoint1_time = random.uniform(0.5, 1.0)
            endpoint2_time = random.uniform(0.5, 1.0)
            endpoint3_time = random.uniform(0.5, 1.0)
        
        data.append({'endpoint1': round(float(endpoint1_time), 3), 'endpoint2': round(float(endpoint2_time), 3), 'endpoint3': round(float(endpoint3_time), 3)})
    return data

# Train and save the model
def train_and_save_model():
    model = compose.Pipeline(
        preprocessing.MinMaxScaler(),  # Normalize data
        anomaly.HalfSpaceTrees(
            n_trees=5,
            height=3,
            window_size=3,  
            seed=10
        )
    )

    data = simulate_data()
    for features in data:
        model.learn_one(features)

    # Save the model
    joblib.dump(model, 'model.pkl')
    print("Model trained and saved in 'model.pkl'.")

if __name__ == "__main__":
    train_and_save_model()
