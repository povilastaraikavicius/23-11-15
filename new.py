# Let user enter name, surname and age. Print if user is allowed to enter an online casino or not. 21 is the age cap.

# user_name_list = []
# user_surname_list = []
# user_age_list = []

user_name = input("enter your name:")
user_surname = input("enter your surname:")
user_age = int(input("enter your age:"))

# user_name_list.append(f"user name:{user_name}")
# user_surname_list.append(f"user surname:{user_surname}")
# user_age_list.append(f"user age:{user_age}")

if user_age >= 25:
    print(f"Welcome!{user_name} ")
else:
    print("You are too young.")
# Create a database (list of privileged users), print a specific message with a
# personal greeting if the user is a privileged and just "Welcome otherwise"

privilege_users = ["Povilas", "Andrius"]

if user_name in privilege_users:
    print("Welcome otherwise")
else:
    print("welcome")
