import mock
import pytest

from api.helpers.property import (
    match_provinces,
    match_properties,
    schema_validation,
)


class TestHelpers(object):
    def test_should_return_provinces_to_given_coordinates(self):
        gode_coordinates = {
            'x': 0,
            'y': 500,
        }
        expected_provinces = ['Gode', 'Scavy']
        longitude = gode_coordinates.get('x')
        latitude = gode_coordinates.get('y')
        provinces = match_provinces(
            longitude=longitude, latitude=latitude
        )

        assert len(provinces)
        assert set(provinces) == set(expected_provinces)

    def test_should_return_properties_to_given_properties_list_and_coordinates(
        self, properties
    ):
        coordinates = {
            'ax': 20,
            'ay': 500,
            'bx': 600,
            'by': 700,
        }

        properties_response = mock.Mock()
        properties_response.json = mock.Mock(
            return_value=properties.get('properties')
        )
        matched_properties = match_properties(properties_response, coordinates)
        assert len(matched_properties.content['properties'])

    def test_should_not_return_properties_to_given_properties_list_and_coordinates(
        self, properties
    ):
        coordinates = {
            'ax': 0,
            'ay': 0,
            'bx': 0,
            'by': 0,
        }

        properties_response = mock.Mock()
        properties_response.json = mock.Mock(
            return_value=properties.get('properties')
        )
        matched_properties = match_properties(properties_response, coordinates)

        assert matched_properties.content == 'Nenhum imóvel encontrado'
        assert matched_properties.status_code == 404

    def test_should_return_propertie_for_given_valid_propertie_data(self):
        spotippos_property = {
            'squareMeters': 93,
            'description': "Occaecat excepteur officia excepteur sit. Qui magna amet fugiat laborum enim.",
            'title': "Imóvel multi provincia, com 4 quartos e 3 banheiros.",
            'baths': 3,
            'y': 700,
            'beds': 4,
            'x': 600,
            'price': 971000,
            'provinces': [
                "Gode",
                "Ruja",
            ]
        }
        valid_spotippos_property_schema = schema_validation(spotippos_property)
        assert valid_spotippos_property_schema == spotippos_property

    def test_should_return_errors_for_given_invalid_property_data(
        self,
        app,
        invalid_property
    ):
        expected_errors = [['Not a valid integer.'], ['Not a valid string.']]
        invalid_spotippos_property_schema = schema_validation(invalid_property)
        for error in expected_errors:
            assert error in invalid_spotippos_property_schema.content.values()
