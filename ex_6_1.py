class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password
    def set_password(self, new_password):
        self.__password = new_password
    def check_password(self, password):
        return self.__password == password
Anton = UserAccount('Anton', 'lololo@gmail.com', '333333333')
print(Anton.check_password('333333333'))
Anton.set_password('Tort')
print(Anton.check_password('333333333'))
print(Anton.check_password('Tort'))