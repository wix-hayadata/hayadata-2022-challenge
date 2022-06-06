[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/)
# Wix hayaData challenge 2022

challenge.py is a script that will add recipes to a recipe system, developed for the new restaurants @ Wix new campus.

The script will also place an order containing all of the ingredients from the recipes.

:bug: **There are 5 bugs in the code** - your mission as a seasoned pythonista is to fix them. (Hint: a bug can be a missing piece of code).

After fixing the code, this is the expected output when running the script:

    Registered create_tahini_recipe successfully
    Registered create_salad_recipe successfully
    Registered create_rice_recipe successfully
    Registered create_soup_recipe successfully
    Ordering ['Coriander', 'Lemon', 'Pepper', 'Salt', 'cucumber: Medium', 'tomato: Small']

Important Notes:
 1. The list of ingredients should be unique (e.g. "Salt" will appear only once) and sorted alphabetically.
 2. If the default ingredients (e.g. "Tap Water") for the recipe are used - no need to have them in the order,
 they're already in the kitchen :)
 3. keep the __main__ part in the code as it is
