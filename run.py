import numpy as np
import os

valid_yes_response = ["Yes", "yes", "YES", "y", "Y"]
valid_no_response = ["No", "no", "NO", "n", "N"]


def main_menu():
    """
    Displays main menu and welcome message when program is started.
    """
    while True:
        print("***************************************\n")
        print("WELCOME TO OUR ONLINE GYM PROGRAM BUILDER.\n")
        print("Before we get started building your program\n"
              "we have a few quick medical questions you must answer.\n")
        prompt = "Are you ready to proceed: (Yes/No)"
        response = input(prompt + "\n")

        try:
            if response in valid_yes_response:
                print("Proceeding...\n")
                par_q_medical_form()
            else:
                if response in valid_no_response:
                    print("That's no problem! Come back when you are ready!")
                    exit()
                else:
                    print("Invalid response. Please enter 'Yes' or 'No'.")
        except ValueError:
            print("Invalid input. Please enter 'Yes' or 'No'.")


def par_q_medical_form():
    """
    Will take the user through a series of
    medical questions that they must answer yes or no
    """
    while True:
        questions = [
            "Do you have a heart condition?",
            "When you do exercise, do you feel pain in your chest?",
            "Are you pregnant?",
            "Do you have a joint or bone problem?",
            "Do you ever lose your balance because of dizziness?"
        ]

        for i, question in enumerate(questions, start=1):
            while True:
                answer = input(f"Question {i}: {question} (Yes/No)\n").lower()
                if answer in valid_yes_response or valid_no_response:
                    break
                else:
                    print("Invalid input. Please enter 'Yes' or 'No'.")

            if answer in valid_yes_response:
                print(f"Question {i} answered 'Yes'. "
                      "Please obtain medical clearance before continuing.")
                exit()
                return

        os.system("clear")
        program_options()
        break


def program_options():
    """
    Display options for program type so the user can choose.
    """

    print("Thank you! You are clear to proceed.\n")
    print("Please choose for one of the following options below\n")
    print("............................")
    print("1. Muscle Building Program")
    print("2. Strength Building Program")
    print("............................\n")

    while True:
        try:
            option = int(input("Enter your choice here: \n"))
        except ValueError:
            print("Please enter a number")
            continue

        if option == 1:
            os.system("clear")
            muscle_building_program()
            break
        elif option == 2:
            os.system("clear")
            strength_building_program()
            break
        else:
            print("Invalid Choice")


def muscle_building_program():
    """
    Function to gather info to start building a Muscle Building gym program.
    """

    print("Thank you!\n")
    print("To create the best Muscle\nBuilding Gym Program "
          "for you we have a few questions to ask.\n")
    print("What type of training split are you looking for?\n")
    print("1. Full Body Training Split")
    print("2. Upper/Lower Training Split")
    print("3. Push, Pull, Legs Training Split\n")

    while True:
        try:
            option = int(input("Enter your choice here: \n"))
        except ValueError:
            print("Please enter a number")
            continue

        if option == 1:
            os.system("clear")
            print("Thank you! \n")
            print("How many days a week would you like the program to be? \n")
            print("1. I would like to train 2 days per week")
            print("2. I would like to train 3 days per week")
            print("3. I would like to train 4 days per week\n")
            while True:
                try:
                    option = int(input("Enter your choice here: \n"))
                except ValueError:
                    print("Please enter a number")
                    continue
                    break

                if option == 1:
                    os.system("clear")
                    two_days_per_wk_full_body_muscle_building_program()
                    break
                elif option == 2:
                    os.system("clear")
                    three_days_per_wk_full_body_muscle_building_program()
                    break
                elif option == 3:
                    os.system("clear")
                    four_days_per_wk_full_body_muscle_building_program()
                    break
                else:
                    print("Invalid Choice")
        elif option == 2:
            os.system("clear")
            print("Thank you! \n")
            print("How many days a week would you like the program to be? \n")
            print("1. I would like to train 2 days per week")
            print("2. I would like to train 3 days per week")
            print("3. I would like to train 4 days per week\n")
            while True:
                try:
                    option = int(input("Enter your choice here: \n"))
                except ValueError:
                    print("Please enter a number")
                    continue
                    break

                if option == 1:
                    os.system("clear")
                    two_days_per_wk_upper_lower_muscle_building_program()
                    break
                elif option == 2:
                    os.system("clear")
                    three_days_per_wk_upper_lower_muscle_building_program()
                    break
                elif option == 3:
                    os.system("clear")
                    four_days_per_wk_upper_lower_muscle_building_program()
                    break
                else:
                    print("Invalid Choice")
        elif option == 3:
            os.system("clear")
            print("Thank you! \n")
            print("How many days a week would you like the program to be? \n")
            print("1. I would like to train 3 days per week")
            print("2. I would like to train 4 days per week")
            print("3. I would like to train 5/6 days per week\n")
            while True:
                try:
                    option = int(input("Enter your choice here: \n"))
                except ValueError:
                    print("Please enter a number")
                    continue
                    break

                if option == 1:
                    os.system("clear")
                    three_days_per_wk_push_pull_legs_muscle_building_program()
                    break
                elif option == 2:
                    os.system("clear")
                    four_days_per_wk_push_pull_legs_muscle_building_program()
                    break
                elif option == 3:
                    os.system("clear")
                    five_six_days_per_wk_p_p_l_muscle_building_program()
                    break
                else:
                    print("Invalid Choice")
        else:
            print("Invalid Choice")


