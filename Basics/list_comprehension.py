temperatures = [220, 234, 178, 93]

dec_temperatures = [temperature /10 for temperature in temperatures]

print(dec_temperatures)

temps = [220, 234, 178, 93, -99999, 42]

new_temps = [temp / 10 for temp in temps if temp != -99999]
new_temps_subs =  [temp / 10 if temp != -99999 else 0 for temp in temps ]
print(new_temps)
print(new_temps_subs)

mix_list = [220, 'yes', 1, 93, '900', ' hello', 14]
new_list = [item for item in mix_list if isinstance(item, int)] 
print(new_list)