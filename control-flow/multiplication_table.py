# multiplication_table.py
# A script to generate a multiplication table using a for loop

# Prompt the user for a number
try:
    number = int(input("Enter a number to see its multiplication table: "))

    # Generate and print the multiplication table from 1 to 10
    for i in range(1, 11):
        product = number * i
        print(f"{number} * {i} = {product}")

except ValueError:
    print("Invalid input. Please enter an integer.")