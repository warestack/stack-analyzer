# Running the Stack Analyzer locally

## Setting Up the Project locally

### Prerequisites

- Python 3.11 or newer
- pip and pipenv

### Installation

1. **Clone the Project**

First, clone the repository to your local machine:

```bash
git clone https://github.com/warestack/stack-analyzer.git
cd stack-analyzer
```

2. **Set up your virtual environment**

Use pipenv to create a virtual environment and install dependencies:

```bash
pipenv install
```

This command reads the Pipfile in the project root and installs all necessary packages, creating a virtual environment.

### Running the Project

1. **Activate the Virtual Environment**

Activate the pipenv-created virtual environment:

```bash
pipenv shell
```

2. **Setting up your PAT token**

The Stack Analyzer utilises the github API to analyze a repository's structure, so you'd need to create a `.env` file on the project root directory with the following content:

```bash
GITHUB_PAT=your_pat_token
```

3. **Start the Flask Application**

The repository includes a flask application for testing purposes. This means you can send curl commands to test various repositories while you develop more analyzers.

Run the Flask web service:

```bash
flask run
```

Alternatively, you can run the application on debug (and live reload) mode:

```bash
flask --app app.py --debug run
```

### Testing the Service

To test the tech stack analyzer service, you can use curl to send a POST request to the /analyze endpoint. Replace http://127.0.0.1:5000 with the appropriate URL if you've configured the service to run elsewhere.

```bash
curl -X POST http://127.0.0.1:5000/analyze -H "Content-Type: application/json" -d "{\"repo_url\":\"https://github.com/example/repo\"}"
```

This command simulates sending a repository URL to the analyzer. Given the project's current setup, it will return a JSON response based on the hardcoded analysis within the Flask application.

#### Unit tests

To run the unit tests (included within `tests`), you can use the following command while being at the project root directory:

```bash
python -m unittest discover tests
```

Or if you want to run a specific unit test you could do so as such:

```bash
python -m unittest tests/test_analyze_node.py
```
