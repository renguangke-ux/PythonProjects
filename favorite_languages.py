favorite_languages = {
    "jen":["python","rust"],
    "sarah":["c"],
    "edward":["rust","go"],
    "phil":["python","haskell"],
}
for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languanges are")
    for languange in languages:
        print(f"\t{languange.title()}")