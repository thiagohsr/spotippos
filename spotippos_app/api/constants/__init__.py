# -*- coding: utf-8 -*-
HEADER_JSON_CONTENT = {
    'Content-type': 'application/json', 'Accept': 'text/plain'
}

SUCCESS_MESSAGES = {
    201: "Created Propertie: {title} in {provinces} province(s)",
}

ERROR_MESSAGES = {
    422: {
        'message': "Please, verify data for register this propertie"
    },
    404: {
        'message': "Provide an valid ID to retrive the queried propertie."
    },
}

MIN_BEDS = 1
MAX_BEDS = 5

MIN_BATHS = 1
MAX_BATHS = 5

MIN_SQUARE_METERS = 20
MAX_SQUARE_METERS = MIN_SQUARE_METERS * 12

MIN_LONGITUDE = 0
MAX_LONGITUDE = 1400

MIN_LATITUDE = 0
MAX_LATITUDE = 1000

PROVINCES = {
    'Gode': {
        'boundaries': {
            'upperLeft': {
                'x': 0,
                'y': 1000,
            },
            'bottomRight': {
                'x': 600,
                'y': 500,
            },
        }
    },
    'Ruja': {
        'boundaries': {
            'upperLeft': {
                'x': 400,
                'y': 1000,
            },
            'bottomRight': {
                'x': 1100,
                'y': 500,
            },
        }
    },
    'Jaby': {
        'boundaries': {
            'upperLeft': {
                'x': 1100,
                'y': 1000,
            },
            'bottomRight': {
                'x': 1400,
                'y': 500,
            },
        }
    },
    'Scavy': {
        'boundaries': {
            'upperLeft': {
                'x': 0,
                'y': 500,
            },
            'bottomRight': {
                'x': 600,
                'y': 0,
            },
        }
    },
    'Groola': {
        'boundaries': {
            'upperLeft': {
                'x': 600,
                'y': 500,
            },
            'bottomRight': {
                'x': 800,
                'y': 0,
            },
        }
    },
    'Nova': {
        'boundaries': {
            'upperLeft': {
                'x': 800,
                'y': 500,
            },
            'bottomRight': {
                'x': 1400,
                'y': 0,
            },
        }
    }
}
