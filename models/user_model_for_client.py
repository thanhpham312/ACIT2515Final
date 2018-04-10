from models.user_model import UserModel

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
