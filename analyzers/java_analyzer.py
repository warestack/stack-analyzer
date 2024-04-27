from utils.github_utils import fetch_file_from_github, check_file_existence_in_repo
import xml.etree.ElementTree as ET

def analyze_java(repo_url):
    """
    Analyze a Java project by fetching its pom.xml or build.gradle and analyzing the project structure,
    including detection of Kotlin usage.

    :param repo_url: URL of the GitHub repository to analyze
    """
    
    analysis_result = {
        "languages": ["Java"],  # Java is assumed; Kotlin check will be added
        "frameworks": [],
        "build_tools": [],
        "dockerised": False,
        "dependency_manager": None,  # Will be determined based on build file
    }

    # Check for Maven or Gradle build files
    if check_file_existence_in_repo(repo_url, 'pom.xml'):
        analysis_result['dependency_manager'] = 'Maven'
        build_file_content = fetch_file_from_github(repo_url, 'pom.xml')
        if build_file_content:
            analysis_result['build_tools'].append('Maven')
            root = ET.fromstring(build_file_content)
            # Parsing dependencies and plugins for Maven
            dependencies = root.findall('.//{http://maven.apache.org/POM/4.0.0}dependency')
            for dependency in dependencies:
                group_id = dependency.find('{http://maven.apache.org/POM/4.0.0}groupId').text if dependency.find('{http://maven.apache.org/POM/4.0.0}groupId') is not None else ""
                artifact_id = dependency.find('{http://maven.apache.org/POM/4.0.0}artifactId').text if dependency.find('{http://maven.apache.org/POM/4.0.0}artifactId') is not None else ""
                if 'org.jetbrains.kotlin' in group_id:
                    analysis_result['languages'].append('Kotlin')
                if 'spring-boot-starter' in artifact_id:
                    analysis_result['frameworks'].append('Spring Boot')

    elif check_file_existence_in_repo(repo_url, 'build.gradle'):
        analysis_result['dependency_manager'] = 'Gradle'
        build_file_content = fetch_file_from_github(repo_url, 'build.gradle')
        if build_file_content:
            analysis_result['build_tools'].append('Gradle')
            # Checks for Gradle-based Kotlin projects
            if 'org.jetbrains.kotlin' in build_file_content or 'kotlin("jvm")' in build_file_content:
                analysis_result['languages'].append('Kotlin')
            if 'org.springframework.boot' in build_file_content:
                analysis_result['frameworks'].append('Spring Boot')
            if 'com.vaadin' in build_file_content:
                analysis_result['frameworks'].append('Vaadin')

    # Docker detection
    if check_file_existence_in_repo(repo_url, 'Dockerfile') or check_file_existence_in_repo(repo_url, 'docker-compose.yml'):
        analysis_result['dockerised'] = True

    if not analysis_result['dependency_manager']:
        return {"error": "Project build system could not be determined or is unsupported."}

    return analysis_result