from core.services.rest_api import RestImplementation, RestMethods
from core.services.rest_api.restInterface import IRest


class ApiClient(RestImplementation, IRest):

    def __init__(self, base_address, headers=None):
        super(ApiClient, self).__init__(base_address, headers)

    def get(self, path="/", params=None, headers=None, expected_status_code=200):
        return super().executeRequest(method=RestMethods.GET,
                                      path=path,
                                      params=params,
                                      headers=headers,
                                      expected_status_code=expected_status_code)

    def post(self, path="/", params=None, data=None, json_body=None,
             headers=None, expected_status_code=200):
        return super().executeRequest(method=RestMethods.POST,
                                      data=data,
                                      json_body=json_body,
                                      path=path,
                                      params=params,
                                      headers=headers,
                                      expected_status_code=expected_status_code)

    def put(self, path="/", params=None, headers=None, data=None, json_body=None, expected_status_code=200):
        return super().executeRequest(method=RestMethods.PUT,
                                      data=data,
                                      json_body=json_body,
                                      path=path,
                                      params=params,
                                      headers=headers,
                                      expected_status_code=expected_status_code)

    def patch(self, path="/", params=None, headers=None, data=None, json_body=None, expected_status_code=200):
        return super().executeRequest(method=RestMethods.PATCH,
                                      data=data,
                                      json_body=json_body,
                                      path=path,
                                      params=params,
                                      headers=headers,
                                      expected_status_code=expected_status_code)
