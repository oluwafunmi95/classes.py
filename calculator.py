#the user enters any two number
#save two numbers in any two variables say x and y
#enter the specified operation
#check if operation is valid, how?
#if valid, perform operation on two numbers
#if not, throw a syntax error

a = int(input("Enter your number : "))

print(a)

b = int(input("Enter your number : "))

print(b)
4
operator = input("Select operator: ")

print(operator)
if operator== "+":
    add = a + b
    print(add)
elif operator== "-":
    diff = a - b
    print(diff)
elif operator== "*":
    product = a * b
    print(product)
else:
    division = a / b
    print(division)












# a,b =0,2
# while a<15:
#     print(a)
#     a,b = b, a+b

# z = 20*20
# print("The value of z is", z )

# a,b = 0,1
# while a<500:
#     print(a, end=',')
#     a, b = b, a+b
#     # print()