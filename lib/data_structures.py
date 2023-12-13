spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [food.get("name") for food in spicy_foods]

# names = get_names(spicy_foods)
# print(names)

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"] > 5]
       
def print_spicy_foods(spicy_foods):
    spicy = []
    for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = food["heat_level"]
        emoji = "🌶" * heat_level
        spicy.append(f"{name} ({cuisine}) | Heat Level: {emoji}")

    for item in spicy:
        print(item)
print_spicy_foods(spicy_foods)

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food 
    return None 
result_american = get_spicy_food_by_cuisine(spicy_foods, "American")
print(result_american)      


def print_spiciest_foods(spicy_foods):
    spiciest = []
    for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = food["heat_level"]
        emoji = "🌶" * heat_level
        if heat_level > 5:
            spiciest.append(f"{name} ({cuisine}) | Heat Level: {emoji}")

    for item in spiciest:
        print(item)
print_spiciest_foods(spicy_foods)

def get_average_heat_level(spicy_foods):
    heat_levels=[]
    for food in spicy_foods:
        heat_level = food["heat_level"]
        heat_levels.append(heat_level)
    # print(heat_levels)
    avg = sum(heat_levels)/len(heat_levels)
    return avg
average = get_average_heat_level(spicy_foods)
print(average)


def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