def two_days_per_wk_full_body_muscle_building_program():
    """
    This function prints a 2 day per week,
    full body muscle building program to the console.
    """

    print("Thank you! Building your program now...\n")
    print("You have chosen a 2 Day Per Week, "
          "Full Body Split, Muscle Building Program")
    print("Please find you program below: \n")
    print("\tDay 1")
    print("\tBarbell Bench Press,         1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tWide Grip Pulldowns,         1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tRomanian Deadlift (RDL),     1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tLeg Extension,               1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tCable Lateral Raise,         1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tCable Bicep Curls,           1-2 sets, 5-8 reps, 2-3 mins rest")
    print("\tSeated Calf Raise,           1-2 sets, 5-8 reps, 2-3 mins rest\n")
    print("\tDay 2")
    print("\tPec Dec,                     1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tChest Supported Row,         1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tSeated Leg Curl,             1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tLeg Press,                   1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tShoulder Press Machine,      1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tCable Tricep Pushdown,       1-2 sets, 5-8 reps, 2-3 mins rest")
    print("\tStanding Calf Raise,         1-2 sets, 5-8 reps, 2-3 mins rest\n")
    print("Please allow for at least one day off between Day's 1 and 2\n")
    print("Thank you for using this online Program Builder!\n"
          "We wish you all the best with your fitness journey!\n")
    input("Press any key and Enter to continue.\n")
    os.system('cls' if os.name == 'nt' else 'clear')
    exit_or_restart()


def three_days_per_wk_full_body_muscle_building_program():
    """
    This function prints a 3 day per week,
    full body muscle building program to the console.
    """

    print("Thank you! Building your program now...\n")
    print("You have chosen a 3 Day Per Week, "
          "Full Body Split, Muscle Building Program")
    print("Please find you program below: \n")
    print("\tDay 1")
    print("\tBarbell Bench Press,           1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tWide Grip Pulldowns,           1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tRomanian Deadlift (RDL),       1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tLeg Extension,                 1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tCable Lateral Raise,           1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tCable Bicep Curls,             1-2 sets, 5-8 reps, "
          "2-3 mins rest\n")
    print("\tDay 2")
    print("\tIncline Bench Press,           1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tChest Supported Row,           1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tLying Leg Curl,                1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tBulgarian Split Squat,         1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tRear Delt Flyes,               1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tCable Tricep Pushdown,         1-2 sets, 5-8 reps, "
          "2-3 mins rest\n")
    print("\tDay 3")
    print("\tPec Dec,                       1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tNarrow Grip Pulldown,          1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tSeated Leg Curl,               1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tLeg Press,                     1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tShoulder Press Machine,        1-3 sets, 5-8 reps, "
          "2-3 mins rest")
    print("\tSeated Calf Raise,             1-2 sets, 5-8 reps, "
          "2-3 mins rest\n")
    print("Please allow for at least one day off between Day's 1, 2 and 3\n")
    print("Thank you for using this online Program Builder!\n"
          "We wish you all the best with your fitness journey!\n")
    input("Press any key and Enter to continue.\n")
    os.system('cls' if os.name == 'nt' else 'clear')
    exit_or_restart()


