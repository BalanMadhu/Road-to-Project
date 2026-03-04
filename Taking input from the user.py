# Taking input from the user
name = input("Enter your name: ")          # string input
age = int(input("Enter your age: "))       # integer input
height = float(input("Enter your height: "))  # float input
is_student = input("Are you a student? (yes/no): ")

# Converting yes/no to boolean
is_student = True if is_student.lower() == "yes" else False
# Output (printing values back to the user)
print("\n--- User Details ---")
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student:", is_student)

# Using formatted output
print(f"\nHello {name}, you are {age} years old and your height is {height} meters.")
