# PowerPoint Analyzer

PowerPoint Analyzer is a Python project that processes PowerPoint presentations and generates explanations using the OpenAI API. It helps you summarize the content of each slide and provide additional information.

## Features

- Extract text content from PowerPoint slides.
- Utilize the OpenAI API to generate explanations for each slide.
- Save the generated explanations to a JSON file.

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/your-username/powerpoint-analyzer.git
   ```

2. Navigate to the project directory:

   ```shell
   cd powerpoint-analyzer
   ```

3. Create a virtual environment (optional but recommended):

   ```shell
   python3 -m venv venv
   source venv/bin/activate
   ```

4. Install the required dependencies:

   ```shell
   pip install -r requirements.txt
   ```

## Usage

1. Set up your OpenAI API key:
   - Sign up for an OpenAI account and obtain an API key.
   - Export the API key as an environment variable:
     ```shell
     export OPENAI_API_KEY=your-api-key
     ```
   
2. Run the script:
   ```shell
   python main.py <presentation_path>
   ```
   Replace `<presentation_path>` with the path to your PowerPoint presentation file.

3. The script will process the presentation, generate explanations for each slide, and save the explanations to a JSON file.

## Example

```shell
python main.py path/to/presentation.pptx
```

## Requirements

- Python 3.6+
- `openai` library (install via `pip install openai`)
- `pptx` library (install via `pip install python-pptx`)

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
```

Feel free to customize the content and sections according to your project's specific details and requirements.