def four_days_per_wk_full_body_muscle_building_program():
    """
    This function prints a 4 day per week,
    full body muscle building program to the console.
    """

    print("Thank you! Building your program now...\n")
    print("You have chosen a 4 Day Per Week, "
          "Full Body Split, Muscle Building Program")
    print("Please find you program below: \n")
    print("\tDay 1")
    print("\tBarbell Bench Press,           1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tWide Grip Pulldowns,           1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tRomanian Deadlift (RDL),       1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tLeg Extension,                 1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tCable Lateral Raise,           1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tCable Bicep Curls,             1-2 sets, 5-8 reps, "
          "2-3 mins rest\n")
    print("\tDay 2")
    print("\tIncline Bench Press,           1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tChest Supported Row,           1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tLying Leg Curl,                1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tBulgarian Split Squat,         1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tRear Delt Flyes,               1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tSeated Calf Raise,             1-2 sets, 5-8 reps, "
          "2-3 mins rest\n")
    print("\tDay 3")
    print("\tDips,                          1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tLat Prayer,                    1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tLying Leg Curl,                1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tHack Squat,                    1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tT-Bar Row,                     1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tCable Tricep Pushdown,         1-2 sets, 5-8 reps, "
          "2-3 mins rest\n")
    print("\tDay 4")
    print("\tPec Dec,                       1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tNarrow Grip Pulldown,          1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tSeated Leg Curl,               1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tLeg Press,                     1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tShoulder Press Machine,        1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tSeated Calf Raise,             1-2 sets, 5-8 reps, "
          "2-3 mins rest\n")
    print("Please allow for at least one day off between "
          "Day's 1, 2, 3 and 4\n")
    print("Thank you for using this online Program Builder!\n"
          "We wish you all the best with your fitness journey!\n")
    input("Press any key and Enter to continue.\n")
    os.system('cls' if os.name == 'nt' else 'clear')
    exit_or_restart()


def two_days_per_wk_upper_lower_muscle_building_program():
    """
    This function prints a 2 day per week,
    upper/lower muscle building program to the console.
    """

    print("Thank you! Building your program now...\n")
    print("You have chosen a 2 Day Per Week, "
          "Upper/Lower Split, Muscle Building Program")
    print("Please find you program below: \n")
    print("\tUpper Day")
    print("\tBarbell Bench Press,         1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tWide Grip Pulldowns,         1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tLateral Raise Machine,       1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tRear Delt Flyes,             1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tCable Bicep Curls,           1-2 sets, 5-8 reps, 2-3 mins rest\n")
    print("\tLower Day")
    print("\tRomanian Deadlift (RDL),     1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tLeg Press,                   1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tBulgarian Split Squat,       1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tSeated Calf Raise,           1-2 sets, 5-8 reps, 2-3 mins rest")
    print("\tCable Ab Crunch,             1-2 sets, 5-8 reps, 2-3 mins rest\n")
    print("Please allow for at least one day "
          "off between Upper and Lower days\n")
    print("Thank you for using this online Program Builder!\n"
          "We wish you all the best with your fitness journey!\n")
    input("Press any key and Enter to continue.\n")
    os.system('cls' if os.name == 'nt' else 'clear')
    exit_or_restart()


