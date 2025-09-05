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


#%%


class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0  # Default value

user_1 = User("001", "John")
user_2 = User("002", "Jack")

print(user_1.followers)  # Returns 0 (Default value)


#%%

class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0  # Default value
        self.following = 0  # Default value

    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("001", "John")
user_2 = User("002", "Jack")

user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
