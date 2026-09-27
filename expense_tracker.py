expenses = []
amounts = []
dates = []
cats = []

print("Simple Expense Tracker")
print("Made by Bitan Deb")
print("Reg No: 26BHI10050")
print("VITarthi Python Essentials")
print("")
print("Starting the program now")

def menu():
    print("")
    print("What do you want to do")
    print("1 Add expense")
    print("2 See all expenses")
    print("3 Total spent")
    print("4 Save to file")
    print("5 Load from file")
    print("6 Exit program")
    print("")

def add():
    print("Ok enter details now")
    print("Please fill carefully")
    c = input("Category name: ")
    a = input("Amount spent: ")
    d = input("Date: ")
    print("You entered category as " + c)
    print("You entered amount as " + a)
    print("You entered date as " + d)
    if c == "":
        print("Category empty")
        print("Try again later")
        return
    if a == "":
        print("Amount empty")
        print("Try again later")
        return
    if d == "":
        print("Date empty")
        print("Try again later")
        return
    ok = 0
    try:
        num = float(a)
        ok = 1
    except:
        print("Amount not number")
        print("Please enter proper amount next time")
        ok = 0
    if ok == 1:
        expenses.append(c)
        cats.append(c)
        amounts.append(num)
        dates.append(d)
        print("Added ok")
        print("Category was " + c)
        print("Amount was " + str(num))
        print("Date was " + d)
        print("Now it is saved in list")
        print("You can view it from menu option 2")
    else:
        print("Not added because of error")
        print("Nothing changed in the list")

def show():
    print("Showing all expenses now")
    print("Please wait")
    n = len(expenses)
    if n == 0:
        print("List is empty")
        print("No expense found")
        print("Add something first using option 1")
        return
    print("Total items in list is " + str(n))
    print("Here they are one by one")
    x = 0
    while x < n:
        print("Item number " + str(x+1))
        print("Category = " + expenses[x])
        print("Amount = " + str(amounts[x]))
        print("Date = " + dates[x])
        print("---")
        x = x + 1
        if x < n:
            print("Next item below")
    print("Finished showing all")
    print("That was complete list")

def total():
    print("Calculating total now")
    print("Adding all amounts")
    n = len(amounts)
    if n == 0:
        print("Nothing to calculate")
        print("Total is 0")
        print("Add expenses first")
        return
    s = 0
    y = 0
    while y < n:
        s = s + amounts[y]
        y = y + 1
    print("Total spent is " + str(s))
    print("This is sum of all amounts")
    if s > 500:
        print("You spent more than 500")
    if s > 1000:
        print("You spent more than 1000")
    if s < 100:
        print("Spending is low")
    if s == 0:
        print("Zero spending")
    print("Calculation done")
    print("You can check again anytime")

def save():
    print("Saving to file")
    print("Writing data now")
    f = open("expenses.txt" , "w")
    n = len(expenses)
    if n == 0:
        print("Nothing to save")
        print("List is empty")
        f.close()
        return
    i = 0
    while i < n:
        one = expenses[i]
        two = str(amounts[i])
        three = dates[i]
        line = one + "," + two + "," + three
        f.write(line)
        f.write("\n")
        i = i + 1
    f.close()
    print("File saved")
    print("Name of file is expenses.txt")
    print("You can check it in the folder")
    print("Data is safe now")

def load():
    print("Trying to load file")
    print("Looking for expenses.txt")
    try:
        f = open("expenses.txt" , "r")
        data = f.readlines()
        f.close()
        expenses.clear()
        cats.clear()
        amounts.clear()
        dates.clear()
        count = 0
        for line in data:
            line = line.strip()
            if line != "":
                parts = line.split(",")
                if len(parts) == 3:
                    expenses.append(parts[0])
                    cats.append(parts[0])
                    amounts.append(float(parts[1]))
                    dates.append(parts[2])
                    count = count + 1
        print("Load complete")
        print("Number of items loaded is " + str(len(expenses)))
        print("Count was " + str(count))
    except:
        print("File not found or problem")
        print("Just start new")
        print("You can add expenses manually")

running = 1
while running == 1:
    menu()
    ch = input("Type your choice: ")
    print("You selected " + ch)
    if ch == "1":
        add()
    elif ch == "2":
        show()
    elif ch == "3":
        total()
    elif ch == "4":
        save()
    elif ch == "5":
        load()
    elif ch == "6":
        print("Closing now")
        print("Thank you for using")
        print("By Bitan Deb")
        print("Reg 26BHI10050")
        running = 0
    else:
        print("Wrong option")
        print("Only 1 to 6 allowed")
        print("Try once more")
        print("Please read the menu carefully")

print("Program ended")
print("Have a nice day")
