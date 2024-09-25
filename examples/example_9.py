# Example 9: Count Distinct Numbers
# Read the input data
input_data = input("Enter a list of integers separated by spaces: ")

# Split the input data into a list of integers
numbers = list(map(int, input_data.split()))

# Convert the list to a set to find unique numbers
unique_numbers = set(numbers)

# Print the number of unique numbers
print(len(unique_numbers))
