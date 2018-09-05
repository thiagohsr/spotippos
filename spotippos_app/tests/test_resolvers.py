import pytest
import vcr

from api.helpers.resolvers import (
    get_propertie_by_id,
    get_properties_by_coordinates,
    save_propertie,
)

my_vcr = vcr.VCR(
    serializer='yaml',
    cassette_library_dir='tests/fixtures/cassettes',
    record_mode='once',
    match_on=['uri', 'method'],
)


class TestResolvers(object):

    def test_should_return_propertie_with_passed_id(self, app):
        expected_propertie = {
            'id': 1,
            'title': 'Imóvel código 1, com 5 quartos e 4 banheiros',
            'price': 1250000,
            'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
            'x': 870,
            'y': 867,
            'beds': 5,
            'baths': 4,
            'provinces': [
                'Scavy'
            ],
            'squareMeters': 134,
        }
        propertie_id = expected_propertie.get('id')
        with my_vcr.use_cassette(
            'test_should_return_propertie_with_passed_id.yaml'
        ):
            with app.app_context():
                response = get_propertie_by_id(propertie_id)
                propertie_json = response.json()
                assert propertie_json.get('id') == expected_propertie.get('id')
                assert (
                    propertie_json.get(
                        'title') == expected_propertie.get('title')
                )

    def test_should_return_properties_for_given_coordinates(self, app):
        request_coordinates = {
            'ax': 20,
            'ay': 500,
            'bx': 600,
            'by': 700,
        }
        with my_vcr.use_cassette(
            'test_should_return_properties_for_given_coordinates.yaml'
        ):
            with app.app_context():
                response = get_properties_by_coordinates(request_coordinates)
                assert response.content.get(
                    'totalProperties'
                ) == len(response.content.get('properties'))

    def test_should_not_return_properties_for_given_coordinates(self, app):
        request_coordinates = {
            'ax': 0,
            'ay': 0,
            'bx': 0,
            'by': 0,
        }
        expected_response = {
            'content': 'Nenhum imóvel encontrado',
            'status_code': 404
        }
        with my_vcr.use_cassette(
            'test_should_not_return_properties_for_given_coordinates.yaml'
        ):
            with app.app_context():
                response = get_properties_by_coordinates(request_coordinates)

                assert response.content == expected_response.get('content')
                assert response.status_code == expected_response.get(
                    'status_code'
                )

    def test_should_save_propertie_data(self, app):
        propertie_data = {
            'beds': 4,
            'price': 971000,
            'baths': 3,
            'title': 'Imóvel código 4125, com 4 quartos e 3 banheiros.',
            'description': (
                'Occaecat excepteur officia excepteur sit. '
                'Qui magna amet fugiat laborum enim.'
            ),
            'y': 141,
            'x': 101,
            'squareMeters': 93,
        }
        expected_response = {
            'content': (
                "Created Propertie: Imóvel código 4125, com 4 quartos "
                "e 3 banheiros. in ['Scavy'] province(s)"
            ),
            'status_code': 201
        }

        with my_vcr.use_cassette(
            'test_should_save_propertie_data.yaml'
        ):
            with app.app_context():
                response = save_propertie(propertie_data)
                assert response.content == expected_response['content']
                assert response.status_code == expected_response['status_code']

    def test_should_fail_save_propertie_parameters_with_wrong_type(
        self,
        app,
        invalid_propertie
    ):
        expected_status_code = 422
        with my_vcr.use_cassette(
            'test_should_fail_save_propertie_parameters_with_wrong_type.yaml'
        ):
            with app.app_context():
                response = save_propertie(invalid_propertie)
                for key in invalid_propertie:
                    assert key in response.content
                assert response.status_code == expected_status_code
