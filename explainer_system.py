import asyncio
import json
import time
import os

from openAi import OpenAi
from pptxParser import PresentationParser


def process_file(file_path):
    # Parse presentation
    presentation_parser = PresentationParser(file_path)
    slides = presentation_parser.process_presentation()

    # Generate explanations
    api_key = os.environ.get("OPENAI_API_KEY")
    openai_api = OpenAi(api_key=api_key)
    explanations = asyncio.run(openai_api.generate_explanations(slides))

    # Save the explanation JSON in the outputs folder
    filename = os.path.basename(file_path)
    output_file = f"outputs/{filename}.json"
    with open(output_file, "w") as f:
        json.dump({"explanations": explanations}, f, indent=4)


def explainer_system():
    while True:
        # Scan the uploads folder for new files
        uploads_folder = "uploads/"
        files = os.listdir(uploads_folder)
        for file in files:
            file_path = os.path.join(uploads_folder, file)
            if os.path.isfile(file_path):
                # Make a debugging print
                print(f"Processing file: {file}")

                # Process the file
                process_file(file_path)

                # Make another debugging print
                print(f"File processed: {file}")

        # Sleep for a few seconds between iterations
        time.sleep(10)
