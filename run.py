


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
        q1 = input("Question 1:\nDo you have a heart condition? (Yes/No)\n")

        if q1 in ["No", "no", "NO", "n", "N"]:
            q2 = input("Question 2:\nWhen you do physical activity, do you feel pain in your chest? (Yes/No)\n")

            if q2 in ["No", "no", "NO", "n", "N"]:
                q3 = input("Question 3:\nAre you pregnant? (Yes/No)\n")

                if q3 in ["No", "no", "NO", "n", "N"]:
                    q4 = input("Question 4:\nDo you have a joint or bone problem? (Yes/No)\n")

                    if q4 in ["No", "no", "NO", "n", "N"]:
                        q5 = input("Question 5:\nDo you ever lose consciousness\nor do you lose your balance because of dizziness? (Yes/No)\n")

                        if q5 in ["No", "no", "NO", "n", "N"]:
                            print("Thank you! You are clear to proceed\n")
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


main_menu()
