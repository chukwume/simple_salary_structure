first_name = input('Enter first name: ').title()
last_name = input('Enter last name: ').title()

while True:
    try:
        gross_annual = int(input("What is the Gross Annual Salary of employee? \nDo not include any symbols. Eg. 'NGN2,500,500' should be written as '2500000'\n"))
        break
    except:
        print ('Enter a valid Gross Annual Salary.')
        continue

basic = 0.39 * gross_annual # Assuming 39% of annual salary is 'Basic'
housing = 0.29 * gross_annual # Assuming 29% of annual salary is 'Housing'
transport = 0.1 * gross_annual # Assuming 10% of annual salary is 'Transport'

relief = (gross_annual * 0.2) + 200000 # Consolidated Relief of N200,000 plus 20% of Gross annual income
pension = 0.08 * (basic + housing + transport) # Assuming 8% pension

taxable_income = gross_annual - (relief + pension)

if taxable_income <= 300000:
    paye_annum = 0.07 * taxable_income
elif taxable_income <= 600000:
    paye_annum = (0.07 * 300000) + (0.11*(taxable_income - 300000))
elif taxable_income <= 1100000:
    paye_annum = (0.07 * 300000) + (0.11 * 300000) + (0.15*(taxable_income - 600000))
elif taxable_income <= 1600000:
    paye_annum = (0.07 * 300000) + (0.11 * 300000) + (0.15 * 500000) + (0.19*(taxable_income - 1100000))
elif taxable_income <= 3200000:
    paye_annum = (0.07 * 300000) + (0.11 * 300000) + (0.15 * 500000) + (0.19 * 500000) + (0.21*(taxable_income - 1600000))
else:
    paye_annum = (0.07 * 300000) + (0.11 * 300000) + (0.15 * 500000) + (0.19 * 500000) + (0.21 * 1600000) + (0.24*(taxable_income - 3200000))

yearly_net = gross_annual - paye_annum - pension
monthly_net = yearly_net / 12

print('Monthly and yearly salary of {} {} is NGN{} and NGN{} respectively.'.format(first_name, last_name, round(monthly_net,2), round(yearly_net,2)))
