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

    @allure.step('Check response status is 200')
    def check_response_status_200(self):
        assert self.response.status_code == 200

    @allure.step('Check response status is 400')
    def check_response_status_400(self):
        assert self.response.status_code == 400

    @allure.step('Check response status is 401')
    def check_response_status_401(self):
        assert self.response.status_code == 401

    @allure.step('Check response status is 403')
    def check_response_status_403(self):
        assert self.response.status_code == 403

    @allure.step('Check response status is 404')
    def check_response_status_404(self):
        assert self.response.status_code == 404

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
