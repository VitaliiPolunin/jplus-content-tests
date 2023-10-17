import json
import logging

import allure
import curlify
import requests
from allure import attachment_type as at
from assertpy import assert_that, soft_assertions
from requests.adapters import HTTPAdapter
from urllib3 import Retry

from core.services.rest_api.restMethods import RestMethods
from core.util.configManager import config


class RestImplementation:
    logger = logging.getLogger(__name__)

    def __init__(self, base_address, headers=None):
        self.base_address = base_address
        self.headers = headers

    def executeRequest(self, method: RestMethods, path="/", params=None, data=None, json_body=None,
                       headers=None, expected_status_code=None):
        # Prepare base url
        url = f"{self.base_address}/{path}"

        session = self.getHttpSession()

        with allure.step(f'{method.value} request to: {url}'):
            # Prepare headers
            request_headers = self.headers if headers is None else headers
            self.logger.info(f'{method.value} request to: {url}')
            # Execute request according to REST method
            if method.name == RestMethods.GET.name:
                response = session.get(url=url, params=params, headers=request_headers)
            elif method.name == RestMethods.POST.name:
                response = session.post(url=url, params=params, data=data, json=json_body, headers=request_headers)
            elif method.name == RestMethods.PUT.name:
                response = session.put(url=url, params=params, data=data, json=json_body, headers=request_headers)
            elif method.name == RestMethods.PATCH.name:
                response = session.patch(url=url, params=params, data=data, json=json_body, headers=request_headers)
            else:
                raise NameError(f'No option specified for executeRequest method with method: {method.value}')
            return self.attach_allure_logs(response, expected_status_code)

    def attach_allure_logs(self, response, expected_status_code: int):
        with allure.step(f'Status code: {response.status_code}'):
            self.logger.debug(f'Curl: {curlify.to_curl(response.request)}')
            self.logger.info(f'Status code is: {response.status_code}')
            allure.attach(curlify.to_curl(response.request), "Request")
            # Catch error when response couldn't be parsed as JSON for allure
            if bool(response.text):
                pretty_resp = response.json() \
                    if response.headers.get('content-type') == 'application/json' \
                    else response.text
                allure.attach(json.dumps(pretty_resp), "Response body", attachment_type=at.JSON)
            else:
                pretty_resp = response.__str__()
                allure.attach(pretty_resp, "Response body")

            self.logger.debug(f'Response body: {pretty_resp}')

            # Assert status code
            with soft_assertions():
                assert_that(response.status_code).described_as("Status code").is_equal_to(expected_status_code)
                assert_that(response.elapsed.microseconds).described_as(
                    f'Response time is: {response.elapsed}.') \
                    .is_less_than(config.REST_TIMEOUT_MS * 1000)

            return response

    def getHttpSession(self):
        session = requests.Session()
        retry = Retry(connect=3, backoff_factor=0.5)
        adapter = HTTPAdapter(max_retries=retry)
        session.mount('http://', adapter)
        session.mount('https://', adapter)
        return session
