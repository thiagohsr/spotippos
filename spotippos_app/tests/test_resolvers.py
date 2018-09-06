from api.helpers.resolvers import (
    get_property_by_id,
    get_properties_by_coordinates,
    save_property,
)


class TestResolvers(object):

    def test_should_return_property_with_passed_id(self, app, vcr_replay):
        expected_property = {
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
        property_id = expected_property.get('id')
        with vcr_replay.use_cassette(
            'test_should_return_property_with_passed_id.yaml'
        ):
            with app.app_context():
                response = get_property_by_id(property_id)
                property_json = response.json()
                assert property_json.get('id') == expected_property.get('id')
                assert (
                    property_json.get(
                        'title') == expected_property.get('title')
                )

    def test_should_return_properties_for_given_coordinates(
        self,
        app,
        vcr_replay
    ):
        request_coordinates = {
            'ax': 20,
            'ay': 500,
            'bx': 600,
            'by': 700,
        }
        with vcr_replay.use_cassette(
            'test_should_return_properties_for_given_coordinates.yaml'
        ):
            with app.app_context():
                response = get_properties_by_coordinates(request_coordinates)
                assert response.content.get(
                    'totalProperties'
                ) == len(response.content.get('properties'))

    def test_should_not_return_properties_for_given_coordinates(
        self,
        app,
        vcr_replay
    ):
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
        with vcr_replay.use_cassette(
            'test_should_not_return_properties_for_given_coordinates.yaml'
        ):
            with app.app_context():
                response = get_properties_by_coordinates(request_coordinates)

                assert response.content == expected_response.get('content')
                assert response.status_code == expected_response.get(
                    'status_code'
                )

    def test_should_save_property_data(self, app, vcr_replay):
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

        with vcr_replay.use_cassette(
            'test_should_save_property_data.yaml'
        ):
            with app.app_context():
                response = save_property(propertie_data)
                assert response.content == expected_response['content']
                assert response.status_code == expected_response['status_code']

    def test_should_fail_save_property_parameters_with_wrong_type(
        self,
        app,
        invalid_property,
        vcr_replay
    ):
        expected_status_code = 422
        with vcr_replay.use_cassette(
            'test_should_fail_save_property_parameters_with_wrong_type.yaml'
        ):
            with app.app_context():
                response = save_property(invalid_property)
                for key in invalid_property:
                    assert key in response.content
                assert response.status_code == expected_status_code
