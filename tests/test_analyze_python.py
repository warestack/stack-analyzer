import unittest
from unittest.mock import patch

from analyzers.python_analyzer import analyze_python

class TestPythonAnalyzer(unittest.TestCase):
    @patch('analyzers.python_analyzer.fetch_file_from_github')
    @patch('analyzers.python_analyzer.check_file_existence_in_repo')
    def test_analyze_python_django_project(self, mock_check_file, mock_fetch_file):
        # Setup mocks
        repo_url = 'https://github.com/example/django_project'
        mock_check_file.side_effect = lambda url, file: file in ['requirements.txt', 'Dockerfile']
        requirements_content = """
        django==3.1.7
        gunicorn==20.0.4
        """
        mock_fetch_file.return_value = requirements_content

        # Expected result
        expected_result = {
            'languages': ['Python'],
            'frameworks': ['Django'],
            'build_tools': [],
            'dockerised': True,
            'dependency_manager': 'pip',
        }

        # Test
        result = analyze_python(repo_url)
        self.assertEqual(result, expected_result)

    # Additional tests can be added here for other frameworks or configurations

if __name__ == '__main__':
    unittest.main()