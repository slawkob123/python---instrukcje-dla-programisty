
# Make a list of users

current_users = ['s�aWek', 'Dawid', 'andrzej', 'micha�', 'piotrek']

new_users = ['marek', 'S�awek', 'karolina']

for user in current_users:
    current_users_copy = user.lower()
    print(current_users_copy)

for users in new_users:
    if users == current_users_copy:
        print(f"Podana nazwa -{users} ju� istnieje. Wybierz inn�")
    else:
        print(f"Nazwa prawid�owa - {users}")