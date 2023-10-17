import logging
from core.util.configManager import config

from core.services.rest_api.restBase import ApiClient

auth_headers = {
    'Content-Type': 'application/json'
}


class ApiBase:
    logger = logging.getLogger(__name__)

    # Init ApiBase class. By default api client is set from request. \
    # It could be configured for locust execution
    def __init__(self,
                 apiClient=ApiClient(
                     base_address=config.AUTH_URL,
                     headers=auth_headers)):
        self.apiClient = apiClient

    def spec(self):
        return self.apiClient
