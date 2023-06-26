import pytest
import requests


def test_get_all_breeds(base_url):
    response = requests.get(base_url + '/breeds/list/all')
    assert response.status_code == 200
    assert type(response.json().get('message')) == dict
    assert response.json().get('status') == 'success'


def test_single_random_image(base_url):
    response = requests.get(base_url + '/breeds/image/random')
    assert response.status_code == 200
    assert type(response.json().get('message')) == str
    assert response.json().get('status') == 'success'


@pytest.mark.parametrize('num_images, expected_num', [(1, 1),
                                                      (10, 10),
                                                      (50, 50),
                                                      (51, 50)],
                         ids=['one image', '10 images', 'max value images 50', 'over the max'])
def test_multiple_random_images(base_url, num_images, expected_num):
    response = requests.get(base_url + f'/breeds/image/random/{num_images}')
    assert response.status_code == 200
    assert type(response.json().get('message')) == list
    assert response.json().get('status') == 'success'
    assert len(response.json().get('message')) == expected_num


@pytest.mark.parametrize('breed', ['borzoi', 'husky', 'mastiff'])
def test_all_images_breed(base_url, breed):
    response = requests.get(base_url + f'/breed/{breed}/images')
    assert response.status_code == 200
    assert type(response.json().get('message')) == list
    assert response.json().get('status') == 'success'
    for url_image in response.json().get('message'):
        assert breed.casefold() in url_image.casefold()


@pytest.mark.parametrize('breed', ['boxer', 'bulldog', 'chihuahua'])
def test_random_breed_image(base_url, breed):
    response = requests.get(base_url + f'/breed/{breed}/images/random')
    assert response.status_code == 200
    assert type(response.json().get('message')) == str
    assert response.json().get('status') == 'success'
    assert breed in response.json().get('message')
