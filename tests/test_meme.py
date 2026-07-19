import pytest
import allure
from data import VALID_CREATE_MEME_PAYLOAD, VALID_UPDATE_MEME_PAYLOAD, INVALID_MEME_PAYLOAD


@allure.feature('Test Memes')
@allure.story('Getting Memes Info')
@allure.title('Get all existent memes')
def test_get_all_memes(get_meme_endpoint):
    get_meme_endpoint.get_all_memes()
    get_meme_endpoint.check_response_status_code(200)
    get_meme_endpoint.check_memes_list_is_not_empty()

@allure.feature('Test Memes')
@allure.story('Getting Memes Info')
@allure.title('Get a single meme')
def test_get_single_meme(get_meme_endpoint, new_meme_id):
    get_meme_endpoint.get_single_meme(meme_id=new_meme_id)
    get_meme_endpoint.check_response_status_code(200)
    get_meme_endpoint.check_meme_id(expected_meme_id=new_meme_id)

@allure.feature('Test Memes')
@allure.story('Manipulating Memes')
@allure.title('Create a new meme')
def test_create_meme(create_meme_endpoint, get_meme_endpoint):
    payload = VALID_CREATE_MEME_PAYLOAD
    create_meme_endpoint.create_meme(payload=payload)
    create_meme_endpoint.check_response_status_code(200)
    create_meme_endpoint.check_id_is_not_none()
    create_meme_endpoint.check_response_fields(expected_payload=payload)
    new_meme_id = create_meme_endpoint.json['id']
    get_meme_endpoint.get_single_meme(meme_id=new_meme_id)
    get_meme_endpoint.check_response_fields(expected_payload=payload)

@allure.feature('Test Memes')
@allure.story('Manipulating Memes')
@allure.title('Update meme')
def test_update_meme(update_meme_endpoint, get_meme_endpoint, new_meme_id):
    payload = VALID_UPDATE_MEME_PAYLOAD.copy()
    payload['id'] = new_meme_id
    update_meme_endpoint.update_meme(meme_id=new_meme_id, payload=payload)
    update_meme_endpoint.check_response_status_code(200)
    update_meme_endpoint.check_meme_id(expected_meme_id=new_meme_id)
    update_meme_endpoint.check_response_fields(expected_payload=payload)
    get_meme_endpoint.get_single_meme(meme_id=new_meme_id)
    get_meme_endpoint.check_response_fields(expected_payload=payload)

@allure.feature('Test Memes')
@allure.story('Manipulating Memes')
@allure.title('Delete meme')
def test_delete_meme(delete_meme_endpoint, get_meme_endpoint, new_meme_id):
    delete_meme_endpoint.delete_meme(meme_id=new_meme_id)
    delete_meme_endpoint.check_response_status_code(200)
    get_meme_endpoint.get_single_meme(meme_id=new_meme_id)
    get_meme_endpoint.check_response_status_code(404)

@allure.feature('Test Memes')
@allure.story('Security')
@allure.title('Impossible to get memes without authorization')
def test_get_meme_without_token(get_meme_endpoint):
    headers_without_token = {'Content-Type': 'application/json'}
    get_meme_endpoint.get_all_memes(headers=headers_without_token)
    get_meme_endpoint.check_response_status_code(401)

@allure.feature('Test Memes')
@allure.story('Validation')
@allure.title('Create meme with invalid data')
@pytest.mark.parametrize('invalid_payload', INVALID_MEME_PAYLOAD)
def test_create_meme_with_invalid_payload(create_meme_endpoint, invalid_payload):
    create_meme_endpoint.create_meme(payload=invalid_payload)
    create_meme_endpoint.check_response_status_code(400)

@allure.feature('Test Memes')
@allure.story('Security')
@allure.title('Impossible update not mine meme')
def test_update_not_mine_meme(get_meme_endpoint, update_meme_endpoint, new_meme_id):
    not_mine_meme_id = get_meme_endpoint.get_not_mine_meme_id(my_meme_id=new_meme_id)
    payload = VALID_UPDATE_MEME_PAYLOAD.copy()
    payload['id'] = not_mine_meme_id
    update_meme_endpoint.update_meme(meme_id=not_mine_meme_id, payload=payload)
    update_meme_endpoint.check_response_status_code(403)
