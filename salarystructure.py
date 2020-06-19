# Code to calculate the monthly PAYE of an employee

first_name = input('Enter first name of employee: ').title()
last_name = input('Enter last name of employee: ').title()

while True:
    try:
        gross_annual = int(input("What is the Gross Annual Income of employee? \nDo not include any symbols. Eg. 'NGN2,500,000' should be written as '2500000'\n"))
        break
    except:
        print ('\nEnter a valid Gross Annual Income.')
        continue

basic = 0.4 * gross_annual # Assuming 40% of annual salary is 'Basic'
housing = 0.3 * gross_annual # Assuming 30% of annual salary is 'Housing'
transport = 0.1 * gross_annual # Assuming 10% of annual salary is 'Transport'

relief = (gross_annual * 0.2) + 200000   # Consolidated Relief of N200,000 plus 20% of Gross Annual Income
pension = 0.08 * (basic + housing + transport)   # Assuming 8% pension

taxable_income = gross_annual - (relief + pension)

if taxable_income <= 300000:
    paye_annum = 0.07 * taxable_income   # 7% tax on first NGN300,000
elif taxable_income <= 600000:
    paye_annum = (0.07 * 300000) + (0.11*(taxable_income - 300000))  # 11% tax on next NGN300,000
elif taxable_income <= 1100000:
    paye_annum = (0.07 * 300000) + (0.11 * 300000) + (0.15*(taxable_income - 600000))   # 15% tax on next NGN500,000
elif taxable_income <= 1600000:
    paye_annum = (0.07 * 300000) + (0.11 * 300000) + (0.15 * 500000) + (0.19*(taxable_income - 1100000))    # 19% tax on next NGN500,000
elif taxable_income <= 3200000:
    paye_annum = (0.07 * 300000) + (0.11 * 300000) + (0.15 * 500000) + (0.19 * 500000) + (0.21*(taxable_income - 1600000))    # 21% tax on next NGN1,600,000
else:
    paye_annum = (0.07 * 300000) + (0.11 * 300000) + (0.15 * 500000) + (0.19 * 500000) + (0.21 * 1600000) + (0.24*(taxable_income - 3200000))    # 24% tax on remaining amount

paye_monthly = paye_annum / 12    # monthly PAYE

print('The monthly PAYE of {} {} is NGN{}.'.format(first_name, last_name, round(paye_monthly, 2)))
