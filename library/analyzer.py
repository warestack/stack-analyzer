# analyzer.py
from analyzers.node_analyzer import analyze_node
from analyzers.php_analyzer import analyze_php
from analyzers.python_analyzer import analyze_python
from utils.github_utils import check_file_existence_in_repo

def analyze_repository(repo_url):
    """
    Determine the project type and forward it to the appropriate analyzer.

    :param repo_url: URL of the GitHub repository to analyze
    :return: Analysis results as a dictionary
    """
    # this structure makes it easier to add more analyzers in the future
    analyzers = {
        # PHP analyzer
        'composer.json': analyze_php,
        # PYTHON analyzer 
        'requirements.txt': analyze_python,  
        'Pipfile': analyze_python, 
        'pyproject.toml': analyze_python, 
        # NODE analyzer
        'package.json': analyze_node, 
    }
    # @cfc detect more kinds of repositories
    
    for config_file, analyzer_func in analyzers.items():
        if check_file_existence_in_repo(repo_url, config_file):
            return analyzer_func(repo_url)
    
    return {"error": "Project type could not be determined or is unsupported."}
