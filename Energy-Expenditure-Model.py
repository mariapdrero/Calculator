"""
Comp 115 - Project 1
Human Kinetics model for estimating total daily energy expenditure

Ask user for 6 input factors, estimate and report their estimated total daily energy expenditure (ETDEE)

Author:  Maria Pedrero
Date:  Friday, February 11th, 2023
Credits: Joseph Fall for assigning this project to my COMP 115 class and Caroline Soo from Human Kinetics for allowing the class to adapt this assignment.

"""

import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
from pyfiglet import figlet_format

# GLOBAL VARIABLES
bold = '\033[1m'
italics = '\033[3m'
normal_text = '\033[0m'
underline = '\033[4m'
reset_color = '\033[39m'
dashline = '\u2015'
v_dashline = '|'
triplevdash = '|||'
calculator = ("_____________________\n" +
      "|  _________________  |\n" +
      "| | COMP115         | |\n" +
      "| |_PROJECT_01______| |\n" +
      "|  ___ ___ ___   ___  |\n" +
      "| | 7 | 8 | 9 | | + | |\n" +
      "| |___|___|___| |___| |\n" +
      "| | 4 | 5 | 6 | | - | |\n" +
      "| |___|___|___| |___| |\n" +
      "| | 1 | 2 | 3 | | x | |\n" +
      "| |___|___|___| |___| |\n" +
      "| | . | 0 | = | | / | |\n" +
      "| |___|___|___| |___| |\n" +
      "|_____________________|")

alien = ("      .--.   |V|\n\
     /    \\ _| /\n\
     q .. p \\ /\n\
      \\--/  //\n\
bye  __||__//\n\
    /.    _/\n\
   // \\  /\n\
  //   ||\n\
  \\\\  /  \\\n\
   )\\|    |\n\
  / || || |\n\
  |/\\| || |\n\
     | || |\n\
     \\ || /\n\
   __/ || \\__\n\
  \\____/\\____/")


# Step 1: FUNCTIONS
# BMR FUNCTION
def bmr(gender, weight, height, age):
    """ computes the basal metabolic rate expenditure for a person with given weight (kg), height (m) and age (years), the total will vary depending on their gender."""
    weight_kg = weight / 2.205
    height_cm = height * 2.54
    if gender == 'male':
        return 66 + (13.7 * weight_kg) + (5 * height_cm) - (6.8 * age)
    elif gender == 'female':
        return 655 + (9.6 * weight_kg) + (1.8 * height_cm) - (4.7 * age)

assert bmr('female', 121, 70.08, 19) == 1412.9084810884353
assert bmr('male', 155, 70, 47) == 1598.4385487528345


# PHYSICAL ACTIVITY EXPENDITURE FUNCTIONS
# Function 1: shows list of options to user and gets input
def select_option():
    """ this function shows the user four options to choose their input from and returns activity factor """
    options = [{
        'Level': 1, 'Description':"Sedentary - mostly resting with little or no activity."}, 
               {'Level': 2,'Description':"Light - occasional unplanned activity e.g. going for a walk, or a swim or skiing."}, 
               {'Level':3,'Description':"Moderate - daily planned activity such as short jogs, brisk walk."},
               {'Level': 4,'Description':"Heavy - daily planned workouts (hours or several hours of continuous activity."
    }]

    print(f"{Fore.CYAN + Style.NORMAL + underline}Choose a level of activity from the following options:")
    for i, option in enumerate(options):
        print("Level: " + str(option['Level']) + " Description: " +
              option['Description'])

    selected_option = int(input(f"{Fore.CYAN + italics}Type the level number you chose (1 - 4): " + reset_color + normal_text))
    return activity_factor(selected_option)

# Function 2: converts the level from user input to the activity factor decimal.
def activity_factor(level):
    """this function determines the activity factor of the person by taking the level of activity they inputed and transforms it into the activity factor"""
    if level == 1:
        return 0.25
    elif level == 2:
        return 0.375
    elif level == 3:
        return 0.55
    elif level == 4:
        return 0.78
    else:
        return 0


assert activity_factor(3) == 0.55
assert activity_factor(6) == 0
assert activity_factor(4) == 0.78


# Function 3: final answer given the two prior functions
def phys_act_exp(users_bmr, activity_factor):
    """this function gives the total physical activity expenditure by multiplying the bmr and the activity factor."""
    return users_bmr * activity_factor
