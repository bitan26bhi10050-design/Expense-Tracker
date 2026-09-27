# Simple expense tracker

The expense tracker application written in simple python code to track expenses in the command line. Using this application, a user can add expenses, view the existing expenses, calculate the total expenses and store the expenses in a text file.

Author: Bitan Deb, Reg No: 26BHI10050, Course: VITarthi Python Essentials

## Features

Add expense: Using this option a user can add expenses by providing the details like category of expense, amount and the date of expense.
View all expense: By selecting this option, a user can view all the expenses that have been added so far.

Calculate total: This option helps to view the total amount of all the expenses.
Save to file: This option helps to save all the existing expenses in a file called 'expenses.txt'.

Load from file: By using this option, the data in the file can be loaded into the application.
Exit: This option exits the application.
## Requirements
Python 3.x (No external libraries are required for this application)
## Usage
Verify that python 3.x is installed in your system. Save the code in a file called 'expense_tracker.py'. Open the terminal in the same directory as the file and type 'python expense_tracker.py' to run the file. A command prompt will be opened, select from the options given below.
## What do you want to do

1 Add expense
2 See all expenses
3 Total spent
4 Save to file
5 Load from file
6 Exit program
When the program is started, it shows the following message.
The options 1-6 correspond to the following actions:
| Actions   | Options |
|----------------|--------|
| Add expense | 1  |
| See all expense| 2  |
| Total spent | 3  |
| Save to file | 4  |
| Load from file | 5  |
| Exit program | 6  |
By choosing 1, the user can add an expense. This option takes the category, amount and date of the expense as input and stores it in a list. The amount should be in integer or float value. Else, it will raise an error. The category and date cannot be empty.
When the option 2 is chosen, it prints all the expenses that have been stored in the list.
By choosing option 3, the sum of all the expenses is calculated and displayed.
Using option 4, all the expenses are saved in a file called 'expenses.txt' in the same directory as the application. For this application, the file is stored in comma separated values format.
The option 5 loads all the data that is present in the file into the application.
The option 6 closes the application.
## Notes
The expenses data is stored only in the application unless the option 4 is chosen. The data in the application will be lost if the application is closed without saving the data in a file.
When the user enters a wrong input for amount, the application will show an error and ask to resubmit the input.
The category, amount and date cannot be empty.
## Future Improvements
Adding options to search for a category, deleting an existing expense, saving the data in CSV files with headers and calculating the average expenses for a month or category.
