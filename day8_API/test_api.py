import time
import requests
import pytest

base_url = 'https://jsonplaceholder.typicode.com/'
HTTP_code = 200
url = 'https://playground.learnqa.ru/api/'


@pytest.mark.skip
def test_get_all_posts():
    response = requests.get(f'{base_url}posts')
    assert response.status_code == HTTP_code, 'wrong status code'
    assert len(response.json()) == 100


def test_get_post1():
    response = requests.get(f'{base_url}posts/1')
    assert response.status_code == HTTP_code, 'wrong status code'
    response_data = response.json()
    expected_keys = ['userId', 'id', 'title', 'body']
    for key in response_data.keys():
        assert key in expected_keys, 'wrong keys'


def test_post_in_posts():
    post_data = {
        'id': 101,
        'title': 'my title',
        'body': 'my body'
    }
    response = requests.post(f'{base_url}posts/', data=post_data)
    assert response.status_code == 201, 'wrong status code'
    response_data = response.json()
    expected_title = 'my title'
    assert response_data['title'] == expected_title


def get_all_names():
    response = requests.get(f'{base_url}users/')
    response_data = response.json()
    name_list = []
    for i, name in enumerate(response_data):
        name_list.append((i + 1, response_data[i]['name']))
    return name_list


@pytest.mark.parametrize('userID, expected_name', get_all_names())
def test_get_all_users_name(userID, expected_name):
    response = requests.get(f'{base_url}users/{userID}')
    response_data = response.json()
    assert response_data['name'] == expected_name, 'wrong name'


def test_end_to_end():
    new_user = {
        'userId': '55',
        'id': '555',
        'title': 'my last name',
        'body': '12345'
    }

    response = requests.post(f'{base_url}posts', data=new_user)
    assert response.status_code == 201

    response_data = response.json()
    # assert id in response_data.keys
