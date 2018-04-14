class Transaction():
    '''
    Model for the transactions
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
