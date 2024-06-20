# Bodywise Fitness App

## Project Description 
A fitness app in which users can create a profile, and get statistics about their BMI and V02 Max range based on their age and gender. 
Features: 
- User Registration and Login: Securely register and log in to your account.
- Profile Management: Update and manage your personal health information.
- BMI Calculation: Calculate your Body Mass Index (BMI) and view where it falls on the BMI range.
- VO2 Max Range Determination: Determine your VO2 max range based on your profile data.
- Interactive Sidebar Navigation: Easily navigate through different sections of the app.

I have used the Python GUI Tkinter for the development of this project as it is a simple, user-friendly interface with which I have experience. I also used the Python Imaging Library (PIL) to format images onto the Tkinter window. 

I particularly faced challenges with creation of the front-end as I prefer creating algorithms and back-end logic. This included making the side bar, learning how to incorporate different frames in the window, and adding/aligning images. 
In the future, I would like to implement the Goal Visualiser bar, whereby the user can enter their daily steps, sleep, and calories burned goals, and then the actual values for the day, and a bar graph will appear for each field that helps the user visualise how close they are to achieve their goal, in turn encouraging them to improve fitness by working towards these health goals. I would also implement a 'badge' system which gives users virtual badges for different achievements (such as completing a certain goal daily for a week straight), futher facilitating motivation to gain and maintain fitness. 

## Installation Requirements and Dependancies 

To run this project, you need to have Python 3.x installed on your machine along with the following Python packages:

1. **Tkinter**: Tkinter is included with the standard Python distribution. Some Linux distributions may need it to be installed manually. Tkinter can be installed using the following:

    ```bash
    sudo apt-get install python3-tk
    ```

2. **Pillow**: Pillow is a Python Imaging Library that adds images to Tkinter windows.Pillow can be installed using pip:

    ```bash
    pip install Pillow
    ```

3. **ttk**: ttk is a submodule of Tkinter and is included with the standard Python distribution. No additional installation is required.


### Running the Application
After these dependencies are installed, the application can be run by executing the following command in the Terminal:|

    ```bash
    python mainapp.py
    ```

## User Guide 
When first using the app, users will need to create an account by pressing 'Register'. This will 
take them to a page that allows them to enter personal details and, upon entering all fields correctly, 
they will have an account with which they can 'Login' the next time they use the application. 

Following instructions on the screen will allow for ease of navigation, but each page is summarised below as well.
Profile Page: Click on the button labelled 'Profile' to access. This page allows you to view your personal details at a glance and make any changes. If you are unsure of your VO2 Max, please just enter a random number within this range and proceed as normal. Upon pressing 'Submit', if all the values for the fields are correct, the file storing your data will be updated. If there is one or more incorrect value, an error message will popup that details the field in which the error was. 

BMI Page: Click on the button labelled 'BMI Page' to access. Users are met with information about BMI, and a disclaimer. There is an image which demonstrates the ranges one may fall in, and what that means e.g. a BMI < 18.5 is underweight. Press the 'Calculate BMI' button and a pointer will appear that shows the range you are in, as well as a text that tells you your BMI. If in one task you have changed your profile information and want to see your new BMI, please press the button again and it should update automatically.

VO2 Max Page: Click on the button labelled 'VO2 Max Page to access. Your VO2 Max range (ie where you sit for your age and gender based on provided VO2 Max (the efficiency with which you can take in oxygen ranging roughly from 10-100)). 

Buttons: All buttons are labelled with their functionality, and the back buttons always take you to the previous page (which is either the Login Page or the Home Page).

Please enjoy using my project!
Kind regards,
Ananya Nivargi