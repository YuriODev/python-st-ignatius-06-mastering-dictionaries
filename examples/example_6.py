# Example 6: Count Digits
# Read the input data
input_data = input("Enter a sequence of numbers ending with zero: ")

# Split the input data into a list of numbers
numbers = list(map(int, input_data.split()))

# Initialize a list to store the count of each digit from 1 to 9
counts = [0] * 9

# Count the occurrences of each number
for number in numbers:
    if number != 0:
        counts[number - 1] += 1

# Print the result
print(" ".join(map(str, counts)))
