# -*- encoding: utf-8 -*-

import json
import pytest

from flask import Flask
from app import create_app


@pytest.fixture
def app():
    app = create_app()
    return app
