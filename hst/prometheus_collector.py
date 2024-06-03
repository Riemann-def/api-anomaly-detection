import requests

class PrometheusCollector:
    def __init__(self, prometheus_url, queries):
        self.prometheus_url = prometheus_url
        self.queries = queries

    def fetch_data(self):
        results = {}
        try:
            for endpoint, query in self.queries.items():
                response = requests.get(self.prometheus_url, params={'query': query})
                response.raise_for_status()
                data = response.json()
                if 'data' in data and 'result' in data['data'] and data['data']['result']:
                    results[endpoint] = float(data['data']['result'][0]['value'][1])
                else:
                    print(f"No data found for query: {query}")
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
        except (KeyError, IndexError, ValueError) as e:
            print(f"Error processing data: {e}")
        return results

    def extract_values(self, metrics):
        try:
            return metrics
        except (KeyError, IndexError, ValueError) as e:
            print(f"Error extracting values: {e}")
            return None
