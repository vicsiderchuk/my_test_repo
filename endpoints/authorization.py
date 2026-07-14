import requests
import allure
from endpoints.endpoint import Endpoint


class Authorization(Endpoint):
    @allure.step('Request a new token')
    def new_token(self, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(
            f'{self.url}/authorize',
            json=payload,
            headers=headers
        )
        self.json = self.response.json()
        return self.response

    @allure.step('Check if token is alive')
    def check_token(self, token, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.get(
            f'{self.url}/authorize/{token}',
            headers=headers
        )
        return self.response
