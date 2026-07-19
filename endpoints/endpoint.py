import allure


class Endpoint:
    url = 'http://memesapi.course.qa-practice.com'
    response = None
    json = None
    def __init__(self, token=None):
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': token
        }

    @allure.step('Check response status code is {expected_status_code}')
    def check_response_status_code(self, expected_status_code):
        assert self.response.status_code == expected_status_code, \
            f'Expected status code {expected_status_code}, but got {self.response.status_code}'

    @allure.step('Check that returned ID is the same as requested ID')
    def check_meme_id(self, expected_meme_id):
        if 'data' in self.json:
            meme_id = self.json['data']['id']
        else:
            meme_id = self.json['id']
        assert str(meme_id) == str(expected_meme_id)

    @allure.step('Check that response contains ID')
    def check_id_is_not_none(self):
        assert self.json.get('id') is not None

    @allure.step('Check that fields in response match fields in requested payload')
    def check_response_fields(self, expected_payload):
        assert self.json['text'] == expected_payload['text']
        assert self.json['url'] == expected_payload['url']
        assert self.json['tags'] == expected_payload['tags']
        assert self.json['info'] == expected_payload['info']

    @allure.step('Check that response has token')
    def check_response_has_token(self):
        assert 'token' in self.json
        assert self.json['token']
