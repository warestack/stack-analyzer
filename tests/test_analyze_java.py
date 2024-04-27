import unittest
from unittest.mock import patch
from analyzers.java_analyzer import (
    analyze_java,
)  # Make sure to import your analyzer function correctly


class TestJavaAnalyzer(unittest.TestCase):
    @patch("analyzers.java_analyzer.fetch_file_from_github")
    @patch("analyzers.java_analyzer.check_file_existence_in_repo")
    def test_analyze_gradle_kotlin_project(self, mock_check_file, mock_fetch_file):
        # Setup mocks for Gradle Kotlin project
        repo_url = "https://github.com/example/gradle_kotlin_project"
        mock_check_file.side_effect = lambda url, file: file == "build.gradle"
        gradle_file_content = """
        plugins {
            id 'org.jetbrains.kotlin.jvm' version '1.4.10'
        }

        dependencies {
            implementation 'org.jetbrains.kotlin:kotlin-stdlib-jdk8'
            implementation 'org.springframework.boot:spring-boot-starter-web'
        }
        """
        mock_fetch_file.return_value = gradle_file_content

        # Expected result
        expected_result = {
            "languages": ["Java", "Kotlin"],
            "frameworks": ["Spring Boot"],
            "build_tools": ["Gradle"],
            "dockerised": False,
            "dependency_manager": "Gradle",
        }

        # Test
        result = analyze_java(repo_url)
        self.assertEqual(result, expected_result)

    @patch("analyzers.java_analyzer.fetch_file_from_github")
    @patch("analyzers.java_analyzer.check_file_existence_in_repo")
    def test_analyze_maven_project_dockerised(self, mock_check_file, mock_fetch_file):
        # Setup mocks for Maven Dockerized project
        repo_url = "https://github.com/example/maven_docker_project"
        mock_check_file.side_effect = lambda url, file: file in [
            "pom.xml",
            "Dockerfile",
        ]
        pom_file_content = """
        <project xmlns="http://maven.apache.org/POM/4.0.0"
                 xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                 xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
            <modelVersion>4.0.0</modelVersion>
            <groupId>com.example</groupId>
            <artifactId>docker-java-app</artifactId>
            <version>1.0</version>
            <dependencies>
                <dependency>
                    <groupId>org.springframework.boot</groupId>
                    <artifactId>spring-boot-starter-web</artifactId>
                </dependency>
            </dependencies>
        </project>
        """
        mock_fetch_file.return_value = pom_file_content

        # Expected result
        expected_result = {
            "languages": ["Java"],
            "frameworks": ["Spring Boot"],
            "build_tools": ["Maven"],
            "dockerised": True,
            "dependency_manager": "Maven",
        }

        # Test
        result = analyze_java(repo_url)
        self.assertEqual(result, expected_result)

    # Additional tests can be added here for other scenarios


if __name__ == "__main__":
    unittest.main()
