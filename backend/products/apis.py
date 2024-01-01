import requests

def fetch_makeup_data():
    api_endpoint = "http://127.0.0.1:8000/products/?search=makeup"
    return requests.get(api_endpoint).json()

def fetch_foundation_data():
    api_endpoint = "http://127.0.0.1:8000/products/?search=foundation"
    return requests.get(api_endpoint).json()

def fetch_bb_cc_cream_data():
    api_endpoint = "http://127.0.0.1:8000/products/?search=BB & CC cream"
    return requests.get(api_endpoint).json()

def fetch_concealer_data():
    api_endpoint = "http://127.0.0.1:8000/products/?search=concealer"
    return requests.get(api_endpoint).json()