monthly_income = int(input("Enter your monthly income: "))
monthly_expense = int(input( "Enter your total monthly expenses: "))
monthly_savings = monthly_income - monthly_expense
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print("Projected savings after one year, with interest, is: $",int(projected_savings))