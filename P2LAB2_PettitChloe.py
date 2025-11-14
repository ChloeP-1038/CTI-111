# Chloe Pettit
# 11/14/2025
# P2LAB2
# Write code that uses a dictionary to store user input.

vehicle_mpg = {'Camaro': 18.21, 'Prius': 52.36, 'Model S': 110, 'Silverado': 26}
keys = vehicle_mpg.keys()
print(vehicle_mpg.keys())
chosen_vehicle = input("Enter a vehicle to see its mpg: ")
mpg = vehicle_mpg[chosen_vehicle]
print('The', chosen_vehicle, 'gets', mpg, 'mpg.')
miles = float(input('How many miles will you drive the', chosen_vehicle, '?'))
gallons = miles / mpg
print(f'{gallons:.2f}', 'gallons of gas are needed to drive the', chosen_vehicle, '.')
