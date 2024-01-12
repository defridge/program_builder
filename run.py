


def main_menu():
    """
    Displays main menu and welcome message when program is started.
    """
    print("***************************************\n")
    print("WECOME TO OUR ONLINE GYM PROGRAM BUILDER.\n")
    print("Before we get started building your program\nwe have a few quick medical questions you must answer.\n")

    while True:
        prompt = "Are you ready to proceed: (Yes/No)"
        response = input(prompt + "\n")

        try:
            if response in ["Yes", "yes", "y", "YES", "Y"]:
                print("Proceeding...")
            else:
                if response in ["No", "no", "NO", "n", "N"]:
                    print("That's no problem! Come back when you are ready!")
                else:
                    print("Invalid response. Please enter 'Yes' or 'No'.")
        except ValueError:
            print("Invalid input. Please enter 'Yes' or 'No'.")

main_menu()