def three_days_per_wk_upper_lower_muscle_building_program():
    """
    This function prints a 3 day per week,
    upper/lower muscle building program to the console.
    """

    print("Thank you! Building your program now...\n")
    print("You have chosen a 3 Day Per Week, "
          "Upper/Lower Split, Muscle Building Program")
    print("Please find you program below: \n")
    print("\tUpper Day 1")
    print("\tBarbell Bench Press,         1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tWide Grip Pulldowns,         1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tLateral Raise Machine,       1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tRear Delt Flyes,             1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tCable Bicep Curls,           1-2 sets, 5-8 reps, 2-3 mins rest\n")
    print("\tLower Day 2")
    print("\tRomanian Deadlift (RDL),     1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tLeg Press,                   1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tBulgarian Split Squat,       1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tSeated Calf Raise,           1-2 sets, 5-8 reps, 2-3 mins rest")
    print("\tCable Ab Crunch,             1-2 sets, 5-8 reps, 2-3 mins rest\n")
    print("\tUpper Day 2")
    print("\tPec Dec,                     1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tPlate Loaded Lat Row,        1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tShoulder Press Machine,      1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tRear Delt Flyes,             1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tCable Tricep Pushdown,       1-2 sets, 5-8 reps, 2-3 mins rest\n")
    print("\tLower Day 2")
    print("\tSeated Leg Curl,             1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tHack Squat,                  1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tLeg Extension,               1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tStanding Calf Raise,         1-2 sets, 5-8 reps, 2-3 mins rest")
    print("\tLying Leg Raise,             1-2 sets, 5-8 reps, 2-3 mins rest\n")
    print("Please allow for at least one day "
          "off between Upper and Lower days\n")
    print("For 3 days per week follow like below:")
    print("Week 1: Upper 1, Lower 1, Upper 2")
    print("Week 2: Lower 2, Upper 1, Lower 1")
    print("Week 3: Upper 1, Lower 1, Upper 2")
    print("etc etc...\n")
    print("Thank you for using this online Program Builder!\n"
          "We wish you all the best with your fitness journey!\n")
    input("Press any key and Enter to continue.\n")
    os.system('cls' if os.name == 'nt' else 'clear')
    exit_or_restart()


def four_days_per_wk_upper_lower_muscle_building_program():
    """
    This function prints a 4 day per week,
    upper/lower muscle building program to the console.
    """

    print("Thank you! Building your program now...\n")
    print("You have chosen a 4 Day Per Week, "
          "Upper/Lower Split, Muscle Building Program")
    print("Please find you program below: \n")
    print("\tUpper Day 1")
    print("\tBarbell Bench Press,         1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tWide Grip Pulldowns,         1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tLateral Raise Machine,       1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tRear Delt Flyes,             1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tCable Bicep Curls,           1-2 sets, 5-8 reps, 2-3 mins rest\n")
    print("\tLower Day 2")
    print("\tRomanian Deadlift (RDL),     1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tLeg Press,                   1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tBulgarian Split Squat,       1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tSeated Calf Raise,           1-2 sets, 5-8 reps, 2-3 mins rest")
    print("\tCable Ab Crunch,             1-2 sets, 5-8 reps, 2-3 mins rest\n")
    print("\tUpper Day 2")
    print("\tPec Dec,                     1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tPlate Loaded Lat Row,        1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tShoulder Press Machine,      1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tRear Delt Flyes,             1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tCable Tricep Pushdown,       1-2 sets, 5-8 reps, 2-3 mins rest\n")
    print("\tLower Day 2")
    print("\tSeated Leg Curl,             1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tHack Squat,                  1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tLeg Extension,               1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tStanding Calf Raise,         1-2 sets, 5-8 reps, 2-3 mins rest")
    print("\tLying Leg Raise,             1-2 sets, 5-8 reps, 2-3 mins rest\n")
    print("Please allow for at least one day "
          "off between Upper and Lower days\n")
    print("For 4 days per week follow like below:")
    print("Week 1: Upper 1, Lower 1, Upper 2, Lower 2")
    print("etc etc...\n")
    print("Thank you for using this online Program Builder!\n"
          "We wish you all the best with your fitness journey!\n")
    input("Press any key and Enter to continue.\n")
    os.system('cls' if os.name == 'nt' else 'clear')
    exit_or_restart()


