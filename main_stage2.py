import asyncio
import time
import argparse
import json
import os
import uuid

from app import app
from explainer_client import ExplainerClient

from openAi import OpenAi
from pptxParser import PresentationParser
from explainer_system import explainer_system


def print_to_file(explanations, presentation_path, uid):
    """
    Print the explanations to a file.
    :param explanations: list of explanations from the OpenAI API responses
    :param presentation_path: path to the PowerPoint presentation
    :param uid: UID of the upload
    :return: None
    """
    presentation_name = presentation_path.split("/")[-1].split(".")[0]
    output_file = f"{presentation_name}_{uid}.json"
    output_data = {"explanations": explanations}

    with open(output_file, "w") as f:
        json.dump(output_data, f, indent=4)


def main():
    parser = argparse.ArgumentParser(description="Process PowerPoint presentation and generate explanations.")
    parser.add_argument("presentation_path", metavar="presentation_path", type=str,
                        help="path to the PowerPoint presentation")
    args = parser.parse_args()
    presentation_path = args.presentation_path

    print(f"Processing {presentation_path}")

    # Parse presentation
    presentation_parser = PresentationParser(presentation_path)
    slides = presentation_parser.process_presentation()

    # Generate explanations
    api_key = os.environ.get("OPENAI_API_KEY")
    openai_api = OpenAi(api_key=api_key)
    explanations = asyncio.run(openai_api.generate_explanations(slides))

    # Generate UID for the uploaded file
    uid = str(uuid.uuid4())

    # Save the file
    print_to_file(explanations, presentation_path, uid)

    # Run the Flask application
    app.run(debug=True)

    # Start the explainer system
    explainer_system()




if __name__ == "__main__":
    # Start timer to measure execution time
    start_time = time.time()
    main()

    client = ExplainerClient("http://localhost:5000")  # Replace with the base URL of your web app

    # Upload a file and get the UID
    file_path = "path/to/test.pptx"
    uid = client.upload(file_path)
    print(f"Uploaded file with UID: {uid}")

    # Get the status of the upload
    status = client.status(uid)
    print(f"Status: {status.status}")
    print(f"Filename: {status.filename}")
    print(f"Timestamp: {status.timestamp}")
    print(f"Explanation: {status.explanation}")

    end_time = time.time()
