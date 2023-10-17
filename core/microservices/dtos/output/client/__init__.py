from marshmallow import fields, post_load

from core.microservices import to_string_dict
from core.microservices.dtos.input import BaseSchema
from core.microservices.dtos.output.client.metaData import MetaDataSchema


class ClientSchema(BaseSchema):
    id = fields.Str()
    name = fields.Str()
    slug = fields.Str()
    icon = fields.Str(required=False)
    models = fields.List(fields.Str())
    metadata = fields.Nested(MetaDataSchema)
    brands = fields.Str()

    @post_load()
    def deserialize(self, data, **kwargs):
        return ClientDTO(**data)


class ClientDTO:

    def __init__(self, id, name, slug, icon, models, metadata, brands):
        self.id = id
        self.name = name
        self.slug = slug
        self.icon = icon
        self.models = models
        self.metadata = metadata
        self.brands = brands

    def __repr__(self):
        return to_string_dict(self)
