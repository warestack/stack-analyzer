import unittest
from unittest.mock import patch, MagicMock
import json

from analyzers.php_analyzer import analyze_php

class TestAnalyzePHP(unittest.TestCase):
    
    @patch('analyzers.php_analyzer.fetch_file_from_github')
    @patch('analyzers.php_analyzer.check_file_existence_in_repo')
    def test_php_framework_and_docker_detection(self, mock_check_file_existence, mock_fetch_file_from_github):
        # mocking fetch_file_from_github to simulate composer.json with Laravel framework
        composer_json_content = json.dumps({
            "require": {
                "laravel/framework": "^8.0"
            }
        })
        mock_fetch_file_from_github.return_value = composer_json_content
        
        def side_effect(repo_url, file_name):
            if file_name == 'Dockerfile':
                return True  # simulating that Dockerfile exists
            elif file_name == 'package.json':
                return False  # simulating that package.json does not exist
            return False
        
        mock_check_file_existence.side_effect = side_effect

        expected = {
            "languages": ["PHP"],  
            "frameworks": ["Laravel"],
            "build_tools": [],
            "dockerised": True, 
            "dependency_manager": "Composer", 
        }
        result = analyze_php('https://github.com/some/php_repo')
        
        self.assertEqual(result, expected)
        
        # Ensure that the mocks were called with the expected arguments
        mock_fetch_file_from_github.assert_called_once_with('https://github.com/some/php_repo', 'composer.json')
        mock_check_file_existence.assert_any_call('https://github.com/some/php_repo', 'Dockerfile')
        mock_check_file_existence.assert_any_call('https://github.com/some/php_repo', 'package.json')

if __name__ == '__main__':
    unittest.main()
