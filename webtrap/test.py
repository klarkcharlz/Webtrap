# перед запуском тестов запустите отдельно сервер

import unittest
import requests  # для отправки запросов


class TestingWebtrap(unittest.TestCase):

    @staticmethod
    def read_log():
        with open('Webtrap.log') as log:
            logs = log.readlines()
            return logs[-1].strip()

    def test_post(self):
        # проверка пост запроса
        response = requests.post('http://127.0.0.1:5000/api/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.read_log(), 'Not supported method: POST')

    def test_invalid_arguments(self):
        # проверка не валидных аргументов
        response = requests.get('http://127.0.0.1:5000/api/', {'invalid': 1})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.read_log(), 'Invalid arguments in request!')

    def test_not_api(self):
        # проверка не валидных url
        response = requests.get('http://127.0.0.1:5000/notapi/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.read_log(), 'Not api url: http://127.0.0.1:5000/notapi/')


if __name__ == "__main__":
    unittest.main()
