# -*- coding: utf-8 -*-

from flask import Flask
from flask_restful import Api

from api.resources.spotippos import Spotippos

app = Flask(__name__)
api = Api(app, prefix='/api/v1')

api.add_resource(
    Spotippos,
    '/properties/',
    '/properties/<int:propertie_ground_id>',
    endpoint='spotippos_properties'
)

if __name__ == '__main__':
    app.run(debug=True)
