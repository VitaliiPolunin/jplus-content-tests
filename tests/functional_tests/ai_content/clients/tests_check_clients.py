import allure
from core.microservices.content_service.controllers.clientController import ClientController


@allure.epic("Clients API check")
@allure.story("Clients CRUD operations check")
class TestCheckClients:
    def test_client_test(self):
        clientInfo = ClientController().getClient(clientId="01HAPJ9MV89N2JAMFH7VSHMNFD")

