# Example 5: Find Synonym
# Read the input data
n = int(input("Enter the number of word pairs: "))
dictionary = {}

for _ in range(n):
    pair = input().split()
    dictionary[pair[0]] = pair[1]
    dictionary[pair[1]] = pair[0]

word = input("Enter a word to find its synonym: ")
print(dictionary[word])
