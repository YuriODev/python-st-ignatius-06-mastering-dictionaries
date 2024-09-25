# Example 10: Print Unique Words
# Read the input data
input_data = input("Enter a sequence of words separated by commas: ")

# Split the input data into a list of words
words = input_data.split(',')

# Initialize a dictionary to store unique words
unique_words = {}

# Add each word to the dictionary to ensure uniqueness
for word in words:
    unique_words[word.strip()] = True  # Using strip() to remove any surrounding whitespace

# Get the unique words as a list
unique_words_list = list(unique_words.keys())

# Sort the unique words in lexicographical order
sorted_unique_words = sorted(unique_words_list)

# Print the sorted unique words joined by commas
print(",".join(sorted_unique_words))
