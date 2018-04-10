import json
from models.data.user import User

class UserModel():
    def __init__(self, file_name):
        self.__user_list = {}
        self.__file_name = file_name
        self._load_from_file(file_name)

    @property
    def user_list(self):
        return self.__user_list

    def _load_from_file(self, file_name):
        with open(file_name, 'r') as f:
            self.__user_list = json.load(f)

    def _save_to_file(self, file_name):
        with open(file_name, 'w') as f:
            json.dump(self.__user_list, f, indent=4)