def three_days_per_wk_push_pull_legs_muscle_building_program():
    """
    This function prints a 3 day per week,
    push/pull/legs muscle building program to the console.
    """

    print("Thank you! Building your program now...\n")
    print("You have chosen a 3 Day Per Week, "
          "Push/Pull/Legs Split, Muscle Building Program")
    print("Please find you program below: \n")
    print("\tPush Day")
    print("\tBarbell Bench Press,         1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tShoulder Press Machine,      1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tLateral Raise Machine,       1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tCable Tricep Pushdowns,      1-2 sets, 5-8 reps, 2-3 mins rest\n")
    print("\tPull Day")
    print("\tWide Grip Lat Pulldown,      1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tT-Bar Row,                   1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tRear Delt Flyes,             1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tCable Bicep Curl,            1-2 sets, 5-8 reps, 2-3 mins rest\n")
    print("\tLeg Day")
    print("\tRomanian Deadlift (RDL),     1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tHack Squat,                  1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tSeated Leg Curl,             1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tSeated Calf Raise,           1-2 sets, 5-8 reps, 2-3 mins rest")
    print("\tCable Crunch,                1-2 sets, 5-8 reps, 2-3 mins rest\n")
    print("Please allow for at least one day off between training days days\n")
    print("Thank you for using this online Program Builder!\n"
          "We wish you all the best with your fitness journey!\n")
    input("Press any key and Enter to continue.\n")
    os.system('cls' if os.name == 'nt' else 'clear')
    exit_or_restart()


def four_days_per_wk_push_pull_legs_muscle_building_program():
    """
    This function prints a 4 day per week,
    push/pull/legs muscle building program to the console.
    """

    print("Thank you! Building your program now...\n")
    print("You have chosen a 4 Day Per Week, "
          "Push/Pull/Legs Split, Muscle Building Program")
    print("Please find you program below: \n")
    print("\tPush Day 1")
    print("\tBarbell Bench Press,         1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tShoulder Press Machine,      1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tLateral Raise Machine,       1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tCable Tricep Pushdowns,      1-2 sets, 5-8 reps, 2-3 mins rest\n")
    print("\tPull Day 1")
    print("\tWide Grip Lat Pulldown,      1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tT-Bar Row,                   1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tRear Delt Flyes,             1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tCable Bicep Curl,            1-2 sets, 5-8 reps, 2-3 mins rest\n")
    print("\tLeg Day 1")
    print("\tRomanian Deadlift (RDL),     1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tHack Squat,                  1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tSeated Leg Curl,             1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tSeated Calf Raise,           1-2 sets, 5-8 reps, 2-3 mins rest")
    print("\tCable Crunch,                1-2 sets, 5-8 reps, 2-3 mins rest\n")
    print("\tPush Day 2")
    print("\tIncline Bench Press,         1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tPec Dec,                     1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tCable Raise Machine,         1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tDips,                        1-2 sets, 5-8 reps, 2-3 mins rest\n")
    print("\tPull Day 2")
    print("\tUpper Back Row,              1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tNarrow Grip Pulldown,        1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tDumbbell Shrugs,             1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tDumbbell Bicep Curl,         1-2 sets, 5-8 reps, 2-3 mins rest\n")
    print("\tLeg Day 2")
    print("\tLying Leg Curl,              1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tLeg Press,                   1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tBulgarian Split Squat,       1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tStanding Calf Raise,         1-2 sets, 5-8 reps, 2-3 mins rest")
    print("\tLying Leg Raise,             1-2 sets, 5-8 reps, 2-3 mins rest\n")
    print("Please allow for at least one day off between training days days\n")
    print("For 4 days per week follow like below:")
    print("Week 1: Push 1, Pull 1, Legs 1, Push 2")
    print("Week 2: Pull 2, Legs 2, Push 1, Pull 1")
    print("Week 3: Legs 1, Push 2, Pull 2, Legs 2")
    print("etc etc...\n")
    print("Thank you for using this online Program Builder!\n"
          "We wish you all the best with your fitness journey!\n")
    input("Press any key and Enter to continue.\n")
    os.system('cls' if os.name == 'nt' else 'clear')
    exit_or_restart()


