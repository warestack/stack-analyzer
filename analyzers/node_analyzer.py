from utils import fetch_file_from_github, check_file_existence_in_repo
import json

def analyze_node(repo_url):
    """
    Analyze a Node.js project by fetching and analyzing its package.json and checking for other files.

    :param repo_url: URL of the GitHub repository to analyze
    """
    
    analysis_result = {
        "languages": ["JavaScript"],  # default assumption
        "frameworks": [],
        "build_tools": [],
        "dockerised": False,
        "dependency_manager": "npm",  # defaults to npm
    }

    # dependency manager detection
    if check_file_existence_in_repo(repo_url, 'yarn.lock'):
        analysis_result['dependency_manager'] = 'yarn'
    # npm is the default, no need to check for package-lock.json explicitly
    # @cfc add more dependency manager checks

    # fetch package.json content
    package_json_content = fetch_file_from_github(repo_url, 'package.json')
    if package_json_content:
        package_json = json.loads(package_json_content)
        dependencies = package_json.get('dependencies', {})
        devDependencies = package_json.get('devDependencies', {})

        # framework Detection
        if 'express' in dependencies:
            analysis_result['frameworks'].append('Express.js')
        if 'nestjs/core' in dependencies or 'nestjs/common' in dependencies:
            analysis_result['frameworks'].append('NestJS')
        if '@angular/core' in dependencies or '@angular/cli' in devDependencies:
            analysis_result['frameworks'].append('Angular')
        if 'next' in dependencies:
            analysis_result['frameworks'].append('NextJS')    
        if 'react' in dependencies:
            analysis_result['frameworks'].append('React')
        if 'koa' in dependencies:
            analysis_result['frameworks'].append('Koa')
        if 'vue' in dependencies or 'vue' in devDependencies:
            analysis_result['frameworks'].append('Vue.js')
        if 'svelte' in dependencies or 'svelte' in devDependencies:
            analysis_result['frameworks'].append('Svelte')
        if '@ionic/react' in dependencies or '@ionic/angular' in dependencies:
            analysis_result['frameworks'].append('Ionic')
        # @cfc add more framework checks

        # build tool detection
        if 'webpack' in devDependencies:
            analysis_result['build_tools'].append('Webpack')
        if 'gulp' in devDependencies:
            analysis_result['build_tools'].append('Gulp')
        if 'grunt' in devDependencies:
            analysis_result['build_tools'].append('Grunt')
        if 'vite' in devDependencies:
            analysis_result['build_tools'].append('Vite')
        # @cfc add more build tool checks

        # typescript detection
        if 'typescript' in devDependencies:
            analysis_result['languages'].append('TypeScript')

    # docker detection
    if check_file_existence_in_repo(repo_url, 'Dockerfile') or check_file_existence_in_repo(repo_url, 'docker-compose.yml'):
        analysis_result['dockerised'] = True

    return analysis_result