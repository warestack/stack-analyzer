# Warestack Stack Analyzer

## Purpose

This project is a library designed to analyze the technology stack of software projects hosted in repositories. By examining base files it determines the project's main programming languages, frameworks, runtime environments, and whether the project is Dockerized.

#### Expected Output

The analyzer should return an object detailing the analyzed tech stack of the provided repository. For example:

```json
{
  "build_tools": ["Webpack"],
  "dependency_manager": "npm",
  "languages": ["JavaScript"],
  "framework": "Express",
  "dockerised": true
}
```

### Importing the library

In case you want to use the analyzer in your python project you could install it via pip.

```bash
pip install stack-analyzer
```

### Setting up your PAT token

The Stack Analyzer utilises the github API to analyze a repository's structure, so you it would require from you to generate a GitHub PAT token and then you would need to create a `.env` file on your project's root directory with the following content:

```bash
GITHUB_PAT=your_pat_token
```

### Using the analyze_repository method

Then you could import the analyzer method in your python files as such:

```python
from stack_analyzer.analyzer import analyze_repository

result = analyze_repository("https://github.com/example/repo")
print(result)

```

## Contributing

If you consider contributing to the Stack Analyzer, make sure to check out our [Contribution Guide](CONTRIBUTING.md) and our [Development Guide](DEVELOPMENT.md), for more information on how to run and test the project locally.

You are welcome to create your own analyzer, add a new feature, or look for our "Call For Contribution" `@cfc` comments in the codebase to contribute in extending existing analyzers.
