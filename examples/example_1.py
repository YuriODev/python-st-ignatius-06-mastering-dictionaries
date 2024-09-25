# Example 1: Print Dictionary Elements
# Read the input data
n = int(input("Enter an integer: "))

# Generate the dictionary with keys from 1 to n and values as squares of keys
squares_dict = {i: i**2 for i in range(1, n + 1)}

# Print the dictionary
print(squares_dict)
