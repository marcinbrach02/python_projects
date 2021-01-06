
class UserData:

    def __init__(self, nickname, password):
        self.__nickname = nickname
        self.__password = password

    @property                                   #oznaczenie w celu wywloania metody nickname
    def nickname(self):                         #metody sa zwyklymi zmiennymi
        return self.__nickname

    @nickname.setter                            #decorator
    def nickname(self, nickname):
        self.__nickname = nickname


u = UserData('test', 'sss')
u.nickname = 'ddd'
print(u.nickname)


print(type(u))
print(isinstance(u, UserData))






