import inspect


class OrderIngredients:
    ingredients_list = []

    def __init__(self, recipe_function):
        self.recipe_function = recipe_function()

    def __call__(self, *args, **kwargs):
        self.prepare_ingredients_list(args, kwargs)
        return self.recipe_function(*args, **kwargs)

    def prepare_ingredients_list(self, args, kwargs):
        OrderIngredients.ingredients_list.append(args)
        OrderIngredients.ingredients_list.append([f"{key}: {value}" for key, value in kwargs.items()])
        OrderIngredients.ingredients_list = sorted(OrderIngredients.ingredients_list)

    def place_order(cls):
        return f"Ordering {cls.ingredients_list}"


def create_or_update_recipe(*ingredients):
    """ No need to modify this function """
    return "Mock recipe"


def report_success(func_name):
    print(f"Registered {func_name} successfully")


def create_tahini_recipe(*spices, tahini: str = "Har Bracha", water: str = "Tap Water"):
    basic_tahini = create_or_update_recipe(tahini, water)
    for spice in spices:
        create_or_update_recipe(basic_tahini, spice)
    report_success(inspect.stack()[0].function)


def create_salad_recipe(*vegetables, tomato: str = "Cherry Tomato", cucumber: str = "Large Cucumber"):
    basic_salad = create_or_update_recipe(tomato, cucumber)
    for vegetable in vegetables:
        create_or_update_recipe(basic_salad, vegetable)
    report_success(inspect.stack()[0].function)


def create_rice_recipe(*vegetables, rice: str = "short", water: str = "Tap Water"):
    basic_rice = create_or_update_recipe(rice, water)
    for vegetable in vegetables:
        create_or_update_recipe(basic_rice, vegetable)
    report_success(inspect.stack()[0].function)


def create_soup_recipe(*vegetables, noodles: str = "rice", water: str = "Tap Water"):
    basic_soup = create_or_update_recipe(noodles, water)
    for vegetable in vegetables:
        create_or_update_recipe(basic_soup, vegetable)
    report_success(inspect.stack()[0].function)


if __name__ == "__main__":
    """
    This script will add the recipes to a recipe system,
    And then place an order containing all of the ingredients from the recipe.
    There are 5 bugs in the code. your mission is to fix them. Hint: a bug can be a missing piece of code.
    After fixing the code, this is the expected output when running the script:
   
    Registered create_tahini_recipe successfully
    Registered create_salad_recipe successfully
    Registered create_rice_recipe successfully
    Registered create_soup_recipe successfully
    Ordering ['Coriander', 'Lemon', 'Pepper', 'Salt', 'cucumber: Medium', 'tomato: Small']
   
    Important Notes:
    1. The list of ingredients should be unique (e.g. "Salt" will appear only once) and sorted alphabetically.
    2. If the default ingredients (e.g. "Tap Water" for the rice recipe) for the recipe are used - no need to have them in the order,
    they're already in the kitchen :)
    3. Do not modify the code below this line, keep the __main__ part as it is
    """
    
    create_tahini_recipe("Lemon", "Salt", "Pepper")
    create_salad_recipe("Coriander", "Salt", tomato="Small", cucumber="Medium")
    create_rice_recipe()
    create_soup_recipe("carrot", "cabbage")
    output = OrderIngredients.place_order()
    print(output)
    assert output == "Ordering ['Coriander', 'Lemon', 'Pepper', 'Salt', 'cabbage', 'carrot', 'cucumber: Medium', " \
                     "'tomato: Small']"
    print("Success!")
