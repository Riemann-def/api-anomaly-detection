from flask import Blueprint, jsonify
import time
import random

main = Blueprint('main', __name__)

@main.route('/api/v1/endpoint1')
def endpoint1():
    time.sleep(random.uniform(0.19, 0.21))  # Simulate normal processing time
    if random.randint(1, 300) == 1:
        time.sleep(5)  # Simulate an anomaly
    return jsonify({'message': 'Response from endpoint1'})

@main.route('/api/v1/endpoint2')
def endpoint2():
    time.sleep(random.uniform(0.29, 0.31))  # Simulate normal processing time
    if random.randint(1, 300) == 1:
        time.sleep(5)  # Simulate an anomaly
    return jsonify({'message': 'Response from endpoint2'})

@main.route('/api/v1/endpoint3')
def endpoint3():
    time.sleep(random.uniform(0.39, 0.41))  # Simulate normal processing time
    if random.randint(1, 300) == 1:
        time.sleep(5)  # Simulate an anomaly
    return jsonify({'message': 'Response from endpoint3'})
