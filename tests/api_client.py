import requests
from tests.config import BASE_URL

class APIClient:
    @staticmethod
    def get(endpoint):
        """Send a GET request"""
        response = requests.get(BASE_URL + endpoint)
        return response

    @staticmethod
    def post(endpoint, payload):
        """Send a POST request"""
        response = requests.post(BASE_URL + endpoint, json=payload)
        return response

    @staticmethod
    def put(endpoint, payload):
        """Send a PUT request"""
        response = requests.put(BASE_URL + endpoint, json=payload)
        return response

    @staticmethod
    def delete(endpoint):
        """Send a DELETE request"""
        response = requests.delete(BASE_URL + endpoint)
        return response
