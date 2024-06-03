from prometheus_client import start_http_server, Gauge
import time
from prometheus_collector import PrometheusCollector
from model_handler import ModelHandler

# URL of the Prometheus API
IP = "http://prometheus:9090"
PROMETHEUS_URL = IP + "/api/v1/query"

QUERIES = {
    'endpoint1': "rate(flask_http_request_duration_seconds_sum{path='/api/v1/endpoint1', status='200'}[30s]) / rate(flask_http_request_duration_seconds_count{path='/api/v1/endpoint1', status='200'}[30s])",
    'endpoint2': "rate(flask_http_request_duration_seconds_sum{path='/api/v1/endpoint2', status='200'}[30s]) / rate(flask_http_request_duration_seconds_count{path='/api/v1/endpoint2', status='200'}[30s])",
    'endpoint3': "rate(flask_http_request_duration_seconds_sum{path='/api/v1/endpoint3', status='200'}[30s]) / rate(flask_http_request_duration_seconds_count{path='/api/v1/endpoint3', status='200'}[30s])"
}

def main():
    prometheus_collector = PrometheusCollector(PROMETHEUS_URL, QUERIES)
    model_handler = ModelHandler('model.pkl')
    
    # Create a Prometheus metric to store the anomaly score
    score_gauge = Gauge('anomaly_score', 'Anomaly score from the HST model, based on time responses')

    # HTTP server for Prometheuss
    start_http_server(8000)

    while True:
        metrics = prometheus_collector.fetch_data()
        if metrics:
            features = metrics
            score = model_handler.calculate_score(features)
            model_handler.learn_one(features)
            
            # Set the anomaly score in the Prometheus metric
            score_gauge.set(score)
        else:
            print("No metrics fetched. Skipping this cycle.")

        time.sleep(10)  # Adjust the sleep time as needed 

if __name__ == "__main__":
    main()
