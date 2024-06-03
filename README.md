# Anomaly Detection in API Performance with Flask, Docker, Prometheus, and Grafana

## Overview

This project is a comprehensive simulation of API performance using Flask, with built-in anomaly detection leveraging Half Space Trees. The application is containerized using Docker and includes Prometheus for metrics collection, Grafana for visualization, Locust for load testing, and a custom HST service for anomaly detection.

## Features

- **Multiple Endpoints:** Simulates various API endpoints with different response times.
- **Anomaly Injection:** Randomly introduces performance anomalies approximately once every 5 minutes.
- **Metrics Collection:** Exports detailed metrics to Prometheus every 15 seconds.
- **Anomaly Detection:** Uses a machine learning model (Half Space Trees) to detect performance anomalies.
- **Visualization:** Provides real-time monitoring through Grafana dashboards.
- **Load Testing:** Uses Locust to simulate user traffic and load on the API with automatic execution.

## Deployment with Docker Compose

### Prerequisites

- Docker
- Docker Compose

### Steps

1. Clone the repository:
   ```bash
   git clone git@github.com:Riemann-def/api-anomaly-detection.git
   cd anomaly-detection-api
   ```

2. Build and run the Docker containers:
    ```bash
    docker-compose up --build
    ```

3. Access the aplication: 
   * The API endpoints are available at http://localhost:5000/api/v1/endpoint1, http://localhost:5000/api/v1/endpoint2, and http://localhost:5000/api/v1/endpoint3.
   * Prometheus metrics are available at http://localhost:9090.
   * Grafana dashboard is available at http://localhost:3000 (default login is admin/admin).
   * Locust UI for load testing is available at http://localhost:8089.

# Using Locust for Load Testing

   Locust has been configured to automatically start load testing the API endpoints with a new request to one of the endpoints every second. Anomalies are introduced approximately once every 5 minutes.

# Accessing Grafana

   1. Open Grafana at http://localhost:3000.
   2. Login with username admin and password admin.
   3. Navigate to the provided dashboard to see real-time metrics and anomaly scores.

# Demonstration Video

![Demo](assets/result.gif)