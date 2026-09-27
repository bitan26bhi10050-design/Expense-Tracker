# Project Report

**Title:** Simple Expense Tracker (Command Line, Python)
**Name:** Bitan Deb
**Registration Number:** 26BHI10050
**Course:** VITarthi Python Essentials

---

## 1. Introduction

Everyone ends up losing track of small daily expenses at some point — a snack here, a bus fare there, and by the end of the month you have no idea where the money actually went. For this project I wanted to build something simple that could at least keep a running record of that, without needing anything beyond core Python. So the goal was a basic expense tracker that runs in the terminal, lets you type in what you spent, and keeps that data around using a plain text file.

This report walks through why I built it the way I did, how it works, what I ran into while building it, and what I'd change if I had more time.

## 2. Objective

The main things I wanted the program to be able to do:

- Let the user add an expense with a category, an amount, and a date
- Show all the expenses that have been entered so far
- Add everything up and give a total
- Save the data to a file so it isn't lost when the program closes
- Load that saved data back in on the next run
- Do all of this through a simple numbered menu, since a beginner-level CLI tool doesn't really need anything more complicated than that

## 3. Tools Used

Nothing beyond the Python standard library. No pandas, no external file formats, no GUI. Just:

- Python 3
- Built-in `input()`, `open()`, lists, loops and functions
- A plain `.txt` file for storage

I kept it this way deliberately. Since the course is about Python essentials, I didn't want to lean on a library to do the work that loops and conditionals are supposed to teach.

## 4. How the Program is Structured

The program stores data using four parallel lists — one each for expense names, amounts, dates, and a second copy of the category list (which, looking back, is a bit redundant, but it's there because of how the logic grew while I was testing things).

There are six functions handling the core logic, each mapped to one menu option:

**`add()`** — asks the user for a category, amount, and date, checks none of them are blank, tries to convert the amount into a float, and only appends to the lists if everything checks out. If the amount isn't a valid number, it just tells the user and doesn't add anything, rather than crashing the program.

**`show()`** — loops through the lists with a `while` loop and prints each expense one at a time, along with its position in the list, so the output doesn't feel like a wall of text.

**`total()`** — adds up everything in the amounts list. I also added a few small conditional messages here, like flagging if the total crosses 500 or 1000, or noting if spending is unusually low or exactly zero, mainly just to make the output feel a little more responsive rather than a single flat number.

**`save()`** — opens `expenses.txt` in write mode and writes each expense as a single comma-separated line: category, amount, date.

**`load()`** — reads that file back in, splits each line on the commas, and rebuilds all four lists. It's wrapped in a `try/except` so that if the file doesn't exist yet (say, on a completely fresh run), the program doesn't crash — it just tells the user and lets them carry on.

The main part of the program is just a `while` loop that keeps showing the menu and calling the right function based on what number the user types, until they choose option 6 to exit.

## 5. Sample Run (Description)

On starting the program, it prints a short introduction along with my name and registration number, then shows the menu. Typing `1` walks you through entering a category, amount and date. Typing `2` afterward shows that entry back to you with its position number. Typing `3` gives the running total, and typing `4` writes everything to `expenses.txt` in the same folder the script is run from. Closing and reopening the program and choosing `5` reloads that same data, so the tracker effectively "remembers" expenses across sessions as long as you remember to save before quitting.

## 6. Challenges Faced

The trickiest part honestly wasn't the logic — it was making sure bad input didn't crash the whole thing. Early on, if someone typed letters into the amount field, the program would just throw an error and stop. Wrapping that conversion in a `try/except` and only adding the expense if it succeeded fixed that.

The other minor headache was file loading when the file doesn't exist yet. The first version of `load()` didn't handle that case at all, so running option 5 before ever saving anything would crash the program. Wrapping the whole thing in a `try/except` solved it, and now it just tells the user there's nothing to load yet.

## 7. Limitations

I'll be upfront that this isn't meant to be a "real" finance app, and there are a few rough edges:

- No way to edit or delete an expense once it's added — you're stuck with whatever you typed
- Data only exists in memory until you manually save it, so it's easy to lose an entry if you forget
- The `expenses` and `cats` lists store the exact same data, which is unnecessary and could be simplified to just one
- No categorised summaries (e.g., total spent on food vs. travel) — it only gives one grand total
- File handling uses manual `open()`/`close()` calls rather than a `with` block, which is a bit more error prone

## 8. Conclusion

Overall the project does what it set out to do — a working, no-frills expense tracker that can take input, do a bit of validation, calculate totals, and persist data between runs using a text file. It's not polished and there are clear places it could be improved, but building it helped reinforce how lists, loops, functions, and basic file I/O fit together in a real (if small) program, which was really the point of the exercise.

## 9. Files Submitted

- `expense_tracker.py` — the main program
- `expenses.txt` — generated automatically the first time an expense is saved
