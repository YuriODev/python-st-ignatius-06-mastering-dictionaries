# Example 2: Character Count in String
# Read the input data
input_data = input("Enter a string: ")

# Create a dictionary to count the occurrences of each character
char_count = {}
for char in input_data:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

# Print the dictionary
print(char_count)
