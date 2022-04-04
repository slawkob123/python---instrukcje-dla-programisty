
# Make a list of users

current_users = ['s³aWek', 'Dawid', 'andrzej', 'micha³', 'piotrek']

new_users = ['marek', 'S³awek', 'karolina']

for user in current_users:
    current_users_copy = user.lower()
    print(current_users_copy)

for users in new_users:
    if users == current_users_copy:
        print(f"Podana nazwa -{users} ju¿ istnieje. Wybierz inn¹")
    else:
        print(f"Nazwa prawid³owa - {users}")