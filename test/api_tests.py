import requests
import unittest

class APITest(unittest.TestCase):
    # Test GET Routes
    def test_api_get_morse_to_text(self):
        result = requests.get("http://127.0.0.1:8000/morse-to-text/--")
        result_json = result.json()
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result_json, {"original_morse":"--","translated_morse":"M"})

        error_response = requests.get("http://127.0.0.1:8000/morse-to-text/-t-")
        self.assertEqual(error_response.status_code, 400)

    def test_api_get_text_to_morse(self):
        result = requests.get("http://127.0.0.1:8000/text-to-morse/hello")
        result_json = result.json()
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result_json, {"original_text":"hello","translated_text":".... . .-.. .-.. ---"})

        error_response = requests.get("http://127.0.0.1:8000/text-to-morse/ ")
        self.assertEqual(error_response.status_code, 400)

    def test_api_get_validate_morse(self):
        result = requests.get("http://127.0.0.1:8000/validate-morse/--")
        result_json = result.json()
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result_json, {"original_morse":"--","is_morse_valid":True})

        error_response = requests.get("http://127.0.0.1:8000/validate-morse/-------")
        error_response_json = error_response.json()
        self.assertEqual(error_response.status_code, 200)
        self.assertEqual(error_response_json, {"original_morse":"-------","is_morse_valid":False})

    # Test POST Routes
    def test_api_post_morse_to_text(self):
        result = requests.post(
            url="http://127.0.0.1:8000/morse-to-text",
            json={"morse": "-- --- .-. ... . / .. ... / ..-. ..- -."})
        result_json = result.json()
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result_json, {
                        "original_morse":"-- --- .-. ... . / .. ... / ..-. ..- -.", 
                        "translated_morse":"MORSE IS FUN"
                        })
        
        error_response = requests.post(
            url="http://127.0.0.1:8000/morse-to-text",
            json={"morse": "-- --- .-. ... . / .. ... // ..-. ..- -."})
        self.assertEqual(error_response.status_code, 400)

    def test_api_post_text_to_morse(self):
        result = requests.post(
            url="http://127.0.0.1:8000/text-to-morse",
            json={"text": "Hello World!"})
        result_json = result.json()
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result_json, {
                        "original_text":"Hello World!",
                        "translated_text":".... . .-.. .-.. --- / .-- --- .-. .-.. -.. -.-.--"
                        })
        
        error_response = requests.post(
            url="http://127.0.0.1:8000/text-to-morse",
            json={"text": ""})
        self.assertEqual(error_response.status_code, 400)

    def test_api_post_validate_morse(self):
        good_result = requests.post(
            url="http://127.0.0.1:8000/validate-morse",
            json={"morse": ".. -.- .- -.-- / -... --- -.. -.-- .-.-.-"})
        good_result_json = good_result.json()
        self.assertEqual(good_result.status_code, 200)
        self.assertEqual(good_result_json, {
                        "original_morse":".. -.- .- -.-- / -... --- -.. -.-- .-.-.-",
                        "is_morse_valid":True})
        
        error_response = requests.post(
            url="http://127.0.0.1:8000/validate-morse",
            json={"morse": ".. -.- .- -.-- / -... --- -.. -.-- .-.-.-."})
        error_response_json = error_response.json()
        self.assertEqual(error_response.status_code, 200)
        self.assertEqual(error_response_json, {
                        "original_morse":".. -.- .- -.-- / -... --- -.. -.-- .-.-.-.",
                        "is_morse_valid":False})