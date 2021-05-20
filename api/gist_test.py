from api.clients.gist_client import GistClient
from typing import Dict, List
import config


def test_create_gist(gist_client: GistClient):
    username: str = config.GITHUB_USERNAME
    files: Dict = {"myFile.txt": {"content": "This is a test gist"}}
    description: str = "Testing Gist Creation API"

    gist_client.create_gist(description, files)
    all_gists: List[Dict] = gist_client.get_all_gists_for_user(username)
    verify_gist_in_list(all_gists, description)


def test_update_gist(gist_client: GistClient):
    files: Dict = {
        "myFile1.txt": {"content": "This file will be updated"},
        "myFile2.txt": {"content": "This file will be deleted"}
    }
    description: str = "Testing Gist Update API"

    created_gist: Dict = gist_client.create_gist(description, files)
    gist_id: str = created_gist["id"]
    gist: Dict = gist_client.get_gist_with_id(gist_id)
    verify_gist_files(gist, files)

    files = {
        "myFile1.txt": {"content": "Text successfully updated"},
        "myFile2.txt": {"content": ""}
    }
    gist_client.update_gist(gist_id, description, files)

    gist = gist_client.get_gist_with_id(gist_id)
    verify_gist_files(gist, files)


def test_delete_gist(gist_client: GistClient):
    username: str = config.GITHUB_USERNAME
    files: Dict = {"myFile3.txt": {"content": "This gist will be deleted"}}
    description: str = "Testing Gist Deletion API"

    created_gist: Dict = gist_client.create_gist(description, files)
    all_gists: List[Dict] = gist_client.get_all_gists_for_user(username)
    verify_gist_in_list(all_gists, description)

    gist_id: str = created_gist["id"]
    gist_client.delete_gist(gist_id)

    all_gists: List[Dict] = gist_client.get_all_gists_for_user(username)
    verify_gist_not_in_list(all_gists, description)


def verify_gist_in_list(gist_list: List[Dict], exp_gist_description: str):
    gist_descriptions: List[str] = [gist["description"] for gist in gist_list]
    assert exp_gist_description in gist_descriptions


def verify_gist_not_in_list(gist_list: List[Dict], exp_gist_description: str):
    gist_descriptions: List[str] = [gist["description"] for gist in gist_list]
    assert exp_gist_description not in gist_descriptions


def verify_gist_files(gist: Dict, exp_files: Dict):
    exp_num_files = len([file for file in exp_files.values() if file["content"] != ""])
    assert exp_num_files == len(gist["files"])
    for file_name, file_content in exp_files.items():
        if file_content["content"] == "":
            assert file_name not in gist["files"]
        else:
            assert file_name in gist["files"]
            assert file_content["content"] == gist["files"][file_name]["content"]
