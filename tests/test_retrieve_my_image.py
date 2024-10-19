# tests/aws/lambda/test_retrieve_my_image.py

import unittest
from unittest.mock import patch, mock_open
from aws.lambdas.retrieve_my_image import lambda_handler

class TestLambdaHandler(unittest.TestCase):
    
    @patch("builtins.open", new_callable=mock_open, read_data=b"fake_image_data")
    @patch("os.path.dirname", return_value="/mock/path")
    @patch("os.path.join", side_effect=lambda *args: "/mock/path/img/feup_1.jpg")  # Change to your image file
    def test_lambda_handler_success(self, mock_join, mock_dirname, mock_open):
        # Arrange
        event = {}
        context = {}
        
        # Act
        response = lambda_handler(event, context)
        
        # Assert
        self.assertEqual(response['statusCode'], 200)
        self.assertIn('<h1>Faculty logo:</h1>', response['body'])
        self.assertIn("data:image/jpeg;base64,", response['body'])  # Ensure base64 image is present
    
    @patch("builtins.open", side_effect=FileNotFoundError)
    @patch("os.path.dirname", return_value="/mock/path")
    @patch("os.path.join", side_effect=lambda *args: "/mock/path/img/feup_1.jpg")
    def test_lambda_handler_file_not_found(self, mock_join, mock_dirname, mock_open):
        # Arrange
        event = {}
        context = {}
        
        # Act
        response = lambda_handler(event, context)
        
        # Assert
        self.assertEqual(response['statusCode'], 500)
        self.assertIn("Error loading image", response['body'])

if __name__ == "__main__":
    unittest.main()