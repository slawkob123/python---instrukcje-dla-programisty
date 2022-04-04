user_names = ['admin', 'sławek', 'andrzej', 'piotrek', 'iza']

if user_names:
    for user in user_names:
        if user == 'admin':
            print("Witaj admin! Czy chcesz przejrzeć dzisiejszy raport?")
        else:
            print(f"Witaj, {user.title()}! Dziękujemy, że ponownie się zalogowałeś.")
else:
    print("Musimy znaleźć jakichś użytkowników!")