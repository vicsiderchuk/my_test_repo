import pytest
import allure
from data import USER_NAME
from data import INVALID_AUTH_PAYLOAD


@allure.feature('Authorization')
@allure.story('Token generation')
@allure.title('Getting token with valid user name')
def test_successful_authorization(auth_endpoint):
    payload = {"name": USER_NAME}
    auth_endpoint.new_token(payload=payload)
    auth_endpoint.check_response_status_code(200)
    auth_endpoint.check_response_has_token()
    token = auth_endpoint.json['token']
    auth_endpoint.check_token(token=token)
    auth_endpoint.check_response_status_code(200)

@allure.feature('Authorization')
@allure.story('Token generation')
@allure.title('Impossible to get token with invalid user name')
@pytest.mark.parametrize('invalid_payload', INVALID_AUTH_PAYLOAD)
def test_failed_authorization(auth_endpoint, invalid_payload):
    auth_endpoint.new_token(payload=invalid_payload)
    auth_endpoint.check_response_status_code(400)
