


def main_menu():
    """
    Displays main menu and welcome message when program is started.
    """
    while True:
        print("***************************************\n")
        print("WECOME TO OUR ONLINE GYM PROGRAM BUILDER.\n")
        print("Before we get started building your program\nwe have a few quick medical questions you must answer.\n")
        prompt = "Are you ready to proceed: (Yes/No)"
        response = input(prompt + "\n")

        try:
            if response in ["Yes", "yes", "y", "YES", "Y"]:
                print("Proceeding...\n")
                par_q()
            else:
                if response in ["No", "no", "NO", "n", "N"]:
                    print("That's no problem! Come back when you are ready!")
                else:
                    print("Invalid response. Please enter 'Yes' or 'No'.")
        except ValueError:
            print("Invalid input. Please enter 'Yes' or 'No'.")


def par_q():
    """
    Will take the user through a series of medical questions that they must answer yes or no
    """
    while True:
        q1 = input("Question 1: Do you have a heart condition? (Yes/No)\n")

        if q1 in ["No", "no", "NO", "n", "N"]:
            q2 = input("Question 2: When you do physical activity, do you feel pain in your chest? (Yes/No)\n")

            if q2 in ["No", "no", "NO", "n", "N"]:
                q3 = input("Question 3: Are you pregnant? (Yes/No)\n")

                if q3 in ["No", "no", "NO", "n", "N"]:
                    q4 = input("Question 4: Do you have a joint or bone problem? (Yes/No)\n")

                    if q4 in ["No", "no", "NO", "n", "N"]:
                        q5 = input("Question 5: Do you ever lose consciousness\nor do you lose your balance because of dizziness? (Yes/No)\n")

                        if q5 in ["No", "no", "NO", "n", "N"]:
                            print("Thank you! You are clear to proceed\n")
                            program_options()
                            break

                        elif q5 in ["Yes", "yes", "y", "YES", "Y"]:
                            print("Question 5 answered 'Yes'. Please obtain medical clearance to before continuing")
                            break

                        else:
                            print("Invalid input. Please enter 'Yes' or 'No'.")

                    elif q4 in ["Yes", "yes", "y", "YES", "Y"]:
                        print("Question 4 answered 'Yes'. Please obtain medical clearance to before continuing")
                        break

                    else:
                        print("Invalid input. Please enter 'Yes' or 'No'.")

                elif q3 in ["Yes", "yes", "y", "YES", "Y"]:
                    print("Question 3 answered 'Yes'. Please obtain medical clearance to before continuing")
                    break

                else:
                    print("Invalid input. Please enter 'Yes' or 'No'.")

            elif q2 in ["Yes", "yes", "y", "YES", "Y"]:
                print("Question 2 answered 'Yes'. Please obtain medical clearance to before continuing")
                break

            else:
                print("Invalid input. Please enter 'Yes' or 'No'.")

        elif q1 in ["Yes", "yes", "y", "YES", "Y"]:
            print("Question 1 answered 'Yes'. Please obtain medical clearance to before continuing")
            break

        else:
            print("Invalid input. Please enter 'Yes' or 'No'.")


def program_options():
    """
    Display options for prgram type so the user can choose.
    """

    print("Please choose for one of the following options below\n")
    print("1. Muscle Building Program")
    print("2. Strength Building Program")
    print("3. Sports Specific Program\n")

    while True:
        try:
            option = int(input("Enter your choice here: \n"))
        except ValueError:
            print("Please enter a number")
            continue

        if option == 1:
            print("Thank you!\n")
            muscle_building_program()
            break
        elif option == 2:
            print("Program 2")
            break
        elif option == 3:
            print("Program 3")
            break
        else:
            print("Invalid Choice")


