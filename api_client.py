# api_client.py

import requests

BASE_URL_DATASET_SERVICE = "http://127.0.0.1/dataset"  # Replace with your actual URL
BASE_URL_METRICS_SERVICE = "http://127.0.0.1/metrics"  # Replace with your actual URL


def upload_dataset(file, dataset_name=None):
    url = f"{BASE_URL_DATASET_SERVICE}/upload-dataset"
    files = {"file": file}
    data = {"dataset_name": dataset_name}
    response = requests.post(url, files=files, data=data)
    return response.json()


def list_datasets():
    # url = "http://127.0.0.1:8000/datasets/datasets"
    url = f"{BASE_URL_DATASET_SERVICE}/datasets/datasets"
    response = requests.get(url)
    print(response)
    return response.json()


def preprocess_dataset(dataset_id, preprocessing_options):
    url = f"{BASE_URL_DATASET_SERVICE}/datasets/preprocess-dataset"
    data = {"dataset_id": dataset_id, **preprocessing_options}
    response = requests.post(url, data=data)
    return response.json()


def download_dataset(dataset_id):
    url = f"{BASE_URL_DATASET_SERVICE}/datasets/{dataset_id}/download"
    response = requests.get(url)
    return response.json()


def evaluate_metrics(dataset_id, model_type):
    url = f"{BASE_URL_METRICS_SERVICE}/metric-services"
    params = {"dataset_id": dataset_id, "model_type": model_type}
    response = requests.get(url, params=params)
    return response.json()


def get_previous_results():
    # Implement this function based on how you store previous results
    pass


def get_saved_metrics():
    url = f"{BASE_URL_METRICS_SERVICE}/metrics/metrics"
    response = requests.get(url)
    return response.json()


def save_metrics(metrics_data):
    url = f"{BASE_URL_METRICS_SERVICE}/metrics"
    response = requests.post(url, json=metrics_data)
    response.raise_for_status()
    return response.json()