def five_six_days_per_wk_p_p_l_muscle_building_program():
    """
    This function prints a 5/6 day per week,
    push/pull/legs muscle building program to the console.
    """

    print("Thank you! Building your program now...\n")
    print("You have chosen a 5/6 Day Per Week, "
          "Push/Pull/Legs Split,\nMuscle Building Program")
    print("Please find you program below: \n")
    print("\tPush Day 1")
    print("\tBarbell Bench Press,         1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tShoulder Press Machine,      1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tLateral Raise Machine,       1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tCable Tricep Pushdowns,      1-2 sets, 5-8 reps, 2-3 mins rest\n")
    print("\tPull Day 1")
    print("\tWide Grip Lat Pulldown,      1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tT-Bar Row,                   1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tRear Delt Flyes,             1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tCable Bicep Curl,            1-2 sets, 5-8 reps, 2-3 mins rest\n")
    print("\tLeg Day 1")
    print("\tRomanian Deadlift (RDL),     1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tHack Squat,                  1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tSeated Leg Curl,             1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tSeated Calf Raise,           1-2 sets, 5-8 reps, 2-3 mins rest")
    print("\tCable Crunch,                1-2 sets, 5-8 reps, 2-3 mins rest\n")
    print("\tPush Day 2")
    print("\tIncline Bench Press,         1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tPec Dec,                     1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tCable Raise Machine,         1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tDips,                        1-2 sets, 5-8 reps, 2-3 mins rest\n")
    print("\tPull Day 2")
    print("\tUpper Back Row,              1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tNarrow Grip Pulldown,        1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tDumbbell Shrugs,             1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tDumbbell Bicep Curl,         1-2 sets, 5-8 reps, 2-3 mins rest\n")
    print("\tLeg Day 2")
    print("\tLying Leg Curl,              1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tLeg Press,                   1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tBulgarian Split Squat,       1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tStanding Calf Raise,         1-2 sets, 5-8 reps, 2-3 mins rest")
    print("\tLying Leg Raise,             1-2 sets, 5-8 reps, 2-3 mins rest\n")
    print("For 5/6 days per week follow like below:")
    print("Week 1 (5 days): Push 1, Pull 1, Legs 1, Push 2, Pull 2")
    print("Week 2 (5 days): Legs 2, Push 1, Pull 2, Legs 2, Push 1")
    print("Week 3 (5 days): Pull 1, Legs 1, Push 2, Pull 2, Legs 2\n")
    print("Week 1 (6 days): Push 1, Pull 1, Legs 1, Push 2, Pull 2, Legs 3")
    print("etc etc...\n")
    print("Thank you for using this online Program Builder!\n"
          "We wish you all the best with your fitness journey\n!")
    input("Press any key and Enter to continue.\n")
    os.system('cls' if os.name == 'nt' else 'clear')
    exit_or_restart()


def calculate_1rm(reps, weight):
    """
    Estimate 1RM based on the number of reps performed with a certain weight.
    The 1RM will be calculated using the Brzycki formula.
    """

    x = weight / (1.0278 - 0.0278 * reps)
    estimated_1rm = int(np.around(x))

    return estimated_1rm


