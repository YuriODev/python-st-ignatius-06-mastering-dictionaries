# Example 7: Count Word Occurrences
# Read the input data
input_data = input("Enter a sequence of words: ")

# Split the input data into a list of words
words = input_data.split()

# Create a dictionary to store the occurrences of each word
word_counts = {}
result = []

# Count the occurrences of each word
for word in words:
    if word in word_counts:
        result.append(word_counts[word])
        word_counts[word] += 1
    else:
        result.append(0)
        word_counts[word] = 1

# Print the result
print(" ".join(map(str, result)))
