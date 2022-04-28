favourite_languages = {
    'janek': 'python',
    'sara': 'c',
    'edward': 'ruby',
    'pawel': 'python',
    }

friends = ['pawel', 'sara']

for name in favourite_languages.keys():
    print(f"Witaj {name.title()}!")
    if name in friends:
        language = favourite_languages[name].title()
        print(f"Witaj {name.title()}! Widze, ze Twoj ulubiony jezyk to: {language}")