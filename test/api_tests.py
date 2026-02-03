import unittest
from fastapi.testclient import TestClient
from api.app import app
from views.messages import APIMessages
from api.routes.routes import MorseToText, TextToMorse, MorseValidation, Root, HealthCheck
from api.routes.versions import CurrentVersion

class APITest(unittest.TestCase):
    """
    Unit tests for the Morse Translator API endpoints.
    This test class validates the functionality of GET and POST routes for:
    - Converting morse code to text
    - Converting text to morse code
    - Validating morse code patterns
    The tests verify:
    - Successful translations with correct status codes and response formats
    - Proper error handling for invalid inputs
    - Response JSON structure contains expected keys
    - Translated values match expected results
    """
    def setUp(self):
        self.client = TestClient(app)
        
    # Test GET Routes
    def test_api_get_morse_to_text(self):
        test_morse: str = "--"
        test_expected_result: str = "M"
        original_key: str = APIMessages.api_original_morse_key
        translated_key: str = APIMessages.api_translated_morse_key
        url: str = CurrentVersion.current_version_route+MorseToText.route+f'/{test_morse}'
        result = self.client.get(url)
        result_json = result.json()
        self.assertEqual(result.status_code, 200)
        self.assertIn(original_key, result_json)
        self.assertIn(translated_key, result_json)
        self.assertEqual(result_json[original_key], test_morse)
        self.assertEqual(result_json[translated_key], test_expected_result)

        error_response_test_morse: str = "-t-"
        error_response_url: str = CurrentVersion.current_version_route+MorseToText.route+f'/{error_response_test_morse}'
        error_response = self.client.get(error_response_url)
        self.assertEqual(error_response.status_code, 400)

    def test_api_get_text_to_morse(self):
        test_word: str = "hello"
        test_expected_result: str = ".... . .-.. .-.. ---"
        original_key: str = APIMessages.api_original_text_key
        translated_key: str = APIMessages.api_translated_text_key
        url: str = CurrentVersion.current_version_route+TextToMorse.route+f'/{test_word}'
        result = self.client.get(url)
        result_json = result.json()
        self.assertEqual(result.status_code, 200)
        self.assertIn(original_key, result_json)
        self.assertIn(translated_key, result_json)
        self.assertEqual(result_json[original_key], test_word)
        self.assertEqual(result_json[translated_key], test_expected_result)

        error_response_test_morse: str = " "
        error_response_url: str = CurrentVersion.current_version_route+TextToMorse.route+f'/{error_response_test_morse}'
        error_response = self.client.get(error_response_url)
        self.assertEqual(error_response.status_code, 400)

    def test_api_get_validate_morse(self):
        test_morse: str = "--"
        test_expected_result: bool = True
        original_key: str = APIMessages.api_original_morse_key
        validation_key: str = APIMessages.api_morse_validation_check_key
        url: str = CurrentVersion.current_version_route+MorseValidation.route+f'/{test_morse}'
        result = self.client.get(url)
        good_result_json = result.json()
        self.assertEqual(result.status_code, 200)
        self.assertIn(original_key, good_result_json)
        self.assertIn(validation_key, good_result_json)
        self.assertEqual(good_result_json[original_key], test_morse)
        self.assertEqual(good_result_json[validation_key], test_expected_result)

        error_response_test_morse: str = "-------"
        error_response_test_expected_result: bool = False
        error_response_url = CurrentVersion.current_version_route+MorseValidation.route+f'/{error_response_test_morse}'
        error_response = self.client.get(error_response_url)
        error_response_json = error_response.json()
        self.assertEqual(error_response.status_code, 200)
        self.assertIn(original_key, error_response_json)
        self.assertIn(validation_key, error_response_json)
        self.assertEqual(error_response_json[original_key], error_response_test_morse)
        self.assertEqual(error_response_json[validation_key], error_response_test_expected_result)

    # Test POST Routes
    def test_api_post_morse_to_text(self):
        test_morse: str = "-- --- .-. ... . / .. ... / ..-. ..- -."
        test_expected_result: str = "MORSE IS FUN"
        original_key: str = APIMessages.api_original_morse_key
        translated_key: str = APIMessages.api_translated_morse_key
        url: str = CurrentVersion.current_version_route+MorseToText.route
        test_json: dict[str, str] = {"morse": test_morse}
        
        result = self.client.post(url, json=test_json)
        result_json = result.json()
        
        self.assertEqual(result.status_code, 200)
        self.assertIn(original_key, result_json)
        self.assertIn(translated_key, result_json)
        self.assertEqual(result_json[original_key], test_morse)
        self.assertEqual(result_json[translated_key], test_expected_result)
        
        error_response_test_morse: str = "-- --- .-. ... . / .. ... // ..-. ..- -."
        error_response_test_json: dict[str, str] = {"morse": error_response_test_morse}
        error_response = self.client.post(url, json=error_response_test_json)
        self.assertEqual(error_response.status_code, 400)

    def test_api_post_text_to_morse(self):
        test_word: str = "Hello World!"
        test_expected_result: str = ".... . .-.. .-.. --- / .-- --- .-. .-.. -.. -.-.--"
        original_key: str = APIMessages.api_original_text_key
        translated_key: str = APIMessages.api_translated_text_key
        url: str = CurrentVersion.current_version_route+TextToMorse.route
        test_json: dict[str, str] = {"text": test_word}
        
        result = self.client.post(url, json=test_json)
        result_json = result.json()
        
        self.assertEqual(result.status_code, 200)
        self.assertIn(original_key, result_json)
        self.assertIn(translated_key, result_json)
        self.assertEqual(result_json[original_key], test_word)
        self.assertEqual(result_json[translated_key], test_expected_result)

        error_response_test_morse: str = ""
        error_response_test_json: dict[str, str] = {"text": error_response_test_morse}
        error_response = self.client.post(url, json=error_response_test_json)
        self.assertEqual(error_response.status_code, 400)

    def test_api_post_validate_morse(self):
        test_morse: str = ".. -.- .- -.-- / -... --- -.. -.-- .-.-.-"
        test_expected_result: bool = True
        original_key: str = APIMessages.api_original_morse_key
        validation_key: str = APIMessages.api_morse_validation_check_key
        url: str = CurrentVersion.current_version_route+MorseValidation.route
        test_json: dict[str, str] = {"morse": test_morse}
        
        good_result = self.client.post(url, json=test_json)
        good_result_json = good_result.json()
        
        self.assertEqual(good_result.status_code, 200)
        self.assertIn(original_key, good_result_json)
        self.assertIn(validation_key, good_result_json)
        self.assertEqual(good_result_json[original_key], test_morse)
        self.assertEqual(good_result_json[validation_key], test_expected_result)
        
        error_response_test_morse: str = "--- -.- .- -.-- / -... --- -.. -.-- .-.-.-."
        error_response_test_expected_result: bool = False
        error_response_test_json: dict[str, str] = {"morse": error_response_test_morse}
        
        error_response = self.client.post(url, json=error_response_test_json)
        error_response_json = error_response.json()
        
        self.assertEqual(error_response.status_code, 200)
        self.assertIn(original_key, error_response_json)
        self.assertIn(validation_key, error_response_json)
        self.assertEqual(error_response_json[original_key],  error_response_test_morse)
        self.assertEqual(error_response_json[validation_key], error_response_test_expected_result)