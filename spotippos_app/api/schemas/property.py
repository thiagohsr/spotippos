# -*- utf-8 -*-
from api.constants import (
    MAX_BATHS,
    MIN_BATHS,
    MAX_BEDS,
    MIN_BEDS,
    MAX_SQUARE_METERS,
    MIN_SQUARE_METERS,
    MAX_LONGITUDE,
    MIN_LONGITUDE,
    MAX_LATITUDE,
    MIN_LATITUDE,
)

from marshmallow import (
    fields,
    Schema,
    validates,
    ValidationError
)


class PropertySchema(Schema):
    baths = fields.Integer(required=True)
    beds = fields.Integer(required=True)
    description = fields.String(required=True)
    price = fields.Integer(required=True)
    provinces = fields.List(fields.String())
    squareMeters = fields.Integer(required=True)
    title = fields.String(required=True)
    x = fields.Integer(required=True)
    y = fields.Integer(required=True)

    @validates('baths')
    def validate_baths(self, value):
        if value < MIN_BATHS:
            raise ValidationError(
                'Baths quantity must be greater than or equal to'
                ' {min_baths}.'.format(
                    min_baths=MIN_BATHS
                )
            )
        if value > MAX_BATHS:
            raise ValidationError(
                'Baths quantity must not be greater than or equal to'
                ' {max_baths}.'.format(
                    max_baths=MAX_BATHS
                )
            )

    @validates('beds')
    def validate_beds(self, value):
        if value < MIN_BEDS:
            raise ValidationError(
                'Beds quantity must be greater than or equal to'
                ' {min_beds}.'.format(
                    min_beds=MIN_BEDS
                )
            )
        if value > MAX_BEDS:
            raise ValidationError(
                'Beds quantity must not be greater than or equal to'
                ' {max_beds}.'.format(
                    max_beds=MAX_BEDS
                )
            )

    @validates('squareMeters')
    def validate_squareMeters(self, value):
        if value < MIN_SQUARE_METERS:
            raise ValidationError(
                'Propertie area must be greater than or equal to '
                '{min_square_meters} square meters.'.format(
                    min_square_meters=MIN_SQUARE_METERS
                )
            )
        if value > MAX_SQUARE_METERS:
            raise ValidationError(
                'Propertie area must be equal to or minor than'
                ' {max_square_meters}.'.format(
                    max_square_meters=MAX_SQUARE_METERS
                )
            )

    @validates('x')
    def validate_x(self, value):
        if value < MIN_LONGITUDE:
            raise ValidationError(
                'Longitude must be greater than or equal to '
                '{min_longitude}.'.format(min_longitude=MIN_LONGITUDE)
            )
        if value > MAX_LONGITUDE:
            raise ValidationError(
                'Longitude must not be greater than or equal to '
                '{max_longitude}.'.format(max_longitude=MAX_LONGITUDE)
            )

    @validates('y')
    def validate_y(self, value):
        if value < MIN_LATITUDE:
            raise ValidationError(
                'Latitude must be greater than or equal to '
                '{min_latitude}.'.format(
                    min_latitude=MIN_LATITUDE
                )
            )
        if value > MAX_LATITUDE:
            raise ValidationError(
                'Latitude must not be greater than or equal to '
                '{max_latitude}.'.format(
                    max_latitude=MAX_LATITUDE
                )
            )
