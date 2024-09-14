# In function only one *args is allowed
# * should be the first one and then positional arguments can be given

def make_pizza(*toppings, base):
    print(toppings, base)


def make_pizza_2(*topping, base):
    print(base, topping)


make_pizza("mushroom", "tomato", "cheese", base="thin crust")
make_pizza_2("dasda", "dasda", "dasda", base="crust")