def muscle_building_program():
    """
    Function to gather info to start building Muscle Building gym program.
    """

    print("To create the best Muscle Building Gym Program for you we have a few questions to ask.\n")
    print("What type of training split are you looking for? \n")
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
                    print("Thank you! Building your program now...\n")
                    two_days_per_wk_full_body_muscle_building_program()
                    break
                elif option == 2:
                    print("Thank you! Building your program now...\n")
                    three_days_per_wk_full_body_muscle_building_program()
                    break
                elif option == 3:
                    print("Thank you! Building your program now...\n")
                    four_days_per_wk_full_body_muscle_building_program()
                    break
                else:
                    print("Invalid Choice")
        elif option == 2:
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
                    print("Thank you! Building your program now...\n")
                    break
                elif option == 2:
                    print("Thank you! Building your program now...\n")
                    break
                elif option == 3:
                    print("Thank you! Building your program now...\n")
                    break
                else:
                    print("Invalid Choice")
        elif option == 3:
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
                    print("Thank you! Building your program now...\n")
                    break
                elif option == 2:
                    print("Thank you! Building your program now...\n")
                    break
                elif option == 3:
                    print("Thank you! Building your program now...\n")
                    break
                else:
                    print("Invalid Choice")
        else:
            print("Invalid Choice")

def two_days_per_wk_full_body_muscle_building_program():
    """
    This function prints a 2 day per week, full body muscle building program to the console.
    """
    
    print("You have chosen a 2 Day Per Week, Full Body Split, Muscle Building Program")
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
    print("Thank you for using this online Program Builder!\nWe wish you all the best with your fitness journey!")
    main_menu()


def three_days_per_wk_full_body_muscle_building_program():
    """
    This function prints a 3 day per week, full body muscle building program to the console.
    """
    
    print("You have chosen a 3 Day Per Week, Full Body Split, Muscle Building Program")
    print("Please find you program below: \n")
    print("\tDay 1")
    print("\tBarbell Bench Press,           1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tWide Grip Pulldowns,           1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tRomanian Deadlift (RDL),       1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tLeg Extension,                 1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tCable Lateral Raise,           1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tCable Bicep Curls,             1-2 sets, 5-8 reps, 2-3 mins rest\n")
    print("\tDay 2")
    print("\tIncline Bench Press,           1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tChest Supported Row,           1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tLying Leg Curl,                1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tBulgarian Split Squat,         1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tRear Delt Flyes,               1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tCable Tricep Pushdown,         1-2 sets, 5-8 reps, 2-3 mins rest\n")
    print("\tDay 3")
    print("\tPec Dec,                       1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tNarrow Grip Pulldown,          1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tSeated Leg Curl,               1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tLeg Press,                     1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tShoulder Press Machine,        1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tSeated Calf Raise,             1-2 sets, 5-8 reps, 2-3 mins rest\n")
    
    print("Please allow for at least one day off between Day's 1, 2 and 3\n")
    print("Thank you for using this online Program Builder!\nWe wish you all the best with your fitness journey!")
    main_menu()


def four_days_per_wk_full_body_muscle_building_program():
    """
    This function prints a 4 day per week, full body muscle building program to the console.
    """
    
    print("You have chosen a 4 Day Per Week, Full Body Split, Muscle Building Program")
    print("Please find you program below: \n")
    print("\tDay 1")
    print("\tBarbell Bench Press,           1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tWide Grip Pulldowns,           1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tRomanian Deadlift (RDL),       1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tLeg Extension,                 1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tCable Lateral Raise,           1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tCable Bicep Curls,             1-2 sets, 5-8 reps, 2-3 mins rest\n")
    print("\tDay 2")
    print("\tIncline Bench Press,           1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tChest Supported Row,           1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tLying Leg Curl,                1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tBulgarian Split Squat,         1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tRear Delt Flyes,               1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tSeated Calf Raise,             1-2 sets, 5-8 reps, 2-3 mins rest\n")
    print("\tDay 3")
    print("\tDips,                          1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tLat Prayer,                    1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tLying Leg Curl,                1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tHack Squat,                    1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tT-Bar Row,                     1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tCable Tricep Pushdown,         1-2 sets, 5-8 reps, 2-3 mins rest\n")
    print("\tDay 4")
    print("\tPec Dec,                       1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tNarrow Grip Pulldown,          1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tSeated Leg Curl,               1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tLeg Press,                     1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tShoulder Press Machine,        1-3 sets, 5-8 reps, 2-3 mins rest")
    print("\tSeated Calf Raise,             1-2 sets, 5-8 reps, 2-3 mins rest\n")
    
    print("Please allow for at least one day off between Day's 1, 2, 3 and 4\n")
    print("Thank you for using this online Program Builder!\nWe wish you all the best with your fitness journey!")
    main_menu()



main_menu()
