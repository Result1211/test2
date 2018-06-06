class User(object):

    def __init__(self, user_email=None, user_password=None):
        self.user_email = user_email
        self.user_password = user_password

    @classmethod
    def Admin(cls):
        return cls(user_email="test10@test.ru", user_password="tester10")

    # @classmethod
    # def random(cls):
    #     from random import randint
    #     return cls(user_email="user"+str(randint(1, 10))+"@test.ru",
    #                user_password="pass"+str(randint(1, 10)))