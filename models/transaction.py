class Transaction():
    '''
        Model for a  transaction log

        Attributes:
            __account: the account the fees belong to
            __time: time of the transaction
            __type: type of the transaction
            __balance_before: the account balance before the transaction
            __balance_after: the account balance after the transaction
            __balance_before: status of the transaction
            __description: description of the transaction
        Methods:
            _to_dict: a dictionary version of the transaction class
    '''
    def __init__(self, account, time, type, balance_before, balance_after, status, description):
        self.__account = account
        self.__time = time
        self.__type = type
        self.__balance_before = balance_before
        self.__balance_after = balance_after
        self.__status = status
        self.__description = description

    @property
    def time(self):
        return self.__time

    @property
    def type(self):
        return self.__type

    @property
    def balance_before(self):
        return self.__balance_before

    @property
    def balance_after(self):
        return self.__balance_after

    @property
    def status(self):
        return self.__status

    @property
    def description(self):
        return self.__description

    def _to_dict(self):
        return {
          "time": str(self.__time),
          "type": self.__type,
          "balance_before": self.__balance_before,
          "balance_after": self.__balance_after,
          "status": self.__status,
          "description": self.__description
        }
