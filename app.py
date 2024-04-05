from flask import Flask, request, jsonify
import os
from utils import check_file_existence_in_repo

# import analyzers
from analyzers.node_analyzer import analyze_node
from analyzers.php_analyzer import analyze_php
# @cfc implement more analyzers

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze_repo():
    data = request.json
    repo_url = data.get('repo_url')

    # determine if the repository is a Node.js or PHP project
    is_php_project = check_file_existence_in_repo(repo_url, 'composer.json')
    is_node_project = check_file_existence_in_repo(repo_url, 'package.json')
    # @cfc detect more kinds of repositories

    # forward the repo to the analyzers
    # IMPORTANT: node analyzer should remain at last place since fullstack projects
    # e.g. PHP ones may also contain a package.json
    if is_php_project:
        analysis_result = analyze_php(repo_url)
    # @cfc add more checks
    elif is_node_project:
        analysis_result = analyze_node(repo_url)
    else:
        analysis_result = {"error": "Project type could not be determined or is unsupported."}

    return jsonify(analysis_result)

if __name__ == '__main__':
    app.run(debug=True)