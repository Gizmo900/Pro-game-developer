
"""Ask the user to input the following.
1) Distance to destination in kilometers (float)
2) Car's fuel efficiency in km per liter (float)
3) Price of the fuel per liter (float)
4)input the toll

Calculate:
1) Total fuel needed= distance / fuel efficiency
2) Total fuel cost= fuel needed x price per litter
3) Total trip cost= fuel cost + tall (if any)"""

distance = float(input("h=How far away is your destination (kM)?"))
print(distance)
efficiency = float(input("How many litres does your car take up per km e.g 4.5 litre per 100 km?"))
print(efficiency)
fuel_cost = float(input("How much did fuel cost per litre?"))
print(fuel_cost)
toll = float(input("Enter the toll cost (£)?"))

# Calculate
Total_fuel= distance/ efficiency
Total_fuel_cost = Total_fuel*fuel_cost
Total_cost = Total_fuel_cost+toll
print(toll)

print("\n---Trip Cost Summary---\n") # \n to start a new line

print(f"{Total_fuel:.2f}","litre")
print(f"{Total_fuel_cost:.2f}","fuel cost £")
print(f"{Total_cost:.2f}","total cost £")








