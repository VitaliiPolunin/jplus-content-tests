from abc import ABC, abstractmethod


class IRest(ABC):

    @abstractmethod
    def get(self, path: str, params, headers, expected_status_code: int):
        pass

    @abstractmethod
    def post(self, path: str, params, data, json_body, headers, expected_status_code: int):
        pass

    @abstractmethod
    def put(self, path: str, params, headers, data, json_body, expected_status_code: int):
        pass

    @abstractmethod
    def patch(self, path: str, params, headers, data, json_body, expected_status_code: int):
        pass
