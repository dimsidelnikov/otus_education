import pytest
import requests
from jsonschema import validate


def test_get_list_all_breweries(base_url):
    response = requests.get(base_url + '/v1/breweries')
    assert response.status_code == 200

    schema = {
        'type': 'object',
        'required': ['id', 'name', 'brewery_type', 'address_1', 'address_2', 'address_3', 'city', 'state_province',
                     'postal_code', 'country', 'longitude', 'latitude', 'phone', 'website_url', 'state', 'street']
    }

    for brewery in response.json():
        validate(instance=brewery, schema=schema)

    assert len(response.json()) == 50


@pytest.mark.parametrize('num_breweries', [0, 20, 200, 201], ids=['empty list',
                                                                  '20 breweries',
                                                                  'max number breweries 200',
                                                                  'over the max'])
def test_num_breweries_on_page(base_url, num_breweries):
    query = {'per_page': num_breweries}
    max_num_breweries = 200
    response = requests.get(base_url + '/v1/breweries', params=query)
    assert response.status_code == 200
    if num_breweries <= max_num_breweries:
        assert len(response.json()) == num_breweries
    else:
        assert len(response.json()) == max_num_breweries


def test_get_random_brewery(base_url):
    response = requests.get(base_url + '/v1/breweries/random')
    assert response.status_code == 200

    schema = {
        'type': 'object',
        'required': ['id', 'name', 'brewery_type', 'address_1', 'address_2', 'address_3', 'city', 'state_province',
                     'postal_code', 'country', 'longitude', 'latitude', 'phone', 'website_url', 'state', 'street']
    }

    for brewery in response.json():
        validate(instance=brewery, schema=schema)

    assert len(response.json()) == 1


@pytest.mark.parametrize('num_breweries', [1, 10, 50, 51], ids=['1 brewery',
                                                                '10 breweries',
                                                                'max number breweries 50',
                                                                'over the max'])
def test_num_random_breweries(base_url, num_breweries):
    query = {'size': num_breweries}
    max_num_breweries = 50
    response = requests.get(base_url + '/v1/breweries/random', params=query)
    assert response.status_code == 200
    if num_breweries <= max_num_breweries:
        assert len(response.json()) == num_breweries
    else:
        assert len(response.json()) == max_num_breweries


@pytest.mark.parametrize('search_str', ['dog', 'line', 'lot'])
def test_autocomplete(base_url, search_str):
    query = {'query': search_str}
    response = requests.get(base_url + '/v1/breweries/autocomplete', params=query)
    assert response.status_code == 200

    schema = {
        'type': 'object',
        'properties': {
            'id': {'type': 'string'},
            'name': {'type': 'string'}
        },
        'required': ['id', 'name']
    }

    for brewery in response.json():
        validate(instance=brewery, schema=schema)
        assert search_str.casefold() in brewery['name'].casefold()
