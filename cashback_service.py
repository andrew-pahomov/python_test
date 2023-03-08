class CashbackHackService:

    def __init__(self):
        self.__boundary = 1000

    def remain(self, amount):
        return self.__boundary - amount % self.__boundary