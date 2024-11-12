# Ruby Solis-Chavez, Anabel Perez
total = 0
tip = 0.15
people_at_table = int(input("Enter the # of people at the table: "))

for person in range(1, people_at_table + 1):
    meal_cost = float(input("Enter the price of your meal: "))
    total += meal_cost

cost_all = total + (total * tip)
cost_per_person = cost_all/people_at_table
print(f'The amount owned by each person is ${round(cost_per_person, 2)}.')

