from allure_commons._allure import step
from core.microservices.auth_service import AuthApiEndpoints
from core.microservices.dtos.output.auth_service import TokenResponseSchema
from core.microservices.auth_service.apiBase import ApiBase
from core.microservices.dtos.input.auth_service import TokenDTO
from core.util.singleton import singleton


@singleton
class AuthController(ApiBase):
    _token = None

    def __init__(self):
        super().__init__()
        if self._token is None:
            self._token = self._getToken(TokenDTO().simpleToken())

    @step('Get token from 0uth')
    def _getToken(self, input_model: TokenDTO,
                  expected_status_code=200,
                  schema=TokenResponseSchema()):
        self.logger.info("Get token from 0uth")
        response = super().spec().post(path=AuthApiEndpoints.TOKEN.getPath(),
                                       json_body=input_model.serialize(),
                                       expected_status_code=expected_status_code)
        return response.json()['token_type'] + ' ' + response.json()['id_token']

    def getToken(self):
        return self._token
