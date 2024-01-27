def calculate_pizza_slices(people):
    # Number of slices per type of pizza
    slices = {
        "Large": 8,
        "Medium": 6,
        "Regular": 4,
        "Small": 1
    }

    # Calculate the number of pizzas needed for each type
    large_pizzas = people // slices["Large"]
    people %= slices["Large"]
    medium_pizzas = people // slices["Medium"]
    people %= slices["Medium"]
    regular_pizzas = people // slices["Regular"]
    people %= slices["Regular"]
    small_pizzas = people // slices["Small"]
    people %= slices["Small"]

    # Total slices needed
    total_slices = (large_pizzas * slices["Large"]) + (medium_pizzas * slices["Medium"]) + (regular_pizzas * slices["Regular"]) + (small_pizzas * slices["Small"])

    return large_pizzas, medium_pizzas, regular_pizzas, small_pizzas, total_slices

# Example usage:
people = 100
large, medium, regular, small, total_slices = calculate_pizza_slices(people)
print(f"If there are {people} individuals:")
print(f"1. we will have {large} Large pizza")
print(f"2. we will have {medium} Medium pizza")
print(f"3. we will have {regular} Regular pizza")
print(f"4. we will have {small} Small pizza")
print(f"Total slices needed: {total_slices}")

people = 19
large, medium, regular, small, total_slices = calculate_pizza_slices(people)
print(f"\nIf there are {people} individuals:")
print(f"1. we will have {large} Large pizza")
print(f"2. we will have {medium} Medium pizza")
print(f"3. we will have {regular} Regular pizza")
print(f"4. we will have {small} Small pizza")
print(f"Total slices needed: {total_slices}")