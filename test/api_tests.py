import unittest
from fastapi.testclient import TestClient
from api.app import app

client = TestClient(app)


class APITest(unittest.TestCase):
    # Test GET Routes
    def test_api_get_morse_to_text(self):
        result = client.get("/morse-to-text/--")
        result_json = result.json()
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result_json, {"original_morse": "--", "translated_morse": "M"})

        error_response = client.get("/morse-to-text/-t-")
        self.assertEqual(error_response.status_code, 400)

    def test_api_get_text_to_morse(self):
        result = client.get("/text-to-morse/hello")
        result_json = result.json()
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result_json, {"original_text": "hello", "translated_text": ".... . .-.. .-.. ---"})

        error_response = client.get("/text-to-morse/ ")
        self.assertEqual(error_response.status_code, 400)

    def test_api_get_validate_morse(self):
        result = client.get("/validate-morse/--")
        result_json = result.json()
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result_json, {"original_morse": "--", "is_morse_valid": True})

        error_response = client.get("/validate-morse/-------")
        error_response_json = error_response.json()
        self.assertEqual(error_response.status_code, 200)
        self.assertEqual(error_response_json, {"original_morse": "-------", "is_morse_valid": False})

    # Test POST Routes
    def test_api_post_morse_to_text(self):
        result = client.post(
            "/morse-to-text",
            json={"morse": "-- --- .-. ... . / .. ... / ..-. ..- -."}
        )
        result_json = result.json()
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result_json, {
            "original_morse": "-- --- .-. ... . / .. ... / ..-. ..- -.",
            "translated_morse": "MORSE IS FUN"
        })

        error_response = client.post(
            "/morse-to-text",
            json={"morse": "-- --- .-. ... . / .. ... // ..-. ..- -."}
        )
        self.assertEqual(error_response.status_code, 400)

    def test_api_post_text_to_morse(self):
        result = client.post(
            "/text-to-morse",
            json={"text": "Hello World!"}
        )
        result_json = result.json()
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result_json, {
            "original_text": "Hello World!",
            "translated_text": ".... . .-.. .-.. --- / .-- --- .-. .-.. -.. -.-.--"
        })

        error_response = client.post(
            "/text-to-morse",
            json={"text": ""}
        )
        self.assertEqual(error_response.status_code, 400)

    def test_api_post_validate_morse(self):
        good_result = client.post(
            "/validate-morse",
            json={"morse": ".. -.- .- -.-- / -... --- -.. -.-- .-.-.-"}
        )
        good_result_json = good_result.json()
        self.assertEqual(good_result.status_code, 200)
        self.assertEqual(good_result_json, {
            "original_morse": ".. -.- .- -.-- / -... --- -.. -.-- .-.-.-",
            "is_morse_valid": True
        })

        error_response = client.post(
            "/validate-morse",
            json={"morse": "--- -.- .- -.-- / -... --- -.. -.-- .-.-.-."}
        )
        error_response_json = error_response.json()
        self.assertEqual(error_response.status_code, 200)
        self.assertEqual(error_response_json, {
            "original_morse": "--- -.- .- -.-- / -... --- -.. -.-- .-.-.-.",
            "is_morse_valid": False
        })