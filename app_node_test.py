from flask import Flask, request, jsonify
import json

# Ensure node_analyzer is accessible here, might need to adjust import path based on your project structure
from analyzers.node_analyzer import analyze as analyze_node

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze_repo():
    # Simulated repo files including package.json, Dockerfile, and tsconfig.json
    repo_files = {
        "package.json": json.dumps({
            "dependencies": {
                "react": "^17.0.2",
                "nestjs/core": "^7.6.15",
                "express": "^4.17.1"  # Including Express to demonstrate multi-framework detection
            },
            "devDependencies": {
                "typescript": "^4.1.3",
                "webpack": '1.0.0'
            }
        }),
        "yarn.lock": "test",
        "Dockerfile": "FROM node:14",
        "tsconfig.json": "{}"
    }

    # Call the node_analyzer with the simulated repo_files
    analysis_result = analyze_node(repo_files)

    return jsonify(analysis_result)

if __name__ == '__main__':
    app.run(debug=True)