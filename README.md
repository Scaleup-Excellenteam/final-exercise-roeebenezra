# Presentation Explainer

Presentation Explainer is a Python-based application that processes PowerPoint presentations and generates explanations for each slide using OpenAI's GPT model. It provides a Web API, Python client, and an Explainer system for efficient processing and retrieval of explanations.

## Features

- Process PowerPoint presentations and generate explanations for each slide.
- Web API for uploading presentations, checking status, and retrieving explanations.
- Python client for convenient interaction with the Web API.
- Explainer system that continuously processes files dropped into a directory.
- System test for end-to-end testing of the entire system.

## Prerequisites

- Python 3.x
- Dependencies listed in `requirements.txt`

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/your-username/presentation-explainer.git
   ```

2. Install the required dependencies:

   ```shell
   pip install -r requirements.txt
   ```

## Usage

### Web API

1. Start the Web API by running `web_api.py`:

   ```shell
   python web_api.py
   ```

2. The Web API will be accessible at `http://localhost:5000`. Use the following endpoints:

   - `POST /upload`: Upload a PowerPoint presentation. Returns the UID of the upload.
   - `GET /status/{uid}`: Check the status of an upload. Returns the status, filename, timestamp, and explanation.
   - `GET /explanation/{uid}`: Retrieve the explanation for an upload.

### Python Client

The Python client provides a convenient way to interact with the Web API.

1. Import the `ExplainerClient` class from `explainer_client.py`:

   ```python
   from explainer_client import ExplainerClient
   ```

2. Create an instance of the client, specifying the base URL of the Web API:

   ```python
   client = ExplainerClient("http://localhost:5000")
   ```

3. Use the client's methods to upload presentations and check status:

   ```python
   # Upload a presentation
   uid = client.upload("path/to/presentation.pptx")

   # Check the status of an upload
   status = client.status(uid)
   if status.is_done():
       print("Upload processed successfully.")
       print("Explanation:", status.explanation)
   else:
       print("Upload is still pending.")

   # Retrieve the explanation for an upload
   explanation = client.retrieve_explanation(uid)
   print("Explanation:", explanation)
   ```

### Explainer

The Explainer system continuously processes files dropped into a directory.

1. Start the Explainer by running `explainer.py`:

   ```shell
   python explainer.py
   ```

   The Explainer will scan the `uploads` folder, process any unprocessed files, and save the explanations in the `outputs` folder.

### System Test

The system test performs an end-to-end run-through of the entire system.

1. Start the Web API:

   ```shell
   python web_api.py
   ```

2. Start the Explainer:

   ```shell
   python explainer.py
   ```

3. Run the system test script:

   ```shell
   python system_test.py
   ```

   The script will upload a sample presentation, check its status, and display the results.

