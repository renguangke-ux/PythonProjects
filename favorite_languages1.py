favorite_languages = {
    "jen":["python","rust"],
    "sarah":["c"],
    "edward":["rust","go"],
    "phil":["python","haskell"],
}
for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print(f"{name.title()}'s favorite languange is \n\t{languages[0]}")
    else:
        print(f"\n{name.title()}'s favorite languanges are")
        for languange in languages:
            print(f"\t{languange.title()}")