assert phys_act_exp(1412.9084810884353, 0.78) == 1102.0686152489795
assert phys_act_exp(2726.1755782312925, 0.55) == 1499.396568027211

# THERMIC EFFECT OF FOOD EXPENDITURE FUNCTIONS
def thermic_effect(kcal):
    """this function returns the thermic effect of food expenditure by taking the amount of calories consumed and multiplying it by 5% (0.05)."""
    return kcal * 0.05
assert thermic_effect(2631.56) == 131.578
assert thermic_effect(1800) == 90
assert thermic_effect(1456.92) == 72.846


# TOTAL DAILY ESTIMATED ENERGY EXPENDITURE
def daily_energy():
    """this function returns the total daily estimated energy expenditure by adding the users bmr, their phyisical activity and their thermic effect of food."""
    return users_bmr + users_physicalActivity + users_thermicEffect
# i wasn't able to do an assert test here because the function doesn't call for any arguments since i'm just adding them up, however, i've already tested each argument separately. But if i could do an assert test here (if the function had arguments in it), then i would do it like this:
# assert daily_energy(1412.9084810884353, 1102.0686152489795, 115.0) == 2629.977096337415

    
# INTRO OF THE MAIN PROGRAM
input(f'{Fore.YELLOW + Style.BRIGHT}\u00BB'+" Press enter to start...")
print(f'{Fore.WHITE}' + (figlet_format("welcome to the", font="small")), end="")
print(figlet_format("Estimated Daily Energy Expenditure Calculator",
font="straight"))
print(calculator)
print()
print()
print(f"{Fore.RED}By: ", end="")
print("María Pedrero")
print(f"{Fore.RED}Last Updated: ", end="")
print("Saturday, February 11th, 2023")
print(f"{Fore.RED}Harris-Benedict Calculator Used: ", end="")
print("https://www.omnicalculator.com/health/bmr-harris-benedict-equation")
print()
input(f'{Fore.YELLOW + Style.BRIGHT}\u00BB'+" Press enter to continue...")
print()

# Step 2: MAIN PROGRAM
# BMR INPUT VALUES & VARIABLES
weight_num = float(input(f"{Fore.CYAN}Type your weight in pounds: " + reset_color))
height_num = float(input(f"{Fore.CYAN}Type your height in inches: " + reset_color))
gender_str = str(input(f"{Fore.CYAN}Type your gender (either male or female): " + reset_color))
age_num = int(input(f"{Fore.CYAN}Type your age in years: " + reset_color))
print()
users_activity_factor = select_option()
users_bmr = bmr(gender_str, weight_num, height_num, age_num)
# PHYSICAL ACTIVITY EXPENDITURE INPUT VALUES & VARIABLES
users_physicalActivity = phys_act_exp(users_bmr, users_activity_factor)
# THERMIC EFFECT OF FOOD EXPENDITURE INPUT VALUES & VARIABLES
print()
kcal = float(input(f"{Fore.CYAN}Type your approximate daily calorie intake: " + reset_color))
users_thermicEffect = thermic_effect(kcal)
print()
input(f'{Fore.YELLOW + Style.BRIGHT}\u00BB'+" Press enter to get your results...")
# TOTAL DAILY ESTIMATED ENERGY EXPENDITURE INPUT VALUES & VARIABLES
users_totalEnergy = daily_energy()

# BMR OUTPUT
print()
print()
print(Fore.MAGENTA + dashline * 60)
print(Back.BLACK + Fore.GREEN + v_dashline + "Basal metabolic rate expenditure (BMR): ",end="")
print(users_bmr)
# PHYSICAL ACTIVITY OUTPUT
print(Back.BLACK + Fore.GREEN + v_dashline + "Physical activity: ", end="")
print(users_physicalActivity)
# THERMIC EFFECT OUTPUT
print(f"{Back.BLACK + Fore.GREEN + v_dashline}Thermic effect of food: ", end="")
print(users_thermicEffect)
# TOTAL DAILY ENERGY OUTPUT
print(f"{Back.BLACK + Fore.GREEN + Style.BRIGHT + triplevdash}\u2192 Total daily estimated energy: ", end="")
print(users_totalEnergy)
print(Fore.MAGENTA + dashline * 60)

# OUTRO
print((figlet_format("thank you", font="small")), end="")
print(alien)
