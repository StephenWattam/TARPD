
import json
import requests


class OSFClient:

    BASE_URL = "https://api.test.osf.io/v2/"

    def __init__(self, token: str) -> None:
        self.token = token

    def get_user(self) -> dict:
        return self.get(f"users/me")

    def get_collection(self, collection_id) -> dict:
        return self.get(f"collections/{collection_id}")

    def get(self, endpoint) -> dict:
        print(f"Retrieving {OSFClient.BASE_URL}{endpoint}   ///    {self.token}")
        r = requests.get(f"{OSFClient.BASE_URL}{endpoint}", headers={"Authorization": f"Bearer {self.token}"})
        r.raise_for_status()
        return json.loads(r.text)