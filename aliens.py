#creat a empty list for storing alien message
aliens = []
#creat 30 green alien message
for alien_number in range(30):
    new_alien = {'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)
#print the first five aliens
for alien in aliens[0:5]:
    print(alien)
print('......')
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
for alien in aliens[:5]:
    print(alien)
print("......")

for alien in aliens[:5]:
    if alien['color'] == 'green':
        alien['color'] = 'red'
        alien['points'] = 15
        alien['speed'] = 'fast'
for alien in aliens[:8]:
    print(alien)
print("......")
