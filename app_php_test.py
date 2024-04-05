from flask import Flask, request, jsonify
import json
# Ensure the php_analyzer is accessible here, might need to adjust the import path based on your project structure
from analyzers.php_analyzer import analyze as analyze_php

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze_php_repo():
    # Simulated repo files including composer.json, and optionally Dockerfile or docker-compose.yml
    repo_files = {
        "composer.json": json.dumps({
            "require": {
                "laravel/framework": "^8.40",
                "symfony/symfony": "^5.2"
            },
            "require-dev": {
                "laravel-mix": "^9.3",
                "phpunit/phpunit": "^9.3"
            }
        }),
        "Dockerfile": "FROM php:7.4-fpm"
    }

    # Call the php_analyzer with the simulated repo_files
    analysis_result = analyze_php(repo_files)

    return jsonify(analysis_result)

if __name__ == '__main__':
    app.run(debug=True)