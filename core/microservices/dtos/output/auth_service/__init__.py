from marshmallow import fields, post_load
from core.microservices import to_string
from core.microservices.dtos.output.error import ErrorSchema, ErrorDTO


class TokenResponseSchema(ErrorSchema):
    access_token = fields.String()
    id_token = fields.String()
    scope = fields.String()
    expires_in = fields.Int()
    token_type = fields.String()

    @post_load()
    def deserialize(self, data, **kwargs):
        return TokenResponseDTO(**data)


class TokenResponseDTO(ErrorDTO):

    def __init__(self, access_token=None,
                 id_token=None,
                 scope=None,
                 expires_in=None,
                 token_type=None,
                 error=None,
                 error_description=None,
                 **kwargs):
        super().__init__(error, error_description)
        self.access_token = access_token
        self.id_token = id_token
        self.scope = scope
        self.expires_in = expires_in
        self.token_type = token_type

    def __repr__(self):
        return to_string(TokenResponseSchema(), self)
