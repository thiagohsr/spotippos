# -*- encoding: utf-8 -*-
import json
import requests
from collections import namedtuple

from api.constants import (
    HEADER_JSON_CONTENT,
    ERROR_MESSAGES,
    SUCCESS_MESSAGES,
)
from api.helpers.propertie import match_provinces, match_properties

from flask import current_app as app


def get_propertie_by_id(propertie_ground_id):
    url = '{host}/{endpoint}/{propertie_ground_id}'.format(
        host=app.config.get('DATA_API_HOST'),
        endpoint=app.config.get('PROPERTIES_ENDPOINT'),
        propertie_ground_id=propertie_ground_id
    )

    response = requests.get(url)
    return response


def get_properties_by_coordinates(coordinates):
    url = '{host}/{endpoint}/'.format(
        host=app.config.get('DATA_API_HOST'),
        endpoint=app.config.get('PROPERTIES_ENDPOINT')
    )

    response = requests.get(url)

    properties = match_properties(
        response,
        coordinates
    )

    return properties


def save_propertie(propertie_data):
    response_dict = namedtuple('response', 'content status_code')

    url = '{host}/{endpoint}'.format(
        host=app.config.get('DATA_API_HOST'),
        endpoint=app.config.get('PROPERTIES_ENDPOINT')
    )

    provinces = match_provinces(
        longitude=propertie_data.get('x'), latitude=propertie_data.get('y')
    )

    if provinces:
        propertie_data.update({'provinces': provinces})

    response = requests.post(
        url, data=json.dumps(propertie_data), headers=HEADER_JSON_CONTENT
    )

    response_dict.content = (
        SUCCESS_MESSAGES[response.status_code].format(
            title=response.json()['title'],
            provinces=provinces,
        )
    )
    response_dict.status_code = response.status_code

    return response_dict
