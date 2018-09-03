# -*- encoding:utf-8 -*-
from api.schemas import PropertieSchema
from collections import namedtuple
from marshmallow import ValidationError
from api.constants import PROVINCES


def schema_validation(data):
    response_dict = namedtuple('response', 'content status_code')

    schema = PropertieSchema()
    try:
        schema.load(data)

    except ValidationError as errors:
        response_dict.content = errors.messages
        response_dict.status_code = 422
        return response_dict.content, response_dict.status_code


def match_properties(properties_list, coordinates):
    results = []
    for propertie in properties_list.json():
        min_long = int(coordinates.get('ax'))
        min_lat = int(coordinates.get('ay'))
        max_long = int(coordinates.get('bx'))
        max_lat = int(coordinates.get('by'))
        if min_long <= propertie['x'] <= max_long and min_lat <= propertie['y'] <= max_lat:
            results.append(propertie)

    if len(results):
        return {
            'totalProperties': len(results),
            'properties': results
        }, properties_list.status_code

    return {'content': 'Nenhum imóvel encontrado'}, 404


def match_provinces(longitude, latitude):
    # Include province on Propertie data
    provinces = []
    for province in PROVINCES.items():
        max_long = province[1]['boundaries']['bottomRight']['x']
        max_lat = province[1]['boundaries']['upperLeft']['y']
        min_long = province[1]['boundaries']['upperLeft']['x']
        min_lat = province[1]['boundaries']['bottomRight']['y']

        if min_long <= longitude <= max_long and min_lat <= latitude <= max_lat:
            provinces.append(province[0])

    return provinces
