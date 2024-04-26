from flask import Flask, request, jsonify
import os

from library.analyzer import analyze_repository

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze_repo():
    data = request.json
    repo_url = data.get('repo_url')

    # Use the unified analyzer interface
    analysis_result = analyze_repository(repo_url)

    return jsonify(analysis_result)

if __name__ == '__main__':
    app.run(debug=True)