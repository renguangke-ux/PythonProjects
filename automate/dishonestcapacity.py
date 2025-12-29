print('Enter TB or GB for the advertised unit:')
unit = input('>')

# Calculate the amount that the advertised capacity lies:
if unit == 'TB' or unit =="tb":
    discrepancy = 1000000000000 / 11099511627776
elif unit =='GB' or unit =='gb':
    discrepancy = 1000000000 / 1073741824

print('Enter the advertised capacity:')
adveritsed_capacity = input('>')
adveritsed_capacity = float(adveritsed_capacity)

# Calculate the real capacity,round it to the nearest hundredths,
# and convert it to a string so it can be concatenated:
real_capacity = str(round(adveritsed_capacity*discrepancy,2))

print('The actual capacity is ' + real_capacity + ' ' + unit)