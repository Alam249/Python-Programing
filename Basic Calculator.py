#1.1 Basic calculator with 2 numbers
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))

addition = a+b
sub = a-b
mul = a*b
div = a//b

print(f"Sum of a and b is: {addition}")
print(f"Subtraction of a and b is: {sub}")
print(f"Multiplication of a and b is: {mul}")
print(f"Division of a and b is: {div}")

#1.2 Calculate (x²+1)/(x²-1)
x = int(input())
result = (x*x+1)/(x*x-1)
print(result)

#1.3 length of a string

y = input("Enter a string: ")
print(len(y))

#1.4 Power

c = int(input("Enter the base number: "))
d = int(input("Enter the power number: "))

print(pow(c,d))