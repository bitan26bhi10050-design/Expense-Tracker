# Project Statement — Simple Expense Tracker

**Name:** Bitan Deb
**Reg No:** 26BHI10050
**Course:** VITarthi Python Essentials

## What this project is

For this assignment I built a small command line expense tracker in Python. The idea is pretty simple — you run the program, it gives you a menu, and from there you can add an expense, look at everything you've added so far, check how much you've spent in total, and save or load that data using a text file so it doesn't disappear when the program closes.

I kept things basic on purpose since this was meant to practice core Python — lists, loops, functions, file handling and basic input validation — rather than building something fancy with classes or a database.

## How it actually works

When you start the program it prints a short intro and then shows you a menu with six options: add an expense, view all expenses, see the total, save to a file, load from a file, or exit.

Under the hood I'm using four separate lists to hold the data — one for the expense names, one for amounts, one for dates, and one that duplicates the category names (a bit redundant, I know, but that's how it ended up after testing things out). Each time you add an expense it checks that none of the fields are left empty and that the amount you typed can actually be converted into a number. If something's wrong it tells you and just skips adding that entry instead of crashing.

The "show all expenses" option walks through the lists with a while loop and prints each entry one at a time, along with its position in the list. The total option just adds up everything in the amounts list and then prints a couple of extra lines depending on how much you've spent — like a small note if you've crossed 500 or 1000, or if your total is basically zero.

Saving writes everything out to a file called `expenses.txt`, with each expense on its own line as `category,amount,date`. Loading does the reverse — it reads that file back in, splits each line on the commas, and rebuilds the lists so you can carry on from where you left off. If the file isn't there yet, it just tells you and lets you keep going, it doesn't crash.

## A few honest notes

This isn't meant to be a polished production-ready app. There's no error message styling, no proper database, and the code repeats itself in a few places instead of being cleaned up — I left it that way since the point of the exercise was to get the logic working, not to make it look pretty. A few things I'd probably do differently if I revisited this later:

- Get rid of the duplicate `expenses` and `cats` lists since they hold the same thing
- Maybe switch to a list of dictionaries instead of four separate parallel lists
- Add an option to edit or delete an entry, since right now once something's added you're stuck with it
- Handle the file saving/loading with a proper `with open(...)` block instead of manually closing the file every time

## Files in this project

- `expense_tracker.py` — the actual program
- `expenses.txt` — gets created automatically once you save something, this is where the data lives between runs

That's about it. It runs, it does what it's supposed to, and I learned a fair bit about loops and file handling putting it together.
