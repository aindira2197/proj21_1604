class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self, u, p):
        return self.username == u and self.password == p

u = User("admin", "1234")
print(u.login("admin", "1234"))
