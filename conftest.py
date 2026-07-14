import pytest
from endpoints.authorization import Authorization
from endpoints.create_meme import CreateMeme
from endpoints.delete_meme import DeleteMeme
from endpoints.get_meme import GetMeme
from endpoints.update_meme import UpdateMeme


@pytest.fixture(scope='session')
def auth_token():
    auth_service = Authorization()
    payload = {"name": "v_siderchuk"}
    auth_service.new_token(payload=payload)
    return auth_service.json['token']


@pytest.fixture()
def get_meme_endpoint(auth_token):
    return GetMeme(token=auth_token)


@pytest.fixture()
def create_meme_endpoint(auth_token):
    return CreateMeme(token=auth_token)


@pytest.fixture()
def update_meme_endpoint(auth_token):
    return UpdateMeme(token=auth_token)


@pytest.fixture()
def delete_meme_endpoint(auth_token):
    return DeleteMeme(token=auth_token)


@pytest.fixture()
def new_meme_id(create_meme_endpoint, delete_meme_endpoint):
    payload = {
        "text": "This is fine",
        "url": "https://static01.nyt.com/images/2016/08/05/us/05onfire1_xp/05onfire1_xp-superJumbo-v2.jpg",
        "tags": ["dog", "fire", "mug"],
        "info": {"color": "orange", "year": 2026, "popularity": "high"}
    }
    create_meme_endpoint.create_meme(payload=payload)
    yield create_meme_endpoint.meme_id
    delete_meme_endpoint.delete_meme(meme_id=create_meme_endpoint.meme_id)
