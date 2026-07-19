import pytest
from endpoints.authorization import Authorization
from endpoints.create_meme import CreateMeme
from endpoints.delete_meme import DeleteMeme
from endpoints.get_meme import GetMeme
from endpoints.update_meme import UpdateMeme
from data import USER_NAME, VALID_CREATE_MEME_PAYLOAD


@pytest.fixture(scope='session')
def auth_token():
    auth_service = Authorization()
    payload = {"name": USER_NAME}
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
    payload = VALID_CREATE_MEME_PAYLOAD
    create_meme_endpoint.create_meme(payload=payload)
    yield create_meme_endpoint.meme_id
    delete_meme_endpoint.delete_meme(meme_id=create_meme_endpoint.meme_id)


@pytest.fixture()
def auth_endpoint():
    return Authorization()
