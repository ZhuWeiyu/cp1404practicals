"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""
"""
function main()
    get number_of_months
    for month in range(1, number_of_months + 1):
        get income
        incomes.append(income)
    report_income(incomes, number_of_months)

function report_income(incomes, number_of_months)
    for month in range(1, number_of_months + 1):
        income = incomes[month - 1]
        total += income
        print month income total
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    number_of_months = int(input("How many months? "))

    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {month} : "))
        incomes.append(income)

    report_income(incomes, number_of_months)


def report_income(incomes, number_of_months):
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, number_of_months + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


main()