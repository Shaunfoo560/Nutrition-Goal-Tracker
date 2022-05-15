from dataclasses import dataclass
import matplotlib.pyplot

today = []

# Enter your Calorie, Protein, Fat, and Carbohydrates goals here:
calorie_goal = 2500
protein_goal = 100
fat_goal = 50
carbohydrates_goal = 250

@dataclass
class Food:
    name: str
    calories: int
    protein: int
    fat: int
    carbs: int

done = False

while not done:
    print("""
    - Type "1" to add a meal
    - Type "2" to generate graphs
    """)

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Name of food item: ")
        calories = int(input("Amount of Calories: "))
        proteins = int(input("Amount of Protein: "))
        fats = int(input("Amount of Fat: "))
        carbs = int(input("Amount of Carbohydrates: "))
        food = Food(name, calories, proteins, fats, carbs)
        today.append(food)
        print("Food item has been added")

    elif choice == "2":
        calorie_sum = sum(food.calories for food in today)
        protein_sum = sum(food.protein for food in today)
        fat_sum = sum(food.fat for food in today)
        carbohydrates_sum = sum(food.carbs for food in today)

        fig, axis = matplotlib.pyplot.subplots(3, 2)
        fig.patch.set_facecolor('aqua')
        fig.tight_layout()

        axis[0, 0].pie([calorie_sum, calorie_goal - calorie_sum], labels=["Calories", "Remaining"], autopct="%1.1f%%")
        axis[0, 0].set_title("Calories Progress", fontweight='bold')

        axis[0, 1].bar([0], [calorie_sum], width=0.5, label="Consumed")
        axis[0, 1].bar([0.5], [calorie_goal], width=0.5, label="Goal")
        axis[0, 1].legend()
        axis[0, 1].set_title("Calories Progress", fontweight='bold')

        axis[1, 0].pie([protein_sum, fat_sum, carbohydrates_sum], labels=["Proteins", "Fats", "Carbohydrates"], autopct="%1.1f%%")
        axis[1, 0].set_title("Distribution of Macronutrients consumed", fontweight='bold')

        axis[1, 1].bar([0], [protein_sum], width=0.5, label="Consumed")
        axis[1, 1].bar([0.5], [protein_goal], width=0.5, label="Goal")
        axis[1, 1].legend()
        axis[1, 1].set_title("Proteins Progress", fontweight='bold')

        axis[2, 0].bar([0], [fat_sum], width=0.5, label="Consumed")
        axis[2, 0].bar([0.5], [fat_goal], width=0.5, label="Goal")
        axis[2, 0].legend()
        axis[2, 0].set_title("Fats Progress", fontweight='bold')

        axis[2, 1].bar([0], [carbohydrates_sum], width=0.5, label="Consumed")
        axis[2, 1].bar([0.5], [carbohydrates_goal], width=0.5, label="Goal")
        axis[2, 1].legend()
        axis[2, 1].set_title("Carbohydrates Progress", fontweight='bold')

        matplotlib.pyplot.show()

    else:
        print("Please choose either option 1 or 2")