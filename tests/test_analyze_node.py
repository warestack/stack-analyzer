from unittest.mock import patch
import unittest
import json
from analyzers.node_analyzer import analyze_node

class TestAnalyzeNode(unittest.TestCase):
    
    @patch('analyzers.node_analyzer.fetch_file_from_github')
    @patch('analyzers.node_analyzer.check_file_existence_in_repo')
    def test_framework_detection_with_express(self, mock_check_file_existence, mock_fetch_file_from_github):
        # setting up the mock to return False for any file check except 'yarn.lock'
        def side_effect(repo_url, file_name):
            if file_name == 'yarn.lock':
                return True  # simulating that yarn.lock exists
            return False  # simulating that other files do not exist
        
        mock_check_file_existence.side_effect = side_effect

        # mock for fetch_file_from_github to return a package.json as if it was fetched
        mock_fetch_file_from_github.return_value = json.dumps({
            "dependencies": {"express": "^4.17.1"}
        })

        expected = {
            "languages": ["JavaScript"],
            "frameworks": ["Express.js"],
            "build_tools": [],
            "dockerised": False,
            "dependency_manager": "yarn",
        }
        result = analyze_node('https://github.com/some/repo')
        
        self.assertEqual(result, expected)
        
        # You can check that the mock was called with any of these files
        mock_check_file_existence.assert_any_call('https://github.com/some/repo', 'yarn.lock')
        mock_check_file_existence.assert_any_call('https://github.com/some/repo', 'docker-compose.yml')

if __name__ == '__main__':
    unittest.main()
