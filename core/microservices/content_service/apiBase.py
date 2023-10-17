import logging

from core.microservices.auth_service.controllers.authController import AuthController
from core.util.configManager import config
from core.services.rest_api.restBase import ApiClient

content_headers = {
    'Content-Type': 'application/json',
    'Authorization': str(AuthController().getToken()),

}


class ApiBase:
    logger = logging.getLogger(__name__)

    # Init ApiBase class. By default api client is set from request. \
    # It could be configured for locust execution
    def __init__(self,
                 apiClient=ApiClient(
                     base_address=config.CONTENT_URI,
                     headers=content_headers)):
        self.apiClient = apiClient

    def spec(self):
        return self.apiClient

    def getAuthHeaders(self):
        res = content_headers.copy()
        return res
