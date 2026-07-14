import requests
import allure
from endpoints.endpoint import Endpoint


class GetMeme(Endpoint):
    @allure.step('Get single meme')
    def get_single_meme(self, meme_id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.get(
            f'{self.url}/meme/{meme_id}',
            headers=headers
        )
        if self.response.status_code == 200:
            self.json = self.response.json()
        else:
            self.json = {}
        return self.response

    @allure.step('Get all memes')
    def get_all_memes(self, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.get(
            f'{self.url}/meme',
            headers=headers
        )
        if self.response.status_code == 200:
            self.json = self.response.json()
        else:
            self.json = {}
        return self.response

    @allure.step('Check that memes list is not empty')
    def check_memes_list_is_not_empty(self):
        assert len(self.json) > 0

    @allure.step('Find not mine meme ID')
    def get_not_mine_meme_id(self, my_meme_id):
        self.get_all_memes()
        all_memes = self.json['data']
        for meme in all_memes:
            if meme['id'] != my_meme_id:
                return meme['id']
