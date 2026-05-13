expenses = []

while True :

    amount = input("Enter expense or q to quit: ")

    if amount == "q":
        break

    expenses.append(int(amount))
    

print("Total Expense =", sum(expenses))
expenses.sort()
print("money you spend",expenses)
