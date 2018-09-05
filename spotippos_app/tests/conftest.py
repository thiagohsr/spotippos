# -*- encoding: utf-8 -*-

import json
import pytest

from flask import Flask
from app import create_app


@pytest.fixture
def app():
    app = create_app()
    return app


@pytest.fixture
def invalid_propertie():
    return {
        'beds': 'quatro',
        'price': 'novecentos e sententa e um mil',
        'baths': 'tres',
        'title': 1234,
        'description': 971000,
        'y': 'numero_quarenta',
        'x': 'cento_e_onze',
        'squareMeters': 'noventa_e_tres',
    }


@pytest.fixture
def properties():
    return {
        "totalProperties": 3,
        "properties": [
            {
                "y": 505,
                "description": "Coordenadas numericas sem headers.",
                "price": 450000,
                "id": 3,
                "squareMeters": 110,
                "title": "Apezao da horona, com 3 quartos e 1 banheiro",
                "beds": 3,
                "x": 570,
                "provinces": [
                    "Ruja",
                    "Gode"
                ],
                "baths": 1
            },
            {
                "price": 971000,
                "y": 700,
                "squareMeters": 93,
                "id": 12,
                "description": "Occaecat excepteur officia excepteur sit. Qui magna amet fugiat laborum enim.",
                "title": "Im\u00f3vel multi provincia, com 4 quartos e 3 banheiros.",
                "beds": 4,
                "x": 600,
                "provinces": [
                    "Gode",
                    "Ruja"
                ],
                "baths": 3
            },
            {
                "y": 700,
                "price": 971000,
                "description": "Occaecat excepteur officia excepteur sit. Qui magna amet fugiat laborum enim.",
                "x": 600,
                "id": 19,
                "squareMeters": 93,
                "title": "Im\u00f3vel multi provincia, com 4 quartos e 3 banheiros.",
                "beds": 4,
                "provinces": [
                    "Gode",
                    "Ruja"
                ],
                "baths": 3
            }
        ]
    }
