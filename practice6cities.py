cities = {
    'yantai':{
        'country':'china',
        'population':300,
        'fact':'next to ocean',
    },
    'seoul':{
        'country':'korea',
        'population':1000,
        'fact':'next to china',
    },
    'tokyo':{
        'country':'japan',
        'population':2000,
        'fact':'across to ocean',
    },
}
for city_name, city_message in cities.items():
    country = city_message['country']
    population = city_message['population']
    fact =city_message['fact']
    print(f"{city_name.title()} is in {country.title()}. It has {population} people,and it has a fact that it is {fact}.")