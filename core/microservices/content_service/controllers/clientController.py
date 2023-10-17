from allure_commons._allure import step
from core.microservices.content_service.apiBase import ApiBase
from core.microservices.content_service.controllers import AIContentApiEndpoints
from core.microservices.dtos.output.client import ClientSchema


class ClientController(ApiBase):
    @step('Get client info')
    def getClient(self, clientId, statusCode=200,
                  schema=ClientSchema()):
        headers = super().getAuthHeaders()
        response = super().spec().get(path=AIContentApiEndpoints.CLIENTS.getPath(clientId),
                                      expected_status_code=statusCode,
                                      headers=headers)
        return schema.load(response.json())
