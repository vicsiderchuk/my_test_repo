import requests
import allure
from endpoints.endpoint import Endpoint


class UpdateMeme(Endpoint):
    @allure.step('Update a meme')
    def update_meme(self, meme_id, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.put(
            f'{self.url}/meme/{meme_id}',
            json=payload,
            headers=headers
        )
        if self.response.status_code == 200:
            self.json = self.response.json()
        else:
            self.json = {}
        return self.response
