from requests import Response


class BaseClient:

    @staticmethod
    def get_response(response: Response, exp_status_code: int):
        assert exp_status_code == response.status_code
        if response.status_code == 204:
            return None
        else:
            return response.json()