def strength_building_program():
    """
    This function will first work out the 1 rep max of the users squat,
    bench and deadlift
    and then build the program with target weights on those lifts.
    """
    print("To create the best Strength Building Program\nwe must first "
          "work out your 1 rep max\nfor the Squat, Bench, and Deadlift.\n")
    print("Please enter the weight you lifted (in kg's)\nand for "
          "how many reps you lifted it from the last time you performed "
          "a Squat,\nBench, and Deadlift\n")
    while True:
        try:
            print("Squat:")
            squat_weight = float(input("Weight lifted (kg's):\n"))
            squat_reps = int(input("Number of reps:\n"))

            print("Bench:")
            bench_weight = float(input("Weight lifted (kg's):\n"))
            bench_reps = int(input("Number of reps:\n"))

            print("Deadlift:")
            deadlift_weight = float(input("Weight lifted (kg's):\n"))
            deadlift_reps = int(input("Number of reps:\n"))
        except ValueError:
            print("Please enter a valid number")
            continue
        break

    squat_1rm = calculate_1rm(squat_reps, squat_weight)
    bench_1rm = calculate_1rm(bench_reps, bench_weight)
    deadlift_1rm = calculate_1rm(deadlift_reps, deadlift_weight)

    os.system("clear")
    print("Calculating 1RM's...\n")
    print(f"Your estimated Squat 1RM is {squat_1rm}kg\n")
    print(f"Your estiamted Bench 1RM is {bench_1rm}kg\n")
    print(f"Your estiamted Deadlift 1RM is {deadlift_1rm}kg\n")
    print("Creating Strength Building Program...\n")
    print("Please find you program below: \n")
    print("\tDay 1")
    print(f"\tBarbell Bench Press,           4 sets, of\n"
          f"\t{int(bench_1rm * 0.80)}kg for 2-3 reps, 4-5 mins rest")
    print(f"\tDeadlift                       4 sets, of\n"
          f"\t{int(deadlift_1rm * 0.80)}kg for 2-3 reps, 4-5 mins rest\n")
    print("\tLeg Extension,                 1-2 sets, 5-8 reps, 2-3 mins rest")
    print("\tLat Pulldown,                  1-2 sets, 5-8 reps, 2-3 mins rest")
    print("\tRear Delt Flyes,               1-2 sets, 5-8 reps, 2-3 mins rest")
    print("\tCable Bicep Curls,             1-2 sets, 5-8 reps, "
          "2-3 mins rest\n")
    print("\tDay 2")
    print("\tShoulder Press,                4 sets, 2-3 reps, 4-5 mins rest")
    print("\tPull Ups,                      4 sets, 2-3 reps, 4-5 mins rest\n")
    print("\tPec Dec,                       1-2 sets, 5-8 reps, 2-3 mins rest")
    print("\tBulgarian Split Squat,         1-2 sets, 5-8 reps, 2-3 mins rest")
    print("\tHip Thrust,                    1-2 sets, 5-8 reps, 2-3 mins rest")
    print("\tNarrow Grip Rows,              1-2 sets, 5-8 reps, "
          "2-3 mins rest\n")
    print("\tDay 3")
    print(f"\tSquat,                         4 sets, of\n"
          f"\t{int(squat_1rm * 0.80)}kg for 2-3 reps, 4-5 mins rest\n")
    print("\tSeated Leg Curl,               1-2 sets, 5-8 reps, 2-3 mins rest")
    print("\tRDL,                           1-2 sets, 5-8 reps, 2-3 mins rest")
    print("\tIncline Bench Press,           1-2 sets, 5-8 reps, 2-3 mins rest")
    print("\tLateral Raise,                 1-2 sets, 5-8 reps, 2-3 mins rest")
    print("\tTricep Pushdown,               1-2 sets, 5-8 reps, "
          "2-3 mins rest\n")

    print("Please allow for at least one day off between Day's 1, 2, and 3\n")
    print("The weight to be lifted in the\nSquat, Bench, and Deadlift "
          "is 80% of your 1 rep max\n")
    print("Thank you for using this online Program Builder!\n"
          "We wish you all the best with your fitness journey!\n")
    input("Press any key and Enter to continue.\n")
    os.system('cls' if os.name == 'nt' else 'clear')
    exit_or_restart()


def exit_or_restart():
    """
    Function to either restart or exit the program builder
    """

    print("Please choose for one of the following options below\n")
    print("............................")
    print("1. Go to Strength Building Program")
    print("2. Go to Muscle Building Program")
    print("3. Main Menu")
    print("4. Exit")
    print("............................\n")

    while True:
        try:
            option = int(input("Enter your choice here: \n"))
        except ValueError:
            print("Please enter a number")
            continue

        if option == 1:
            os.system("clear")
            strength_building_program()
            break
        elif option == 2:
            os.system("clear")
            muscle_building_program()
            break
        elif option == 3:
            os.system("clear")
            main_menu()
        elif option == 4:
            exit()
        else:
            print("Invalid Choice")


main_menu()
