from utils.github_utils import fetch_file_from_github, check_file_existence_in_repo


def analyze_python(repo_url):
    """
    Analyze a Python project by fetching and analyzing its requirements.txt or Pipfile and checking for other files.

    :param repo_url: URL of the GitHub repository to analyze
    """
    analysis_result = {
        "languages": ["Python"],  # default assumption
        "frameworks": [],
        "build_tools": [],
        "dockerised": False,
        "dependency_manager": "pip",  # defaults to pip
    }

    # Dependency manager detection
    if check_file_existence_in_repo(repo_url, "Pipfile"):
        analysis_result["dependency_manager"] = "pipenv"
    if check_file_existence_in_repo(repo_url, "pyproject.toml"):
        analysis_result["dependency_manager"] = "poetry"
    # Pip is the default, no need to check for requirements.txt explicitly
    # @cfc add more dependency manager checks

    # Fetch requirements or Pipfile content
    dependency_file = (
        "requirements.txt"
        if check_file_existence_in_repo(repo_url, "requirements.txt")
        else "Pipfile"
    )
    dependencies_content = fetch_file_from_github(repo_url, dependency_file)
    if dependencies_content:
        dependencies = dependencies_content.splitlines()

        # Framework detection
        if any("django==" in dep for dep in dependencies):
            analysis_result["frameworks"].append("Django")
        if any("flask==" in dep for dep in dependencies):
            analysis_result["frameworks"].append("Flask")
        if any("fastapi" in dep for dep in dependencies):
            analysis_result["frameworks"].append("FastAPI")
        if any("pyramid==" in dep for dep in dependencies):
            analysis_result["frameworks"].append("Pyramid")
        # @cfc add more framework checks

        # Build tool detection
        if any("pytest" in dep for dep in dependencies):
            analysis_result["build_tools"].append("Pytest")
        if any("tox" in dep for dep in dependencies):
            analysis_result["build_tools"].append("Tox")
        # @cfc add more build tool checks

    # Docker detection
    if check_file_existence_in_repo(
        repo_url, "Dockerfile"
    ) or check_file_existence_in_repo(repo_url, "docker-compose.yml"):
        analysis_result["dockerised"] = True

    # Additional check for frontend files like package.json to indicate potential full stack development
    if check_file_existence_in_repo(repo_url, "package.json"):
        analysis_result["languages"].append(
            "JavaScript"
        )  # This adds a JS layer suggesting frontend involvement

    return analysis_result
