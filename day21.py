recipes = []
count_ingredients = {}
for line in open("data/day21.txt").read().splitlines():
    ingredients, allergens = line.split("(contains ")
    ingredients = set(ingredients.split())
    allergens = set(allergens[:-1].split(", "))
    recipes.append({"ingredients": ingredients, "allergens": allergens})
    for ingredient in ingredients:
        if ingredient in count_ingredients:
            count_ingredients[ingredient] += 1
        else:
            count_ingredients[ingredient] = 1

all_ingredients = set()
all_allergens = set()
for recipe in recipes:
    all_ingredients.update(recipe["ingredients"])
    all_allergens.update(recipe["allergens"])

maybe_ingredients = {allergen: set(all_ingredients) for allergen in all_allergens}
for recipe in recipes:
    other_ingredients = all_ingredients.difference(recipe["ingredients"])
    for allergen in recipe["allergens"]:
        for ingredient in other_ingredients:
            maybe_ingredients[allergen].discard(ingredient)
maybe_ingredients_all = set()
for allergen in maybe_ingredients:
    maybe_ingredients_all.update(maybe_ingredients[allergen])
not_ingredients = all_ingredients.difference(maybe_ingredients_all)
ans = 0
for not_ingredient in not_ingredients:
    ans += count_ingredients[not_ingredient]
print("P1:", ans)

found_ingredients = dict()
while len(found_ingredients) < len(maybe_ingredients):
    for allergen in maybe_ingredients:
        if allergen in set(found_ingredients.keys()):
            continue
        if len(maybe_ingredients[allergen]) == 1:
            found_ingredient = maybe_ingredients[allergen].pop()
            found_ingredients[allergen] = found_ingredient
            for allergen in maybe_ingredients:
                maybe_ingredients[allergen].discard(found_ingredient)

sorted_ingredients = {k: found_ingredients[k] for k in sorted(found_ingredients)}
canonical_ingredients = ",".join(sorted_ingredients.values())
print("P2:", canonical_ingredients)
