# -*- encoding:utf-8 -*-
from api.schemas import PropertieSchema
from collections import namedtuple
from marshmallow import ValidationError
from api.constants import PROVINCES


def schema_validation(data):
    response_dict = namedtuple('response', 'content status_code')

    schema = PropertieSchema()
    try:
        return schema.load(data)
    except ValidationError as errors:
        response_dict.content = errors.messages
        response_dict.status_code = 422
        return response_dict


def match_properties(properties_list, coordinates):
    response_dict = namedtuple('response', 'content status_code')
    min_long = int(coordinates.get('ax'))
    min_lat = int(coordinates.get('ay'))
    max_long = int(coordinates.get('bx'))
    max_lat = int(coordinates.get('by'))
    properties = []
    for propertie in properties_list.json():
        if min_long <= propertie['x'] <= max_long and min_lat <= propertie['y'] <= max_lat:
            properties.append(propertie)

    if len(properties):
        response_dict.content = {
            'totalProperties': len(properties),
            'properties': properties
        }
        response_dict.status_code = properties_list.status_code
        return response_dict

    response_dict.content = 'Nenhum imóvel encontrado'
    response_dict.status_code = 404
    return response_dict


def match_provinces(longitude, latitude):
    # Include province on Propertie data
    provinces = []
    for province in PROVINCES.items():
        max_long = province[1]['boundaries']['bottomRight']['x']
        max_lat = province[1]['boundaries']['upperLeft']['y']
        min_long = province[1]['boundaries']['upperLeft']['x']
        min_lat = province[1]['boundaries']['bottomRight']['y']

        if min_long <= int(longitude) <= max_long and min_lat <= int(latitude) <= max_lat:
            provinces.append(province[0])

    return provinces
