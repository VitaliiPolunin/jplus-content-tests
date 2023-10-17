from marshmallow import Schema, fields, post_load

from core.microservices import to_string


class MetaDataSchema(Schema):
    batchesCount = fields.Int()
    jobsCount = fields.Int()
    modelsCount = fields.Int()
    filesCount = fields.Int()

    @post_load
    def deserialize(self, data, **kwargs):
        return MetaDataDTO(**data)


class MetaDataDTO:

    def __init__(self, batchesCount=None, jobsCount=None, modelsCount=None,
                 filesCount=None):
        self.batchesCount = batchesCount
        self.jobsCount = jobsCount
        self.modelsCount = modelsCount
        self.filesCount = filesCount

    def __str__(self):
        return to_string(MetaDataSchema, self)
