import requests
import json
import logging

class APIConnector:
    def __init__(self, base_url=None, headers=None, timeout=10):
        self.base_url = base_url or ""
        self.headers = headers or {"Content-Type": "application/json"}
        self.timeout = timeout
        logging.basicConfig(level=logging.INFO)

    def set_base_url(self, url):
        self.base_url = url

    def get(self, endpoint, params=None):
        try:
            response = requests.get(f"{self.base_url}{endpoint}", headers=self.headers, params=params, timeout=self.timeout)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logging.error(f"GET request failed: {e}")
            return None

    def post(self, endpoint, data=None):
        try:
            response = requests.post(f"{self.base_url}{endpoint}", headers=self.headers, data=json.dumps(data), timeout=self.timeout)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logging.error(f"POST request failed: {e}")
            return None

    def put(self, endpoint, data=None):
        try:
            response = requests.put(f"{self.base_url}{endpoint}", headers=self.headers, data=json.dumps(data), timeout=self.timeout)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logging.error(f"PUT request failed: {e}")
            return None

    def delete(self, endpoint):
        try:
            response = requests.delete(f"{self.base_url}{endpoint}", headers=self.headers, timeout=self.timeout)
            response.raise_for_status()
            return response.status_code == 204
        except requests.RequestException as e:
            logging.error(f"DELETE request failed: {e}")
            return False
