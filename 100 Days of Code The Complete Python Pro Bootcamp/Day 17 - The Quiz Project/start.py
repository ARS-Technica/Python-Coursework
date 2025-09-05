class User:
    def __init__(self):
        print("New user being created...")

user_1 = User()
user_1.id = "001"
user_1.username = "John"

print(user_1.username)  # Returns "John"

user_2 = User()
user_2.id = "002"
user_2.username = "Jack"

print(user_2.username)  # Returns "Jack"


#%%

class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username

user_1 = User("001", "John")
print(user_1.username)  # Returns "John"

user_2 = User()     # TypeError: __init__() missing 2 required positional arguments: 'user_id' and 'username'
user_2.id = "002"
user_2.username = "Jack"
