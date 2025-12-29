mygirls_name = {
    'first_name':'meng',
    'last_name':'zhang',
    'age':35,
    'city':'muping',

}
print(mygirls_name)
print(mygirls_name['first_name'])
#some umber who loved
loved_number = {
    'wang':68,
    'ling':77,
    'sun':73,
    'fang':66,
    'ren':18,
}
print(loved_number)
#vacubulary
vac = {
    'ip':'intellectual Property',
    'wipo':'world intellectual property organization',
    'ipr':'intellectual property rights',
    'aippi':'association internationale pour la protection de la propriet intellectualle',
    'epo':'european patent office',
}
for key,value  in vac.items():
    print(f'{key.title()}:\n{value}\n')