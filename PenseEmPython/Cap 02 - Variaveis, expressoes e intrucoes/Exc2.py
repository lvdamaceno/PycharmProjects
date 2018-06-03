price = 24.95
amount = 60.00
ship = 3


unit_cost = (price - (price * 40)/100)
print("Unit cost: " + str(unit_cost))


fare = ship + ((amount-1)*0.75)
print("Ship fare: " + str(fare))


books_cost = unit_cost * amount
print("Books cost: " + str(books_cost))


final_cost = books_cost + fare

print(final_cost)

