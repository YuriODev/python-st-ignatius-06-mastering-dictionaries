# Example 8: Count Unique Words
# Read the number of lines
n = int(input())

# Initialize a dictionary to store unique words
unique_words = {}

# String of punctuation characters
punctuation = '!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'

# Read each line and add words to the dictionary
for _ in range(n):
    line = input()
    words = line.split()
    for word in words:
        # Remove punctuation from the word
        clean_w = ''.join(char for char in word if char not in punctuation)
        if clean_w:  # Ensure the cleaned word is not empty
            unique_words[clean_w] = True

# Print the number of unique words
print(len(unique_words))
