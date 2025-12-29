favorite_places = {
    'shi':['guilin','beijing','weihai','yantai'],
    'zhang':['beijing','yantai'],
    'meng':['laishan'],
}

for personal_name, personal_place in favorite_places.items():
    if len(personal_place) == 1:
        print(f"{personal_name.title()} favorite places is:")
        print(f"\t{personal_place[0]}")
    else:
        print(f"{personal_name.title()} favorite places are:")
        for every_place in personal_place:
                print(f"\t{every_place}")