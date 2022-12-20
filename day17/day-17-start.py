class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username;
        self.followers = 0; # default value
        self.following = 0

    def follow(self, user): # method always need a self parameter
        user.followers += 1
        self.following += 1

user_1 = User("001", "angela") # this is way more organize than the one below
user_2 = User("002", "jack")

print(user_1.username)
print(user_1.followers)

#user_1 = User()
#user_1.id = '001'
#user_1.username = 'angela'

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)