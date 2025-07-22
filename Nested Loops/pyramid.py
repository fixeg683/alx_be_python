# Define the height of the pyramid
rows = 5

# Initialize row counter
i = 1

# Outer loop for each row
while i <= rows:
    # Print spaces
    j = 1
    while j <= rows - i:
        print(" ", end="")
        j += 1

    # Print asterisks
    k = 1
    while k <= (2 * i - 1):
        print("*", end="")
        k += 1

    # Move to the next line after each row
    print()
    i += 1
