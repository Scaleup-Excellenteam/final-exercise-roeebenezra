import asyncio
import time
import argparse
import json
import os

from openAi import OpenAi
from pptxParser import PresentationParser


def print_to_file(explanations, presentation_path) -> None:
    """
    Print the explanations to a file.
    :param explanations: list of explanations from the OpenAI API responses
    :param presentation_path: path to the PowerPoint presentation
    :return: None
    """
    presentation_name = os.path.splitext(os.path.basename(presentation_path))[0]
    output_file = f"{presentation_name}.json"
    output_data = {"explanations": explanations}

    with open(output_file, "w") as f:
        json.dump(output_data, f, indent=4)


def main():
    parser = argparse.ArgumentParser(description="Process PowerPoint presentation and generate explanations.")
    parser.add_argument("presentation_path", metavar="presentation_path", type=str,
                        help="path to the PowerPoint presentation")
    args = parser.parse_args()
    presentation_path = args.presentation_path

    print(f"Processing the pptx: {presentation_path}")

    # Parse presentation
    presentation_parser = PresentationParser(presentation_path)
    slides = presentation_parser.process_presentation()

    # Generate explanations
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("ERROR: Please set the OPENAI_API_KEY environment variable.")
        return

    openai_api = OpenAi(api_key=api_key)
    loop = asyncio.get_event_loop()
    explanations = loop.run_until_complete(openai_api.generate_explanations(slides))

    print_to_file(explanations, presentation_path)


if __name__ == "__main__":
    # Start timer to measure execution time
    start_time = time.time()
    main()
    end_time = time.time()
