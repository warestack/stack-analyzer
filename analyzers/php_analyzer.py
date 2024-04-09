from utils.github_utils import fetch_file_from_github, check_file_existence_in_repo
import json

def analyze_php(repo_url):
    """
    Analyze a PHP project by fetching its composer.json and analyzing the project structure.

    :param repo_url: URL of the GitHub repository to analyze
    """

    analysis_result = {
        "languages": ["PHP"],
        "frameworks": [],
        "build_tools": [],
        "dockerised": False,
        "dependency_manager": "Composer",
    }

    # fetch composer.json content
    composer_json_content = fetch_file_from_github(repo_url, 'composer.json')
    if composer_json_content:
        composer_json = json.loads(composer_json_content)
        require = composer_json.get('require', {})
        
        # framework Detection
        if 'laravel/framework' in require:
            analysis_result['frameworks'].append('Laravel')
        if 'symfony/symfony' in require:
            analysis_result['frameworks'].append('Symfony')
        # @cfc add more framework checks

        # Assuming front-end build tools are managed separately and might be included in the project
        if check_file_existence_in_repo(repo_url, 'package.json'):
            analysis_result['languages'].append('JavaScript')  # Indicate potential JS usage
    
    # docker detection
    if check_file_existence_in_repo(repo_url, 'Dockerfile') or check_file_existence_in_repo(repo_url, 'docker-compose.yml'):
        analysis_result['dockerised'] = True

    return analysis_result
