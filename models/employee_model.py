import json

class User():
    def __init__(self, id, username):
        self.__id = id
        self.__username = username

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

class UserModelForClient(UserModel):
    def __init__(self, file_name, username, password):
        super().__init__(file_name)
        self.__username = username
        self.__password = password
        self.__current_user_id = None
        self._set_current_user_id()

    @property
    def current_user_id(self):
        return self.__current_user_id

    def _set_current_user_id(self):
        for id, user_object in self.user_list['user_list'].items():
            if self.__username == user_object['username'] and self.__password == user_object['password']:
                self.__current_user_id = id
                break