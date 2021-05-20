from api.clients.base_client import BaseClient
from requests import Session
from typing import Dict
import config


class GistClient(BaseClient):

    session: Session
    base_url: str

    def __init__(self):
        self.session = Session()
        self.session.headers["accept"] = "application/vnd.github.v3+json"
        self.session.headers["Authorization"] = f"token {config.GITHUB_TOKEN}"
        self.base_url = config.API_URL

    def get_all_gists_for_user(self, username: str):
        endpoint: str = f"{self.base_url}/users/{username}/gists"
        req = self.session.get(endpoint)
        return self.get_response(req, 200)

    def get_gist_with_id(self, gist_id: str):
        endpoint: str = f"{self.base_url}/gists/{gist_id}"
        req = self.session.get(endpoint)
        return self.get_response(req, 200)

    def create_gist(self, description: str, files: Dict):
        endpoint: str = f"{self.base_url}/gists"
        body_params: Dict = {
            "description": description,
            "files": files,
            "public": False
        }
        req = self.session.post(endpoint, json=body_params)
        return self.get_response(req, 201)

    def update_gist(self, gist_id: str, description: str, files: Dict):
        endpoint: str = f"{self.base_url}/gists/{gist_id}"
        body_params: Dict = {
            "description": description,
            "files": files,
            "public": False
        }
        req = self.session.patch(endpoint, json=body_params)
        return self.get_response(req, 200)

    def delete_gist(self, gist_id: str):
        endpoint: str = f"{self.base_url}/gists/{gist_id}"
        req = self.session.delete(endpoint)
        return self.get_response(req, 204)
