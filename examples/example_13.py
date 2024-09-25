# Example 13: Word Length Statistics
# Read the input data
input_data = input("Enter a sequence of words separated by spaces: ")

# Split the input data into words
words = input_data.split()

# Count the frequency of each word length
length_counts = {}
for word in words:
    length = len(word)
    if length not in length_counts:
        length_counts[length] = 0
    length_counts[length] += 1

# Sort the lengths in ascending order
sorted_lengths = sorted(length_counts.keys())

# Print the statistics
for length in sorted_lengths:
    print(f"{length}: {length_counts[length]}")
