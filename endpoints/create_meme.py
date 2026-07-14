import requests
import allure
from endpoints.endpoint import Endpoint


class CreateMeme(Endpoint):
    @allure.step('Create a new meme')
    def create_meme(self, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(
            f'{self.url}/meme',
            json=payload,
            headers=headers
        )
        if self.response.status_code == 200:
            self.json = self.response.json()
            self.meme_id = self.json['id']
        else:
            self.json = {}
            self.meme_id = None
        return self.response
