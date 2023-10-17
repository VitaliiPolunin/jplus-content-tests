import json
from abc import ABC, abstractmethod
from typing import TypeVar

from faker import Faker
from marshmallow import Schema, post_dump


faker = Faker()


class SerializableDTO(ABC):
    T = TypeVar('T')

    @abstractmethod
    def serialize(self, schema: T):
        return schema().dump(self)

    def to_string(self, json_obj):
        return json.dumps(json_obj, indent=4,
                          ensure_ascii=False)


class BaseSchema(Schema):
    SKIP_VALUES = {None}

    @post_dump
    def remove_skip_values(self, data, **kwargs):
        return {
            key: value
            for key, value in data.items()
            if value is not None
        }
