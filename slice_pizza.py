"""

Simple program to practice using .pop(), len(), .insert() .sort(), slicing using [], storing variables, etc.

"""


toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]

num_two_dollar_slices = prices.count(2)  # count how many $2 slices exist
print(num_two_dollar_slices)

num_pizzas = len(toppings)  # how many differenet types of toppings sold
print("We sell", num_pizzas, "different kinds of pizza!")  # inform customer how many pizzas are sold

pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"],
                    [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]

pizza_and_prices.sort()  # sort prices of pizza in ascending order
print(pizza_and_prices)  # show sorted menu

cheapest_pizza = pizza_and_prices[0]
print("The cheapest Pizza is", cheapest_pizza)
priciest_pizza = pizza_and_prices[-1]
print("The priciest Pizza is", priciest_pizza)

# customer decides to buy most expensive Pizza, and thus we ran out
pizza_and_prices.pop()  # remove last pizza

# we made another pizza with peppers for $2.5, let's add it to the list
pizza_and_prices.insert(4, [2.5, "peppers"])

print(pizza_and_prices)  # new menu

# we sold the 3 cheapest pizzas
three_cheapest = pizza_and_prices[:3]
print(three_cheapest)
