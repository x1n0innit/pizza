import random

pizza_toppings = ['tomato', 'mozarella', 'sausage', 'tuna', 'pineapple', 'peporoni', 'bacon', 'ham', 'olives', 'mushrooms']

toppings_picked = []

def getTopping():
  i = random.randint(0, len(pizza_toppings) - 1)
  topping = pizza_toppings[i]
  if topping in toppings_picked:
    getTopping()
  else:
    toppings_picked.append(topping)
    print(topping)

for i in range(3):
  getTopping()
  #print(toppings_picked)
  