from marshmallow import fields
from core.microservices.dtos.input import SerializableDTO, BaseSchema
from core.util.configManager import config


class TokenSchema(BaseSchema):
    client_id = fields.Str(required=True)
    grant_type = fields.Str(required=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True)
    realm = fields.Str(required=True)
    scope = fields.Str(required=True)


class TokenDTO(SerializableDTO):
    def __init__(self, client_id=None,
                 grant_type=None,
                 username=None,
                 password=None,
                 realm=None,
                 scope=None):
        self.client_id = client_id
        self.grant_type = grant_type
        self.username = username
        self.password = password
        self.realm = realm
        self.scope = scope

    def simpleToken(self):
        return TokenDTO(client_id=config.AUTH_CLIENT_ID,
                        grant_type=config.AUTH_GRANT_TYPE,
                        username=config.AUTH_USERNAME,
                        password=config.AUTH_PASSWORD,
                        realm=config.AUTH_REALM,
                        scope=config.AUTH_SCOPE)

    def with_userNameAndPassword(self, username, password):
        self.username = username
        self.password = password
        return self

    def serialize(self, obj=TokenSchema):
        return super().serialize(obj)

    def __repr__(self):
        return super().to_string(self.serialize())
