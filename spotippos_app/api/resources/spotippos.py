# -*- coding: utf-8 -*-

from api.constants import (
    ERROR_MESSAGES
)

from api.helpers.resolvers import (
    get_propertie_by_id,
    get_properties_by_coordinates,
    save_propertie
)

from flask import request
from flask_restful import Resource


class Spotippos(Resource):

    def get(self, propertie_ground_id=None):

        if propertie_ground_id:
            response = get_propertie_by_id(propertie_ground_id)
            return (
                response.json() if response.ok else ERROR_MESSAGES.get(
                    response.status_code
                ), response.status_code
            )

        if len(request.args):
            response = get_properties_by_coordinates(request.args)
            return response.content, response.status_code

        return ERROR_MESSAGES.get(404), 404

    def post(self):
        propertie_data = request.json

        response = save_propertie(propertie_data)

        return response.content, response.status_code
