from marshmallow import Schema, fields, post_load
from core.microservices import to_string_dict


class ErrorSchema(Schema):
    error = fields.String()
    error_description = fields.String()

    @post_load
    def deserialize(self, data, **kwargs):
        return ErrorDTO(**data)


class ErrorDTO:

    def __init__(self, error, error_description):
        self.error = error
        self.error_description = error_description

    def with_error(self, error):
        self.error = error
        return self

    def with_error_description(self, error_description):
        self.error_description = error_description
        return self

    def __eq__(self, other):
        if not isinstance(other, ErrorDTO):
            return False
        return self.error == other.error \
            and self.error_description == other.error_description

    def __str__(self):
        return to_string_dict(self)
