n1 = int(input()) ; n2 = int(input())
print(n1 + n2)
print(n1 + n2/2)
d1 = d2 = 0
#print(n1/d1)
#n1 * n2 = d1
print(d1)


#programming assignment

user_input = input("Please enter the cost of your meal: ") # enter like $100
meal_cost = int(user_input[1:])

tip_rate = .18
tax_rate = .09

tip_cost = meal_cost * tip_rate
tax_cost = meal_cost * tax_rate
total_cost = meal_cost + tip_cost + tax_cost

print(f"Subtotal: ${meal_cost:>7.2f}\n     Tip: ${tip_cost:>7.2f}\n     Tax: ${tax_cost:>7.2f}\n   Total: ${total_cost:7.2f}")
