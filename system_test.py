import subprocess
import time
from explainer_client import ExplainerClient

def run_system_test():
    # Start the Web API
    web_api_process = subprocess.Popen(["python", "web_api.py"])  # Replace with the command to start your web API
    time.sleep(1)  # Allow some time for the web API to start

    # Start the Explainer
    explainer_process = subprocess.Popen(["python", "explainer.py"])  # Replace with the command to start your explainer
    time.sleep(1)  # Allow some time for the explainer to start

    # Create an instance of the ExplainerClient
    client = ExplainerClient("http://localhost:5000")  # Replace with the base URL of your web app

    # Upload a sample presentation
    file_path = "path/to/test.pptx"  # Replace with the path to your sample presentation
    uid = client.upload(file_path)
    print(f"Uploaded file with UID: {uid}")

    # Check the status of the presentation
    status = client.status(uid)
    print(f"Status: {status.status}")
    print(f"Filename: {status.filename}")
    print(f"Timestamp: {status.timestamp}")
    print(f"Explanation: {status.explanation}")

    # Stop the processes
    web_api_process.terminate()
    explainer_process.terminate()


if __name__ == "__main__":
    run_system_test()
