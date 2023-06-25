import pytest
import requests
from jsonschema import validate


@pytest.mark.parametrize('id_post', [1, 10, 25])
def test_get_resource(base_url, id_post):
    response = requests.get(base_url + f'/posts/{id_post}')
    assert response.status_code == 200

    schema = {
        'type': 'object',
        'properties': {
            'userId': {'type': 'number'},
            'id': {'type': 'number'},
            'title': {'type': 'string'},
            'body': {'type': 'string'}
        },
        'required': ['userId', 'id', 'title', 'body']
    }

    validate(instance=response.json(), schema=schema)
    assert response.json().get('id') == id_post


def test_get_all_resources(base_url):
    response = requests.get(base_url + '/posts')
    assert response.status_code == 200

    schema = {
        'type': 'object',
        'properties': {
            'userId': {'type': 'number'},
            'id': {'type': 'number'},
            'title': {'type': 'string'},
            'body': {'type': 'string'}
        },
        'required': ['userId', 'id', 'title', 'body']
    }

    for post in response.json():
        validate(instance=post, schema=schema)


def test_create_resource(base_url):
    headers = {'Content-type': 'application/json; charset=UTF-8'}
    json = {
        'title': 'foo',
        'body': 'bar',
        'userId': 1
    }

    response = requests.post(url=base_url + '/posts', headers=headers, json=json)
    assert response.status_code == 201

    schema = {
        'type': 'object',
        'properties': {
            'userId': {'type': 'number'},
            'id': {'type': 'number'},
            'title': {'type': 'string'},
            'body': {'type': 'string'}
        },
        'required': ['userId', 'id', 'title', 'body']
    }

    validate(instance=response.json(), schema=schema)
    assert response.json().get('title') == json['title']
    assert response.json().get('body') == json['body']
    assert response.json().get('userId') == json['userId']


@pytest.mark.parametrize('id_post, id_user', [(1, 1), (12, 2), (25, 3)], ids=['post 1 user 1',
                                                                              'post 12 user 2',
                                                                              'post 25 user 3'])
def test_update_resource(base_url, id_post, id_user):
    headers = {'Content-type': 'application/json; charset=UTF-8'}
    json = {
        'id': id_post,
        'title': 'foo',
        'body': 'bar',
        'userId': id_user
    }

    response = requests.put(url=base_url + f'/posts/{id_post}', headers=headers, json=json)
    assert response.status_code == 200

    schema = {
        'type': 'object',
        'properties': {
            'userId': {'type': 'number'},
            'id': {'type': 'number'},
            'title': {'type': 'string'},
            'body': {'type': 'string'}
        },
        'required': ['userId', 'id', 'title', 'body']
    }

    validate(instance=response.json(), schema=schema)
    assert response.json().get('title') == json['title']
    assert response.json().get('body') == json['body']
    assert response.json().get('userId') == id_user
    assert response.json().get('id') == id_post


@pytest.mark.parametrize('id_post', [1, 12, 25], ids=['post 1 user 1',
                                                      'post 12 user 2',
                                                      'post 25 user 3'])
def test_delete_resource(base_url, id_post):
    response = requests.delete(base_url + f'/posts/{id_post}')
    assert response.status_code == 200
