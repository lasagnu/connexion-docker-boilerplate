import pytest

class TestHealthCheck:
    def test_healthcheck(self, flask_client):
        self.given_api_client(flask_client)
        self.when_healthcheck_is_requested()
        self.then_status_code_200_is_returned()
        self.then_ok_message_is_returned()

    def given_api_client(self, api_client):
        self.api_client = api_client

    def when_healthcheck_is_requested(self):
        healthcheck_url = '/api/v1/healthcheck'
        self.response = self.api_client.get(healthcheck_url)

    def then_status_code_200_is_returned(self):
        assert self.response.status_code == 200

    def then_ok_message_is_returned(self):
        assert self.response.json == {"message": "ok"}
