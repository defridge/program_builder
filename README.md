# Program Builder

This Python based Program Builder is designed to allow the user to create a custom gym training program that is specific to their needs. The app has 2 options for a gym program, Muscle Building and Strength Building and depending on the information, such as the type of split they would like, the number of days they are looking to train and the weight they lifted on their last gym session the app will build a full workout that the user can follow and take all the guesswork out of their training. The link to the live site can be found here: [Program Builder](https://program-builder-790334250615.herokuapp.com/).

![Program Builder Menu Page](docs/readmepics/program_builder.png)

## Features

### Site Goals

* The goal of the site is to provide the user with a very simple but detailed approach to creating a gym program tailored to their goals.

### Target Audience

* Anyone who is familiar with a gym environment and resistance training exercises but doesn't know where to start with regards to the program to follow.

### App Walkthrough

* MAIN MENU
    * Upon loading the app the user will be welcomed and asked if they are ready to first answer a series of medical questions (Medical Par-Q Form) before a gym program is created.
    * This is to ensure that before the user starts training that there are no issues that may cause an injury.
    * This user is asked to answer yes or no. Yes will bring them to the questions and no will ask them to return to the app when they are ready

![Main Menu](docs/readmepics/main_menu.png)

* MEDICAL QUESTIONS (Medical Par-Q Form)
    * There are 5 questions in total the user must answer one at a time.
        * Question 1: Do you have a heart condition? (Yes/No)
        * Question 2: When you do physical activity, do you feel pain in your chest? (Yes/No)
        * Question 3: Are you pregnant? (Yes/No)
        * Question 4: Do you have a joint or bone problem? (Yes/No)
        * Question 5: Do you ever lose consciousness or Do you lose your balance because of dizziness? (Yes/No)

![Par-Q Questions](docs/readmepics/par_q.png)

* If the user answers "Yes" to any of these questions they will be shown a message asking them to first obtain medical clearance before continuing and the app will jump back to the main menu section.

![Yes response to Par-Q Questions](docs/readmepics/yes_par_q.png)

* If the user answers “No” to all questions they will be clear to proceed to the next section of the app.

* PROGRAM OPTIONS
    * After the user has passed the medical questions they are asked to choose from 2 types of gym program.
        * Muscle Building Program
        * Strength Building Program
    * The user must enter 1 or 2 to make their selection.

![Program Options](docs/readmepics/program_options.png)

* MUSCLE BUILDING PROGRAM
    * If the user chooses the Muscle Building Program they are then asked about what type of muscle building program they would like, the options are:
        * Full Body Training Split
        * Upper/Lower Training Split
        * Push, Pull, Legs Training Split
    * The user will then select and option by inputting 1, 2, or 3

![Muscle Building Program](docs/readmepics/muscle_building_program.png)

* MUSCLE BUILDING PROGRAM - FREQUENCY
    * After choosing one of the options for a type of muscle building program the user will then be asked about their preference for training frequency.
    * Depending on the chosen split the options can be anywhere from 2 days a week to 5/6 days per week.
    * Once a user has chosen their desired frequency the app will build their muscle building program.

![Frequency 1](docs/readmepics/frequency1.png)

![Frequency 2](docs/readmepics/frequency2.png)

* MUSCLE BUILDING PROGRAM - THE FINISHED PROGRAMS
    * With the frequency chosen the user's type specific program will be built and displayed on screen.
    * Underneath the program the user will also see notes on the program such as what order to complete the workouts in and when they should take rest days.

![Finished Program](docs/readmepics/finished_program.png)

* After the program and program info has been built and displayed the user will asked to press any key and enter to continue and then be presented with another menu with the following options
    * They can go to the Strength Building Program section
    * They can go back to the Muscle Building Program section
    * They can go back to the Main Menu
    * They can exit the app

![End Choice](docs/readmepics/end_choice.png)

* STRENGTH BUILDING PROGRAM
    * The second option the user has in terms of type of program is a Strength Building Program.
    * In this section the user will be asked to input some info from the previous workouts in order to allow for the app to work out starting weights when the final program is designed.
    * The user is asked to input the weight they lifted in kg and for how many reps for the exercises Squat, Bench, and Deadlift.
    * The user will be asked to enter this info 1 at a time and then the custom program will be built.
    * If the user has never performed these lifts before they are instructed to first perform these exercises in a gym first for a few sessions and then return to the app to enter the info.

![Strength Building Program](docs/readmepics/strength_building_program.png)

* After the user enters the required exercise info the app will calculate their 1 rep max on all 3 lifts and display that info.
* Below the 1 rep max info the app will create the strength building program.
* The app will then calculate 80% of the 1 rep max on all 3 lifts and insert this weight into the program to give the user the appropriate starting point to help them maximize strength gains.

![1 Rep Max](docs/readmepics/1_rep_max.png)


* 1RM (1 rep max) calculating based off the user input.

![Calculated 1RM](docs/readmepics/calculated_1rm.png)

* Finished strength building program showing the 80% of 1RM's calculated along with some info about the program below.
* Like with the muscle building program the user will be then taken to the final section which will allow them to restart the strength building program section, go to the muscle building program section, go to the main menu or exit the app.

![Finished Strength Building Program](docs/readmepics/finished_strength_program.png)

## Logical Flow

* Main Menu

![Flow Main Menu](docs/flowcharts/flow_main_menu.png)

* Medical Par-Q Questions

![Flow Par-Q](docs/flowcharts/flow_parq.png)

* Program Menu

![Flow Program Menu](docs/flowcharts/flow_program_options.png)

* Muscle Building Program

![Flow Muscle Building Program](docs/flowcharts/flow_muscle_building.png)

* Muscle Building Program Part 2

![Flow Full Body](docs/flowcharts/flow_full_body.png)
![Flow Upper Lower](docs/flowcharts/flow_upper_lower.png)
![Flow PPL](docs/flowcharts/flow_ppl.png)

* Strength Building Program

![Flow Strength Building](docs/flowcharts/flow_strenght_building.png)

* End/Exit Function

![End/Exit Function](docs/flowcharts/flow_end_exit.png)

## Technologies

* Python - Python was the main language used to build the application
* Python Modules - numPy and os modules used for 1 rep max calculations and to clear the screen when going from one section to another in the app
* IDE - The application was developed using Codeanywhere IDE and VScode
* Github - The source code is hosted on Github.
* Git - Git was used to commit and push code during the project.

## Testing

### Functional Testing

Below you will see a breakdown of all tests carried out on the app to ensure it functions as intended:

![Main Menu Testing](docs/testing/main_menu_test.png)
![Program Options Testing](docs/testing/program_options_test.png)
![Muscle Building Testing](docs/testing/muscle_building_test.png)
![Workouts Testing](docs/testing/muscle_building_strength_workouts_test.png)
![Exit/Restart Menu Testing](docs/testing/exit_restart_test.png)

### Case Study

A case study was done to check that the calculations preformed by the app were correct when determining a 1 rep max and then 80% of this 1 rep max to use within the strength building program. Details below show app working correctly:

![Case Study](docs/testing/case_study.png)

### Pep8 Validation

When tested using online validator https://pep8ci.herokuapp.com/ no errors were found.

![Pep8 Validator](docs/testing/pep.png)

### Bugs and Fixes

To this date app is functioning as expected with no issues or bugs.

With more time in the future the plan is to implement some color using colorama Python Package.

## Deployment

### Heroku Deployment

Please find steps below for deployment to Heroku

* Go to Heroku, sign in and click "New" to create a new app.
* Choose an app name and region (Europe), click "Create app".
* Go to "Settings" and navigate to Config Vars. Add the following config variables:
    * PORT : 8000
* Navigate to "Deploy". Set the deployment method to Github and enter repository name and connect.
* Scroll down to Manual Deploy, select "main" branch and click "Deploy Branch".
* The app will now be deployed to heroku

## Credits

* [w3schools](https://www.w3schools.com/python/default.asp) was used throughout the project as a reference when writing Python code.
* The formula to calculate 1RM was taken from [brainmac.co.uk](https://www.brianmac.co.uk/maxload.htm)
* My Mentor Gareth McGirr for his guidance and support throughout my project
