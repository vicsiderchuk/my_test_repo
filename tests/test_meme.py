import pytest
import allure


@allure.feature('Test Memes')
@allure.story('Getting Memes Info')
@allure.title('Get all existent memes')
def test_get_all_memes(get_meme_endpoint):
    get_meme_endpoint.get_all_memes()
    get_meme_endpoint.check_response_status_200()
    get_meme_endpoint.check_memes_list_is_not_empty()

@allure.feature('Test Memes')
@allure.story('Getting Memes Info')
@allure.title('Get a single meme')
def test_get_single_meme(get_meme_endpoint, new_meme_id):
    get_meme_endpoint.get_single_meme(meme_id=new_meme_id)
    get_meme_endpoint.check_response_status_200()
    get_meme_endpoint.check_meme_id(expected_meme_id=new_meme_id)

@allure.feature('Test Memes')
@allure.story('Manipulating Memes')
@allure.title('Create a new meme')
def test_create_meme(create_meme_endpoint, get_meme_endpoint):
    payload = {
        "text": "My English skills",
        "url": "https://i.pinimg.com/236x/4e/01/d8/4e01d8a71b197ea3b500dec47cff04fc.jpg",
        "tags": ["dino", "expectations", "reality"],
        "info": {"color": "white", "year": 2026, "popularity": "low"}
    }
    create_meme_endpoint.create_meme(payload=payload)
    create_meme_endpoint.check_response_status_200()
    create_meme_endpoint.check_id_is_not_none()
    create_meme_endpoint.check_response_fields(expected_payload=payload)
    new_meme_id = create_meme_endpoint.json['id']
    get_meme_endpoint.get_single_meme(meme_id=new_meme_id)
    get_meme_endpoint.check_response_fields(expected_payload=payload)

@allure.feature('Test Memes')
@allure.story('Manipulating Memes')
@allure.title('Update meme')
def test_update_meme(update_meme_endpoint, get_meme_endpoint, new_meme_id):
    payload = {
        "id": new_meme_id,
        "text": "No stress, just vibing",
        "url": "https://img.magnific.com/free-vector/simple-vibing-cat-square-meme_742173-4493.jpg?semt=ais_hybrid&w=740&q=80",
        "tags": ["dino_UPD", "expectations"],
        "info": {"year": 2026, "popularity": "low", "new_info":"test123!_UPD"}
    }
    update_meme_endpoint.update_meme(meme_id=new_meme_id, payload=payload)
    update_meme_endpoint.check_response_status_200()
    update_meme_endpoint.check_meme_id(expected_meme_id=new_meme_id)
    update_meme_endpoint.check_response_fields(expected_payload=payload)
    get_meme_endpoint.get_single_meme(meme_id=new_meme_id)
    get_meme_endpoint.check_response_fields(expected_payload=payload)

@allure.feature('Test Memes')
@allure.story('Manipulating Memes')
@allure.title('Delete meme')
def test_delete_meme(delete_meme_endpoint, get_meme_endpoint, new_meme_id):
    delete_meme_endpoint.delete_meme(meme_id=new_meme_id)
    delete_meme_endpoint.check_response_status_200()
    get_meme_endpoint.get_single_meme(meme_id=new_meme_id)
    get_meme_endpoint.check_response_status_404()

@allure.feature('Test Memes')
@allure.story('Security')
@allure.title('Impossible to get memes without authorization')
def test_get_meme_without_token(get_meme_endpoint):
    headers_without_token = {'Content-Type': 'application/json'}
    get_meme_endpoint.get_all_memes(headers=headers_without_token)
    get_meme_endpoint.check_response_status_401()

@allure.feature('Test Memes')
@allure.story('Validation')
@allure.title('Check that text field is required')
def test_create_meme_without_text(create_meme_endpoint):
    invalid_payload = {
        "text": None,
        "url": "https://img.magnific.com/free-vector/simple-vibing-cat-square-meme_742173-4493.jpg?semt=ais_hybrid&w=740&q=80",
        "tags": ["dino_UPD", "expectations"],
        "info": {"year": 2026, "popularity": "low", "new_info": "test123!_UPD"}
    }
    create_meme_endpoint.create_meme(payload=invalid_payload)
    create_meme_endpoint.check_response_status_400()

@allure.feature('Test Memes')
@allure.story('Security')
@allure.title('Impossible update not mine meme')
def test_update_not_mine_meme(get_meme_endpoint, update_meme_endpoint, new_meme_id):
    not_mine_meme_id = get_meme_endpoint.get_not_mine_meme_id(my_meme_id=new_meme_id)
    payload = {
        "id": not_mine_meme_id,
        "text": "UPD by autotest",
        "url": "UPD by autotest",
        "tags": ["UPD by autotest"],
        "info": {"new_info":"UPD by autotest"}
    }
    update_meme_endpoint.update_meme(meme_id=not_mine_meme_id, payload=payload)
    update_meme_endpoint.check_response_status_403()
