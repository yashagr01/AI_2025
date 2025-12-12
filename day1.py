# 1. Print a Welcome Message  
print("Welcome to the AI Lab!")

print("\n------------------------------")



# 2. Input & Display Student Details  
name = input("Enter your name: ")
roll = input("Enter your roll number: ")
branch = input("Enter your branch: ")
print(f"Student Details → Name: {name}, Roll No: {roll}, Branch: {branch}")

print("\n------------------------------")



# 3. Simple Calculator  
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("Sum =", a + b)
print("Difference =", a - b)
print("Product =", a * b)
if b != 0:
    print("Quotient =", a / b)
else:
    print("Quotient = Division by zero not allowed")

print("\n------------------------------")



# 4. Temperature Converter (Celsius → Fahrenheit)  
c = float(input("Enter temperature in Celsius: "))
f = (9/5) * c + 32
print("Temperature in Fahrenheit =", f)

print("\n------------------------------")



# 5. Even or Odd Checker  
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(num, "is Even")
else:
    print(num, "is Odd")

print("\n------------------------------")



# 6. Largest of Three Numbers  
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
z = float(input("Enter third number: "))
print("Largest number is", max(x, y, z))

print("\n------------------------------")



# 7. Print First N Natural Numbers  
N = int(input("Enter a number N: "))
print("First", N, "natural numbers:")
for i in range(1, N + 1):
    print(i, end=" ")
print()

print("\n------------------------------")



# 8. Calculate Factorial  
n = int(input("Enter a number to find factorial: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
print("Factorial of", n, "=", fact)

print("\n------------------------------")



# 9. List Operations (5 numbers)  
numbers = []
print("Enter 5 numbers:")
for i in range(5):
    numbers.append(float(input(f"Number {i+1}: ")))

print("List =", numbers)
print("Smallest =", min(numbers))
print("Largest =", max(numbers))

print("\n------------------------------")



# 10. Prime Number Function  
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

p = int(input("Enter a number to check prime: "))
if is_prime(p):
    print(p, "is a Prime Number")
else:
    print(p, "is Not a Prime Number")

print("\n----- Program Completed Successfully -----")
