mygirls_name1 = {
    'first_name':'meng',
    'last_name':'zhang',
    'age':35,
    'city':'muping',
}
mygirls_name2 = {
    'first_name':'dong',
    'last_name':'zhang',
    'age':32,
    'city':'longkou',
}
mygirls_name3 = {
    'first_name':'chaodan',
    'last_name':'shi',
    'age':36,
    'city':'qingdao',
}
my_girls = [mygirls_name1,mygirls_name2,mygirls_name3]
for mygirl_name in my_girls:
    name = f"{mygirl_name['last_name']} {mygirl_name['first_name']}"
    age = mygirl_name['age']
    city = mygirl_name['city']
    print(f"my girl {name.title()} is {age} old,and live in {city.title()}")