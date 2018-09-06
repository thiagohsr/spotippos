import json
import requests
from collections import namedtuple

from api.constants import (
    HEADER_JSON_CONTENT,
    ERROR_MESSAGES,
    SUCCESS_MESSAGES,
)

from api.helpers.property import (
    schema_validation
)

from api.helpers.property import match_provinces, match_properties

from flask import current_app as app


def get_property_by_id(propertie_ground_id):
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


def save_property(property_data):
    response_dict = namedtuple('response', 'content status_code')

    url = '{host}/{endpoint}'.format(
        host=app.config.get('DATA_API_HOST'),
        endpoint=app.config.get('PROPERTIES_ENDPOINT')
    )

    valid_property = schema_validation(property_data)
    if hasattr(valid_property, 'content'):
        return valid_property

    provinces = match_provinces(
        longitude=property_data.get('x'), latitude=property_data.get('y')
    )

    if provinces:
        property_data.update({'provinces': provinces})

    response = requests.post(
        url, data=json.dumps(property_data), headers=HEADER_JSON_CONTENT
    )

    response_dict.content = (
        SUCCESS_MESSAGES[response.status_code].format(
            title=response.json()['title'],
            provinces=provinces,
        )
    )
    response_dict.status_code = response.status_code

    return response_dict
