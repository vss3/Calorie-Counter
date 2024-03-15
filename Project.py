def calculate_total_calories(food_dict):
    total_calories = sum(food_dict.values())
    return total_calories

def find_unhealthiest_food(food_dict):
    unhealthiest_food = min(food_dict, key=food_dict.get)
    return unhealthiest_food

def cut_calories(food_dict, percentage):
    sorted_food = sorted(food_dict.items(), key=lambda x: x[1])
    total_calories_to_cut = sum(food_dict.values()) * percentage / 100

    for food, calories in sorted_food:
        if total_calories_to_cut <= 0:
            break
        calories_to_cut_from_food = min(food_dict[food], total_calories_to_cut)
        food_dict[food] -= calories_to_cut_from_food
        total_calories_to_cut -= calories_to_cut_from_food

def main():
    food_dict = {}
    while True:
        food = input("Enter the name of the food you eat per day (or 'done' to finish): ").strip()
        if food.lower() == 'done':
            break
        calories = float(input("Enter the number of calories for this food: "))
        food_dict[food] = calories

    percentage_to_cut = float(input("Enter the percentage of calories you want to cut: "))
    if percentage_to_cut < 0 or percentage_to_cut > 100:
        print("Invalid percentage value. Please enter a value between 0 and 100.")
        return

    total_calories_before_cut = calculate_total_calories(food_dict)
    print("Total calories before cutting:", total_calories_before_cut)

    unhealthiest_food = find_unhealthiest_food(food_dict)
    print("Unhealthiest food:", unhealthiest_food)

    cut_calories(food_dict, percentage_to_cut)
    total_calories_after_cut = calculate_total_calories(food_dict)
    print("Total calories after cutting:", total_calories_after_cut)

    print("Calories cut:", total_calories_before_cut - total_calories_after_cut)
    print("Updated food list:")
    for food, calories in food_dict.items():
        print(f"{food}: {calories} calories")

if __name__ == "__main__":
    main()