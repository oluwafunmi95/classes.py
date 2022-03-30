#Employee ID
#First Name
#Last Name
#Basic Salary
#Allowance
#Pension scheme
#Tax
#Net Salary
#Print each variable

employeeId = "01032022"
firstName = "Oluwafunmilayo"
lastName = "Doxa"
basicSalary = 5000
allowance = 200
pensionScheme = 0.02*basicSalary
tax = 0.01*basicSalary
netSalary = basicSalary - (tax+pensionScheme) + (allowance)
print('Employee Id- ',employeeId)
print('First Name- ',firstName)
print('Last Name- ', lastName)
print('Basic Salary- ','$',basicSalary)
print('Tax- ','$',tax)
print('Allowance- ','$',allowance)
print('Net Salary- ','$',netSalary)