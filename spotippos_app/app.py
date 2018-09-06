

from flask import Flask
from flask_restful import Api

from api.resources.spotippos import Spotippos


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    api = Api(app, prefix='/api/v1')

    api.add_resource(
        Spotippos,
        '/properties/',
        '/properties/<int:propertie_ground_id>',
        endpoint='spotippos_properties'
    )

    return app


if __name__ == '__main__':
    app = create_app()
    app.run()
