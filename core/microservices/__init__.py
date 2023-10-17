import json
from typing import TypeVar

T1 = TypeVar('T1')
T2 = TypeVar('T2')


def to_string(schema: T1, dto: T2):
    return json.dumps(schema.dumps(dto), indent=4,
                      ensure_ascii=False)


def to_string_dict(dto):
    return json.dumps(dto.__dict__,
                      indent=4,
                      ensure_ascii=False)
