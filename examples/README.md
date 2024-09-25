# Examples 🏋️‍♂️

Here are some examples to get you started.

<details open>
<summary><b>Covered topics</b></summary>

| Topic Covered                                           | Code with explanations                            | Problem description | Video explanation (is coming) |   
| ------------------------------------------------------- | ------------------------------------------------- | ------------------- | ---------------- |
| Print Dictionary Elements                               | [Detailed code](./example_1.py)                   | [Problem description](#example-1-print-dictionary-elements) | [Video explanation](#) |
| Character Count in String                               | [Detailed code](./example_2.py)                   | [Problem description](#example-2-character-count-in-string) | [Video explanation](#) |
| Count Unique Values in List                              | [Detailed code](./example_3.py)                   | [Problem description](#example-3-count-unique-values-in-list) | [Video explanation](#) |
| Word Frequency Count                                     | [Detailed code](./example_4.py)                   | [Problem description](#example-4-word-frequency-count) | [Video explanation](#) |
| Find Synonym                                              | [Detailed code](./example_5.py)                   | [Problem description](#example-5-find-synonym) | [Video explanation](#) |
| Count Digits                                             | [Detailed code](./example_6.py)                   | [Problem description](#example-6-count-digits) | [Video explanation](#) |
| Count Word Occurrences                                    | [Detailed code](./example_7.py)                   | [Problem description](#example-7-count-word-occurrences) | [Video explanation](#) |
| Count Unique Words                                        | [Detailed code](./example_8.py)                   | [Problem description](#example-8-count-unique-words) | [Video explanation](#) |
| Count Distinct Numbers                                    | [Detailed code](./example_9.py)                   | [Problem description](#example-9-count-distinct-numbers) | [Video explanation](#) |
| Print Distinct Words                                       | [Detailed code](./example_10.py)                   | [Problem description](#example-10-print-distinct-words) | [Video explanation](#) |
| Most Frequent Word                                        | [Detailed code](./example_11.py)                   | [Problem description](#example-11-most-frequent-word) | [Video explanation](#) |
| Queen's Attack Range                                        | [Detailed code](./example_12.py)                   | [Problem description](#example-12-queens-attack-range) | [Video explanation](#) |
| Word Length Statistics                                    | [Detailed code](./example_13.py)                   | [Problem description](#example-13-word-length-statistics) | [Video explanation](#) |
| Latin-English Dictionary                                    | [Detailed code](./example_14.py)                   | [Problem description](#example-14-latin-english-dictionary) | [Video explanation](#) |
| Language Knowledge                                        | [Detailed code](./example_15.py)                   | [Problem description](#example-15-language-knowledge) | [Video explanation](#) |


<!-- 512 -->
## Example 1: Print Dictionary Elements

**Problem:** Print the elements of a dictionary where keys are numbers from `1` to `n` (both inclusive) and values are the squares of the keys. `n` is an integer input provided by the user.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 5      | {1: 1, 2: 4, 3: 9, 4: 16, 5: 25} |
| 2   | 3      | {1: 1, 2: 4, 3: 9} |
| 3   | 7      | {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49} |
| 4   | 1      | {1: 1} |

<details close>
<summary><b>Python Solution</b></summary>

```python
# Read the input data
n = int(input("Enter an integer: "))

# Generate the dictionary with keys from 1 to n and values as squares of keys
squares_dict = {i: i**2 for i in range(1, n + 1)}

# Print the dictionary
print(squares_dict)
```
</details>


<!-- 516 -->
## Example 2: Character Count in String

**Problem:** Write a program to create a dictionary from an input string to count the number of occurrences of each character.

| No. | Inputs                    | Outputs                                                          |
| --- | ------------------------- | ---------------------------------------------------------------- |
| 1   | Lorem ipsum dolor sit amet | {'L': 1, 'o': 3, 'r': 2, 'e': 2, 'm': 3, ' ': 4, 'i': 2, 'p': 1, 's': 2, 'u': 1, 'd': 1, 'l': 1, 't': 2, 'a': 1} |
| 2   | Hello World               | {'H': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'W': 1, 'r': 1, 'd': 1} |
| 3   | Python is fun             | {'P': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 2, ' ': 2, 'i': 1, 's': 1, 'f': 1, 'u': 1} |
| 4   | Data Science              | {'D': 1, 'a': 2, 't': 1, ' ': 1, 'S': 1, 'c': 2, 'i': 1, 'e': 2, 'n': 1} |

<details close>
<summary><b>Python Solution</b></summary>

```python
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
```
</details>

<!-- 536 -->
## Example 3: Count Unique Values in List

**Problem:** Given a list of integers, determine the number of unique values.

| No. | Inputs                | Outputs               |
| --- | --------------------- | --------------------- |
| 1   | 1 3 4 5 6 5 1 9       | 6                     |
| 2   | 2 2 2 2 2             | 1                     |
| 3   | 7 8 9 10 11           | 5                     |
| 4   | 3 1 4 1 5 9           | 5                     |

<details close>
<summary><b>Python Solution</b></summary>

```python
# Read the input data
input_data = input("Enter a string: ")

# Create a dictionary to count the occurrences of each character
char_count = {}
for char in input_data:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

# Print the number of elements
print(len(char_count))
```
</details>


<!-- 543 -->
## Example 4: Word Frequency Count

**Problem:** Write a program to count the frequency of words in the given sentence. The output should be in reverse alphanumeric order.

| No. | Inputs                               | Outputs                              |
| --- | ------------------------------------ | ------------------------------------ |
| 1   | The five boxing wizards jump quickly | wizards: 1<br>quickly: 1<br>jump: 1<br>five: 1<br>boxing: 1<br>The: 1 |
| 2   | She sells sea shells by the sea shore | shore: 1<br>shells: 1<br>the: 1<br>sea: 2<br>she: 1<br>sells: 1<br>by: 1 |
| 3   | Peter Piper picked a peck of pickled peppers | peppers: 1<br>pickled: 1<br>peck: 1<br>Piper: 1<br>picked: 1<br>Peter: 1<br>a: 1<br>of: 1 |
| 4   | A quick brown fox jumps over the lazy dog | the: 1<br>quick: 1<br>over: 1<br>lazy: 1<br>jumps: 1<br>fox: 1<br>dog: 1<br>brown: 1<br>A: 1 |

<details close>
<summary><b>Python Solution</b></summary>

```python
# Read the input data
input_data = input("Enter a sentence: ")

# Split the input data into a list of words
words = input_data.split()

# Create a dictionary to store the frequency of each word
word_freq = {}
for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

# Sort the dictionary by keys in reverse alphanumeric order
sorted_word_freq = sorted(word_freq.items(), key=lambda x: x[0], reverse=True)

# Print the result
for word, freq in sorted_word_freq:
    print(f"{word}: {freq}")
```
</details>

<!-- 558 -->
## Example 5: Find Synonym

**Problem:** Enter the number of words in the dictionary. The dictionary consists of pairs of words. Each word is a synonym of another word. All words in the dictionary are different. After entering the dictionary, another word is entered. Find its synonym.

| No. | Inputs                                 | Outputs  |
| --- | -------------------------------------- | -------- |
| 1   | 3<br>amazing extraordinary<br>beautiful magnificent<br>delicious savory<br>extraordinary | amazing |
| 2   | 2<br>happy joyful<br>sad gloomy<br>joyful | happy |
| 3   | 4<br>fast quick<br>smart intelligent<br>calm peaceful<br>quick | fast |
| 4   | 1<br>good fine<br>fine | good |

<details close>
<summary><b>Python Solution</b></summary>

```python
# Read the input data
n = int(input("Enter the number of word pairs: "))
dictionary = {}

for _ in range(n):
    pair = input().split()
    dictionary[pair[0]] = pair[1]
    dictionary[pair[1]] = pair[0]

word = input("Enter a word to find its synonym: ")
print(dictionary[word])
```
</details>

<!-- 559 -->
## Example 6: Count Digits

**Problem:** A sequence of numbers from `1` to `9` ending with zero is entered. In total, no more than `100000` numbers will be entered. Count the number of ones, twos, threes, etc. in this sequence and print the result. The output should always contain `9` numbers.

| No. | Inputs                           | Outputs          |
| --- | -------------------------------- | ---------------- |
| 1   | 1 1 4 1 5 8 6 3 5 1 0            | 4 0 1 1 2 1 0 1 0 |
| 2   | 2 2 2 2 3 3 3 0                  | 0 4 3 0 0 0 0 0 0 |
| 3   | 9 8 7 6 5 4 3 2 1 0              | 1 1 1 1 1 1 1 1 1 |
| 4   | 1 2 3 4 5 6 7 8 9 1 2 3 4 0      | 2 2 2 2 1 1 1 1 1 |

<details close>
<summary><b>Python Solution</b></summary>

```python
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
```
</details>



<!-- 563 -->
## Example 7: Count Word Occurrences

**Problem:** A text is entered in one line. For each word in the text, count the number of its occurrences before it.

| No. | Inputs                        | Outputs        |
| --- | ----------------------------- | -------------- |
| 1   | one two one two three two four three | 0 0 1 1 0 2 0 1 |
| 2   | hello world hello everyone    | 0 0 1 0        |
| 3   | good better best good better  | 0 0 0 1 1      |
| 4   | a a a a b b b b               | 0 1 2 3 0 1 2 3|

<details close>
<summary><b>Python Solution</b></summary>

```python
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
```
</details>

<!-- 575 -->
## Example 8: Count Unique Words

**Problem:** Given an integer `n` followed by `n` lines of text, print the number of unique words that appear in the text. A word is defined as a sequence of characters that does not contain spaces. Words are separated by one or more spaces or newline characters. Punctuation marks are part of the word in this definition.

| No. | Inputs                        | Outputs        |
| --- | ----------------------------- | -------------- |
| 1   | 3<br>A fool is a person who thinks he's smarter than me.<br>Yet wolves are more noble sheep, it is difficult for them to imagine their life without the latter. And the sheep?! It's shame to say!<br>Only when he left the chariot, everyone understood that it was a coachman. | 43 |
| 2   | 2<br>This is a test.<br>This is another test. | 5 |
| 3   | 4<br>The quick brown fox.<br>Jumps over the lazy dog.<br>The dog barked.<br>The fox ran away. | 11 |
| 4   | 1<br>Simple text with simple words. | 5 |

<details close>
<summary><b>Python Solution</b></summary>

```python
# Read the number of lines
n = int(input())

# Initialize a dictionary to store unique words
unique_words = {}

# String of punctuation characters
punctuation = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''

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
```
</details>

<!-- 576 -->
## Example 9: Count Distinct Numbers

**Problem:** Given a list of integers which may contain up to `100000` numbers, determine how many distinct numbers are in it.

| No. | Inputs                        | Outputs        |
| --- | ----------------------------- | -------------- |
| 1   | 2 5 7 7 9 0 3 4<br>3 3 4 4 5 1 | 7<br>4         |
| 2   | 1 2 2 3 3 4 4 5 5 6 6 7 7 8 8 9 | 9              |
| 3   | 10 10 20 20 30 30 40 40 50 50 60 60 70 70 80 80 90 90 100 | 10 |
| 4   | 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 | 1              |

<details close>
<summary><b>Python Solution</b></summary>

```python
# Read the input data
input_data = input("Enter a list of integers separated by spaces: ")

# Split the input data into a list of integers
numbers = list(map(int, input_data.split()))

# Convert the list to a set to find unique numbers
unique_numbers = set(numbers)

# Print the number of unique numbers
print(len(unique_numbers))
```
</details>


<!-- 577 -->
## Example 10: Print Unique Words

**Problem:** Given a sequence of words separated by commas, print the unique words in lexicographical order as in the output data.

| No. | Inputs          | Outputs      |
| --- | --------------- | ------------ |
| 1   | abc,abc,bac,aca | abc,aca,bac  |
| 2   | dog,cat,bat,dog | bat,cat,dog  |
| 3   | sun,moon,star,sun,moon | moon,star,sun |
| 4   | apple,banana,apple,orange | apple,banana,orange |

<details close>
<summary><b>Python Solution</b></summary>
    
```python
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
```
</details>


<!-- 587 -->
## Example 11: Most Frequent Word

**Problem:** The user inputs the following data: in the first line, the number of lines `n` is provided, followed by `n` lines of words. Print the word that occurs most frequently in the text. If there are several such words, print the word that appears earlier in alphabetical order.

| No. | Inputs                                      | Outputs   |
| --- | ------------------------------------------- | --------- |
| 1   | 3<br>editor detective baker scientist<br>singer teacher<br>teacher scientist | scientist |
| 2   | 2<br>apple banana apple<br>banana orange apple | apple    |
| 3   | 4<br>dog cat bird dog<br>fish dog cat<br>dog bird fish<br>cat bird fish | dog      |
| 4   | 3<br>red blue green red<br>blue green blue<br>green blue red | blue     |

<details close>
<summary><b>Python Solution</b></summary>

```python
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
```
</details>

<!-- 591 -->
## Example 12: Queen's Attack Range

**Problem:** A queen is placed on a chessboard. Mark the position of the queen on the board and all the squares it attacks. Mark the square where the queen stands with the letter `Q`, the squares it attacks with the symbol `*`, and fill the rest of the squares with dots. The program receives the coordinates of the queen on the chessboard in chess notation, i.e., in the form `e2`, where the first character indicates the column (letter from `a` to `h`, left to right), and the second character indicates the row (digit from `1` to `8`, bottom to top). Print the chessboard as shown in the output data.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | f3     | f3 pattern|
| 2   | d5     | d5 pattern|
| 3   | a1     | a1 pattern|
| 4   | h8     | h8 pattern|

**f3**
```
* . . . . * . .
. * . . . * . .
. . * . . * . .
. . . * . * . *
. . . . * * * .
* * * * * Q * *
. . . . * * * .
. . . * . * . *
```


**d5**
```
* . * . * . * .
. * * * * * * .
* * . * . * . *
. * . Q . * . .
* * . * . * . *
. * * * * * * .
* . * . * . * .
. * . * . * . *
```


**a1**
```
Q * * * * * * *
* * * * * * * *
* * * * * * * *
* * * * * * * *
* * * * * * * *
* * * * * * * *
* * * * * * * *
* * * * * * * *
```


**h8**
```
* * * * * * * Q
. * * * * * * *
* . * * * * * *
. * . * * * * *
* . * . * * * *
. * . * . * * *
* . * . * . * *
. * . * . * . *

```

<details close>
<summary><b>Python Solution</b></summary>

```python
# Read the input data
position = input("Enter the position of the queen (e.g., e2): ")

# Initialize the chessboard
board = [['.'] * 8 for _ in range(8)]

# Convert position to board indices
col = ord(position[0]) - ord('a')
row = 8 - int(position[1])

# Mark the queen's position
board[row][col] = 'Q'

# Mark the rows and columns
for i in range(8):
    if i != row:
        board[i][col] = '*'
    if i != col:
        board[row][i] = '*'

# Mark the diagonals
for i in range(1, 8):
    if row + i < 8 and col + i < 8:
        board[row + i][col + i] = '*'
    if row - i >= 0 and col - i >= 0:
        board[row - i][col - i] = '*'
    if row + i < 8 and col - i >= 0:
        board[row + i][col - i] = '*'
    if row - i >= 0 and col + i < 8:
        board[row - i][col + i] = '*'

# Print the chessboard
for row in board:
    print(" ".join(row))
```
</details>


<!-- 598 -->
## Example 13: Word Length Statistics

**Problem:** The program receives a line containing words separated by spaces. For each word in the text, count the number of times it appears before it. The output should be in reverse alphanumeric order.

| No. | Inputs                           | Outputs           |
| --- | -------------------------------- | ----------------- |
| 1   | Errors should never pass silently. | 4: 1<br>5: 1<br>6: 2<br>9: 1 |
| 2   | Practice makes perfect.         | 8: 1<br>7: 1<br>6: 1<br>5: 1 |
| 3   | To be or not to be, that is the question. | 10: 1<br>6: 1<br>5: 1<br>3: 1<br>2: 3 |
| 4   | Stay hungry, stay foolish.       | 8: 1<br>7: 1<br>5: 2          |

<details close>
<summary><b>Python Solution</b></summary>

```python
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
```
</details>

<!-- 599 -->
## Example 14: Latin-English Dictionary

**Problem:** The program receives a string containing an integer `n` - the number of English words in an English-Latin dictionary, followed by `n` translations of these words. Each entry is in a separate line containing the first English word, followed by a hyphen surrounded by spaces, and then a comma-separated list of translations of this English word in Latin. All words consist only of English letters. Translations are sorted lexicographically. The order of English words in the dictionary is also lexicographical. Print the corresponding Latin-English dictionary in the same format (number of words and their translations). Specifically, the first word in the line of words should be the lexicographically smallest translation of the Latin word, then the second in this order, and so on. The English words in each line should also be sorted lexicographically.

| No. | Inputs                                                               | Outputs                                                                     |
| --- | -------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| 1   | 3<br>apple - malum, pomum, popula<br>fruit - baca, bacca, popum<br>punishment - malum, multa | 7<br>baca - fruit<br>bacca - fruit<br>malum - apple, punishment<br>multa - punishment<br>pomum - apple<br>popula - apple<br>popum - fruit |
| 2   | 2<br>day - dies<br>night - nox, noctis | 3<br>dies - day<br>noctis - night<br>nox - night |
| 3   | 1<br>light - lux, lumen | 2<br>lumen - light<br>lux - light |
| 4   | 2<br>tree - arbor<br>flower - flos, flora | 3<br>arbor - tree<br>flos - flower<br>flora - flower |

<details close>
<summary><b>Python Solution</b></summary>

```python
# Read the number of entries
n = int(input())

# Initialize dictionaries
eng_to_lat = {}
lat_to_eng = {}

# Read each entry and populate dictionaries
for _ in range(n):
    line = input()
    eng_word, lat_words = line.split(" - ")
    lat_words = lat_words.split(", ")
    
    for lat_word in lat_words:
        if lat_word not in lat_to_eng:
            lat_to_eng[lat_word] = []
        lat_to_eng[lat_word].append(eng_word)

# Prepare the output
output = []
output.append(str(len(lat_to_eng)))

for lat_word in sorted(lat_to_eng.keys()):
    eng_words = ", ".join(sorted(lat_to_eng[lat_word]))
    output.append(f"{lat_word} - {eng_words}")

# Print the result
print("\n".join(output))
```
</details>


<!-- 601 -->
## Example 15: Language Knowledge

**Problem:** Each of `n` students in a school knows `m` languages. Determine which languages all students know and languages that at least one student knows. The first line of the input contains the number of students `n`. The next `n` lines contain the number of languages `m`, followed by `m` lines listing the languages known by the `i`-th student. The length of the language names does not exceed `1000` characters, and the number of different languages does not exceed `1000` (`1 ≤ n ≤ 1000`, `1 ≤ m ≤ 500`). In the first line, print the number of languages known by all students. From the second line, print the list of such languages. Then print the number of languages known by at least one student, followed by the list of such languages.

| No. | Inputs                                                           | Outputs                              |
| --- | ---------------------------------------------------------------- | ------------------------------------ |
| 1   | 3<br>3<br>Ukrainian<br>English<br>Polish<br>2<br>Ukrainian<br>English<br>1<br>English | 1<br>English<br>3<br>English<br>Polish<br>Ukrainian |
| 2   | 2<br>2<br>German<br>French<br>1<br>German | 1<br>German<br>2<br>French<br>German |
| 3   | 4<br>3<br>Spanish<br>English<br>Italian<br>3<br>Spanish<br>English<br>French<br>3<br>Spanish<br>English<br>German<br>2<br>Spanish<br>English | 1<br>Spanish<br>English<br>4<br>English<br>French<br>German<br>Italian<br>Spanish |
| 4   | 2<br>1<br>Japanese<br>1<br>Chinese | 0<br>2<br>Chinese<br>Japanese |

<details close>
<summary><b>Python Solution</b></summary>

```python
# Read the number of students
n = int(input())

# Initialize dictionaries to store language counts
language_count = {}
all_languages_set = set()

# Read the languages known by each student
for _ in range(n):
    m = int(input())
    languages = set(input().strip() for _ in range(m))
    
    # Update the counts of each language
    for language in languages:
        if language in language_count:
            language_count[language] += 1
        else:
            language_count[language] = 1
    
    # Update the set of all languages
    all_languages_set.update(languages)

# Determine the languages known by all students
known_by_all = {lang for lang, count in language_count.items() if count == n}

# Prepare the output
output = []
output.append(str(len(known_by_all)))
output.extend(sorted(known_by_all))
output.append(str(len(all_languages_set)))
output.extend(sorted(all_languages_set))

# Print the result
print("\n".join(output))
```
</details>




**Notes:** All the examples above are solved using Python. You can find the solutions in the [examples](../examples) folder. Covered with explanations and comments, these examples will help you understand the practical implementation of the concepts covered in this module. Python tests are also included to verify the correctness of the solutions.
