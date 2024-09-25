# Example 11: Most Frequent Word
# Read the input data
n = int(input("Enter the number of lines: "))

# Initialize a dictionary to store word frequencies
word_freq = {}

# Read the lines and count word frequencies
for _ in range(n):
    line = input().split()
    for word in line:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

# Find the word with the highest frequency
most_frequent_word = None
highest_frequency = -1

for word, frequency in word_freq.items():
    if frequency > highest_frequency or (frequency == highest_frequency and word < most_frequent_word):
        most_frequent_word = word
        highest_frequency = frequency

# Print the most frequent word
print(most_frequent_word)
