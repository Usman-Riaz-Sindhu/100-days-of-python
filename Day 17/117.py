class User:
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.user_name = user_name
        self.followers = 0
        self.following = 0
        # this will put the followers value to 0 by default when ever an object is created throught this class
    # pass
# it we want any function or class empty for while and they don't make any error we use "pass"
    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("001", "Usman Riaz")
user_2 = User("002", "Abdullah Akeel")
print(user_1.id, user_1.user_name)

user_1.follow(user_2)
print(user_1.following)
print(user_1.followers)
print(user_2.following)
print(user_2 .followers)