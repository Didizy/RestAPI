import requests
import json


class Client:
    def __init__(self):
        self.session = requests.Session()
        self.base_url = "http://127.0.0.1:8000/api/"

    def register(self, username, password):
        url = f"{self.base_url}register/"

        data = {
            "username": username,
            "password": password
        }

        requests.post(url, data=data)

    def login(self, username, password):
        url = f"{self.base_url}login/"

        data = {
            "username": username,
            "password": password
        }

        r = self.session.post(url, data=data)
        print(self.session.cookies)
        # print(r.json())
        return r.json()['token']

    def add_task(self, username, token, task_title):
        url = f"{self.base_url}todo/"
        data = {
            "user": username,
            "title": task_title,
            "completion": False
        }

        headers = {'Content-Type': "application/json", "Accept": "*/*", "Authorization": "Bearer " + token}

        self.session.post(url, data=json.dumps(data), headers=headers)

    def task_list(self, username, token):
        url = f"{self.base_url}todo/"

        data = {
            "user": username
        }
        headers = {'Content-Type': "application/json", "Accept": "*/*", "Authorization": "Bearer " + token}
        self.session.get(url, data=json.dumps(data), headers=headers)

    def update_task(self, token, new_title, task_id):
        url = f"{self.base_url}todo/{task_id}"

        data = {
            "title": new_title
        }

        headers = {'Content-Type': "application/json", "Accept": "*/*", "Authorization": "Bearer " + token}
        self.session.put(url, data=json.dumps(data), headers=headers)

    def delete_task(self, token, task_id):
        url = f"{self.base_url}todo/{task_id}"

        headers = {'Content-Type': "application/json", "Accept": "*/*", "Authorization": "Bearer " + token}
        self.session.delete(url, headers=headers)


client = Client()
auth = client.login("test1", "aaa")
# client.add_task("test1", auth, "task_test")
# client.delete_task(auth, "10")
client.update_task(auth, "new_task", "9")
# client.task_list("test1", auth)
