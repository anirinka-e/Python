import json

my_file = open("final_project/test_data.json")

global_data = json.load(my_file)

class DataProvider:

    def __init__(self) -> None:
        self.data = global_data

    def get_date(self, prop: str) -> dict:
        return self.data.get(prop)

    def get_date_str(self, prop: str) -> str:
        return self.data.get(prop)

    def get_token(self) -> str:
        return self.data.get("token_global")

    def get_body_events(self) -> dict:
        return self.data.get("body_events")

    def get_body_date(self) -> dict:
        return self.data.get("body_date")