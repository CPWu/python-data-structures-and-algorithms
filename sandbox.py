# # Hello World Example - Output
# print("Hello World")

# # Arithmetic
# print(20 * 10)

# # String Concat
# print("Today is June " + str(4) + "th")

# # Elegant way of Concat
# print(f"Today is June {4}th")

# # Variables
# yearlySalary = 90000
# currency = "CAD"
# print(f"It would be great if Canada's average salary was: {yearlySalary} {currency}")

# # Functions
# def calculateSalary(hourly, hours):
#     castedHours = int(hours)
#     castedHourly = int(hourly)
#     print(f"Your annual salary is: {castedHours * castedHourly * 52}")

# hourly = input("Your hourly wage: \n")
# hours = input("How many hours do you work per week: \n")
# calculateSalary(hourly, hours)

# # Conditionals if/else
# inputNumber = input("How old are you? \n")
# inputNumber = int(inputNumber)

# if inputNumber > 0 and inputNumber < 18:
#     print("You are a kid!")
# elif inputNumber < 30:
#     print("The enjoyable adulthood years.")
# else:
#     print("Grinding for retirement, life is over.")

# Calculte Function
calculation_to_units = 24
name_of_unit= "hours"
10,8
def days_to_units(num_of_days):
    if num_of_days > 0:
        return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"

# Validation Function
def validate_input():
    try:
        user_input_number = int(num_of_days)
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("You entered a 0, please enter a valid positive number.")
        else:
            print("You entered a negative number, please enter a positive number.")
    except ValueError:
        print("Invalid Input")

# # Loops - While Loop
# userInput = ""
# while userInput != 'exit':
#     userInput = input("Type anything or exit to quit.\n")

# Lists
user_input = ""
while user_input != "exit":
        user_input = input("Hello, enter number of days, and I will convert it to hours. \n")
        list_of_days = user_input.split(",")
        print(list_of_days)
        print(set(list_of_days))
        print(type(list_of_days))
        print(type(set(list_of_days)))
        for num_of_days in set(list_of_days):
            validate_input()
