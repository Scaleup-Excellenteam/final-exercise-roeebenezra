import requests
from datetime import datetime


class Status:
    def __init__(self, status, filename, timestamp, explanation):
        self.status = status
        self.filename = filename
        self.timestamp = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
        self.explanation = explanation

    def is_done(self):
        return self.status == "done"


class ExplainerClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def upload(self, file_path):
        url = f"{self.base_url}/upload"
        with open(file_path, "rb") as file:
            response = requests.post(url, files={"file": file})
        if response.status_code == 200:
            json_data = response.json()
            return json_data["uid"]
        else:
            raise Exception(f"Upload failed with error code {response.status_code}")

    def status(self, uid):
        url = f"{self.base_url}/status"
        params = {"uid": uid}
        response = requests.get(url, params=params)
        if response.status_code == 200:
            json_data = response.json()
            return Status(
                status=json_data["status"],
                filename=json_data["filename"],
                timestamp=json_data["timestamp"],
                explanation=json_data["explanation"]
            )
        else:
            raise Exception(f"Status request failed with error code {response.status_code}")
