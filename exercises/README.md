# Exercises 🏋️‍♂️

## Topics Covered:
- Dictionaries

<!-- 513 -->

## Exercise 1: Day of the Week Dictionary - Easy 😊 (Est. Time: 5-10 mins | Points: 10)

**Problem:** Create a dictionary where the keys are the names of the days of the week, and the values are integers representing the ordinal number of the day of the week from 0 to 6. Print the name of the day for the entered ordinal number. If the entered number is out of bounds, the program does not print any message or indicate an error.

### Input:
- An integer representing the ordinal number of the day.

### Output:
- The name of the day corresponding to the ordinal number, or no output if the number is out of bounds.

### Examples:

| No. | Inputs | Outputs   |
| --- | ------ | --------- |
| 1   | 3      | Wednesday |
| 2   | 0      | Sunday    |
| 3   | 5      | Friday    |
| 4   | 7      |           |

### Note:
This exercise tests the ability to use dictionaries for key-value mappings in Python.


<!-- 519 -->

## Exercise 2: Count Letters and Digits - Easy 😊 (Est. Time: 10 mins | Points: 10)

**Problem:** Write a program that takes a string of characters and calculates the number of letters and digits.

### Input:
- A string of characters.

### Output:
- The count of letters and digits in the format:
```
LETTERS {count}
DIGITS {count}
```

### Examples:

| No. | Inputs                                    | Outputs               |
| --- | ----------------------------------------- | --------------------- |
| 1   | Project Gutenberg offers over 59,000 free eBooks | LETTERS 36<br>DIGITS 5   |
| 2   | 123abc456def                              | LETTERS 6<br>DIGITS 6    |
| 3   | 9876543210                                | LETTERS 0<br>DIGITS 10   |
| 4   | abcdefghijklmnopqrstuvwxyz                | LETTERS 26<br>DIGITS 0   |

### Note:
This exercise tests the ability to work with strings and count specific character types in Python.

<!-- 520 -->

## Exercise 3: Count Upper and Lower Case Letters - Easy 😊 (Est. Time: 10 mins | Points: 10)

**Problem:** Write a program that takes a string of characters and calculates the number of uppercase and lowercase letters.

### Input:
- A string of characters.

### Output:
- The count of uppercase and lowercase letters in the format 
```
UPPER CASE {count}
LOWER CASE {count}
```

### Examples:

| No. | Inputs                                    | Outputs               |
| --- | ----------------------------------------- | --------------------- |
| 1   | The quick brown FOX jumps over a lazy DOG | UPPER CASE 7<br>LOWER CASE 26 |
| 2   | Hello World                               | UPPER CASE 2<br>LOWER CASE 8  |
| 3   | PYTHON programming                        | UPPER CASE 6<br>LOWER CASE 11 |
| 4   | ABCdefGHIjklMNO                           | UPPER CASE 9<br>LOWER CASE 6  |

### Note:
This exercise tests the ability to work with strings and count specific character cases in Python.

<!-- 522 -->

## Exercise 4: Character Frequency Count - Easy 😊 (Est. Time: 10 mins | Points: 10)

**Problem:** Write a program to count the frequency of each character in the given string.

### Input:
- A string of characters.

### Output:
- The frequency of each character in the format "character count", each on a new line.

### Examples:

| No. | Inputs | Outputs  |
| --- | ------ | -------- |
| 1   | google | g 2<br>o 2<br>l 1<br>e 1 |
| 2   | hello  | h 1<br>e 1<br>l 2<br>o 1 |
| 3   | python | p 1<br>y 1<br>t 1<br>h 1<br>o 1<br>n 1 |
| 4   | abcabc | a 2<br>b 2<br>c 2 |

### Note:
This exercise tests the ability to count the frequency of characters in a string in Python.

<!-- 527 -->

## Exercise 5: Morse Code Representation - Easy 😊 (Est. Time: 10 mins | Points: 10)

**Problem:** Use a dictionary to output the Morse code representation of the letter entered by the user. The program should handle both uppercase and lowercase letters.

### Input:
- A letter entered by the user.

### Output:
- The Morse code representation of the letter.

### Examples:

| No. | Inputs | Outputs  |
| --- | ------ | -------- |
| 1   | D      | -..      |
| 2   | f      | ..-.     |
| 3   | A      | .-       |
| 4   | z      | --..     |

### Note:
This exercise tests the ability to use dictionaries and handle character case in Python.


<!-- 531 -->

## Exercise 6: Date Range Check - Easy 😊 (Est. Time: 10 mins | Points: 10)

**Problem:** Given a month and year for two dates (e.g., 12.2014 and 6.2019), the user enters another date (month and year). Determine if the third date falls within the range from the first date to the second date inclusive. The program should output `YES` or `NO`.

### Input:
- A year and month for the third date.

### Output:
- `YES` if the third date falls within the range, `NO` otherwise.

### Examples:

| No. | Inputs  | Outputs |
| --- | ------- | ------- |
| 1   | 2018<br>5 | YES   |
| 2   | 2014<br>11 | NO  |
| 3   | 2019<br>7 | NO   |
| 4   | 2016<br>3 | YES  |

### Note:
This exercise tests the ability to compare dates in Python.

<!-- 535 -->

## Exercise 7: Remove Duplicates from List - Medium 🔥 (Est. Time: 10-15 mins | Points: 20)

**Problem:** Write a program to remove duplicates from a list of integers.

### Input:
- A list of integers entered in a single line.

### Output:
- The list of integers with duplicates removed, sorted in ascending order.

### Examples:

| No. | Inputs                | Outputs               |
| --- | --------------------- | --------------------- |
| 1   | 10 5 11 2 3 5 8 9 3 4 2 | 2 3 4 5 8 9 10 11     |
| 2   | 1 1 1 1 1 1             | 1                     |
| 3   | 5 4 3 2 1               | 1 2 3 4 5             |
| 4   | 2 2 3 3 4 4 5 5         | 2 3 4 5               |

### Note:
This exercise tests the ability to work with lists and remove duplicate elements in Python.

<!-- 544 -->

## Exercise 8: Count Character Occurrences - Medium 🔥 (Est. Time: 10-15 mins | Points: 20)

**Problem:** Write a program that counts and prints the number of occurrences of each character in the input string.

### Input:
- A string of characters.

### Output:
- The count of each character in the string, printed in the order of their first appearance.

### Examples:

| No. | Inputs        | Outputs            |
| --- | ------------- | ------------------ |
| 1   | abcabcdfghj   | a, 2<br>b, 2<br>c, 2<br>d, 1<br>f, 1<br>g, 1<br>h, 1<br>j, 1 |
| 2   | hello world   | h, 1<br>e, 1<br>l, 3<br>o, 2<br> , 1<br>w, 1<br>r, 1<br>d, 1 |
| 3   | aabbcc        | a, 2<br>b, 2<br>c, 2 |
| 4   | programming   | p, 1<br>r, 2<br>o, 1<br>g, 2<br>m, 2<br>a, 1<br>i, 1<br>n, 1 |

### Note:
This exercise tests the ability to count and print character occurrences in Python.


<!-- 549 -->

## Exercise 9: Count Previous Occurrences of Words - Medium 🔥 (Est. Time: 10-15 mins | Points: 20)

**Problem:** Given a line of text, a word is defined as a sequence of non-space characters that are contiguous. Words are separated by one or more spaces or end-of-line characters. For each word in this text, count how many times it has appeared before in this text.

### Input:
- A line of text.

### Output:
- For each word in the text, print how many times it has appeared before.

### Examples:

| No. | Inputs                                   | Outputs               |
| --- | ---------------------------------------- | --------------------- |
| 1   | var list set tuple list tuple tuple dict var | 0 0 0 0 1 1 2 0 1     |
| 2   | hello world hello hello world             | 0 0 1 2 1             |
| 3   | a b c a b c a b c                         | 0 0 0 1 1 1 2 2 2     |
| 4   | one two one two three two four three      | 0 0 1 1 0 2 0 1       |

### Note:
This exercise tests the ability to count the number of previous occurrences of words in a text in Python.


<!-- 556 -->

## Exercise 10: Find Synonym - Medium 🔥 (Est. Time: 10-15 mins | Points: 20)

**Problem:** Given a dictionary consisting of pairs of words. Each word is a synonym for the paired word. All words in the dictionary are different. For a given word, determine its synonym. The program receives the number of synonym pairs `n`. Then `n` lines follow, each line containing exactly two synonymous words. After that, one word is entered. The program should print the synonym for the given word.

### Input:
- An integer `n` representing the number of synonym pairs.
- `n` lines, each containing exactly two synonymous words.
- One word for which the synonym needs to be determined.

### Output:
- The synonym for the given word.

### Examples:

| No. | Inputs                     | Outputs  |
| --- | -------------------------- | -------- |
| 1   | 3<br>Solar Heliac<br>Day Daytime<br>Arrive Occur<br>Heliac | Solar    |
| 2   | 2<br>Happy Joyful<br>Sad Unhappy<br>Joyful | Happy    |
| 3   | 4<br>Big Large<br>Small Tiny<br>Fast Quick<br>Smart Intelligent<br>Quick | Fast |
| 4   | 1<br>Hot Warm<br>Warm | Hot |

### Note:
This exercise tests the ability to work with dictionaries and find corresponding pairs in Python.

<!-- 557 -->

## Exercise 11: Check for Previous Occurrences - Medium 🔥 (Est. Time: 10-15 mins | Points: 20)

**Problem:** Given a sequence of numbers in an input string separated by spaces, for each number print the word `YES` (in a separate line) if this number has occurred earlier in the sequence or `NO` if it has not occurred. Use a dictionary to store the values.

### Input:
- A sequence of numbers separated by spaces.

### Output:
- For each number, print `YES` if it has occurred earlier, otherwise print `NO`.

### Examples:

| No. | Inputs              | Outputs                         |
| --- | ------------------- | ------------------------------- |
| 1   | 4 6 1 8 4 9 0 1     | NO<br>NO<br>NO<br>NO<br>YES<br>NO<br>NO<br>YES |
| 2   | 3 3 4 5 6 7 4 8 9 0 | NO<br>YES<br>NO<br>NO<br>NO<br>NO<br>YES<br>NO<br>NO<br>NO |
| 3   | 1 2 3 4 5 1 2 3 4 5 | NO<br>NO<br>NO<br>NO<br>NO<br>YES<br>YES<br>YES<br>YES<br>YES |
| 4   | 5 6 7 8 9 5 6 7 8 9 | NO<br>NO<br>NO<br>NO<br>NO<br>YES<br>YES<br>YES<br>YES<br>YES |

### Note:
This exercise tests the ability to use dictionaries for tracking occurrences of numbers in Python.

<!-- 560 -->

## Exercise 12: Letter Frequency in English Text - Medium 🔥 (Est. Time: 10-15 mins | Points: 20)

**Problem:** Given a text in English. Besides English letters, it may contain spaces and punctuation marks. Print the information about how many of each letter is present in this text (print 26 numbers). Uppercase and lowercase letters are not distinguished.

### Input:
- A text in English.

### Output:
- 26 numbers representing the count of each letter from 'a' to 'z'.

### Examples:

| No. | Inputs          | Outputs                                  |
| --- | --------------- | ---------------------------------------- |
| 1   | Hello world!    | 0 0 0 1 1 0 0 1 0 0 0 3 0 0 2 0 0 1 0 0 0 0 1 0 0 0 |
| 2   | This is a test. | 1 0 0 0 1 0 0 1 2 0 0 0 0 0 0 0 0 3 3 0 0 0 0 0 0 0 |
| 3   | Python 3.9.1    | 0 0 0 0 0 0 0 1 0 0 0 0 0 0 1 1 0 1 0 1 0 0 0 0 1 0 |
| 4   | abcdefghijklmnopqrstuvwxyz | 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 |
| 5   | The quick brown fox jumps over the lazy dog. | 1 1 1 1 3 1 1 2 1 1 1 1 1 1 4 1 1 2 1 2 2 1 1 1 1 1 |

### Note:
This exercise tests the ability to count and print the frequency of letters in a given text, disregarding case differences.

<!-- 561 -->

## Exercise 12: Unit Conversion - Medium 🔥 (Est. Time: 10-15 mins | Points: 20)

**Problem:** Write a program that performs conversion from one unit of length measurement to another. The supported units are:

- Miles (1 mile = 1609 m)
- Yards (1 yard = 0.9144 m)
- Feet (1 foot = 30.48 cm)
- Inches (1 inch = 2.54 cm)
- Kilometers (1 km = 1000 m)
- Meters (m)
- Centimeters (1 cm = 0.01 m)
- Millimeters (1 mm = 0.001 m)

### Input:
- A string in the format `<number> <unit_from> in <unit_to>`.

### Output:
- The converted length.

### Examples:

| No. | Inputs                 | Outputs              |
| --- | ---------------------- | -------------------- |
| 1   | 1 mile in meters       | 1609.0               |
| 2   | 10 yards in meters     | 9.144                |
| 3   | 5 feet in centimeters  | 152.4                |
| 4   | 12 inches in centimeters | 30.48               |
| 5   | 3 kilometers in meters | 3000.0               |
| 6   | 50 centimeters in meters | 0.5               |
| 7   | 100 millimeters in meters | 0.1              |
| 8   | 2 kilometers in miles | 1.24274238           |
| 9   | 5000 meters in kilometers | 5.0              |
| 10  | 1 mile in inches       | 63360.0              |

### Note:
This exercise tests the ability to perform unit conversions and work with various length measurements.

<!-- 562 -->

## Exercise 13: Check Unique Numbers - Medium 🔥 (Est. Time: 10-15 mins | Points: 20)

**Problem:** Write a program that accepts a sequence of numbers and determines whether all numbers are distinct from each other or not. Do not use loops.

### Input:
- A sequence of numbers entered in a single line.

### Output:
- Print "duplicate list" if any numbers are repeated, otherwise print "is unique sequence".

### Examples:

| No. | Inputs                | Outputs             |
| --- | --------------------- | ------------------- |
| 1   | 1 4 5 0 2 4           | duplicate list      |
| 2   | 1 6 9 10              | is unique sequence  |
| 3   | 2 3 4 5 6 7 8 9 1 2   | duplicate list      |
| 4   | 0 1 2 3 4 5           | is unique sequence  |

### Note:
This exercise tests the ability to work with sets and unique elements in Python.

<!-- 564 -->

## Exercise 14: City to Country Mapping - Medium 🔥 (Est. Time: 10-15 mins | Points: 20)

**Problem:** Given `n` lines with abbreviated country names and full city names for each country, followed by `m` lines with city names, write a program that prints the abbreviated country name for each city.

### Input:
- First line: number of countries `n`
- Next `n` lines: abbreviated country name followed by city names
- Next line: number of cities `m`
- Next `m` lines: city names

### Output:
- Abbreviated country name for each city

### Examples:

| No. | Inputs                                                                                                                                                                | Outputs       |
| --- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| 1   | 5<br>UA Kyiv Zhytomyr Ternopil Dnipro<br>JP Tokyo Osaka Kyoto<br>CA Montreal Toronto Ottawa<br>USA Boston Pittsburgh Washington Seattle<br>UK London Edinburgh Cardiff Belfast<br>3<br>Seattle<br>London<br>Kyiv | USA<br>UK<br>UA |
| 2   | 3<br>IN Delhi Mumbai Bangalore<br>CN Beijing Shanghai Shenzhen<br>FR Paris Lyon Marseille<br>2<br>Paris<br>Beijing | FR<br>CN |
| 3   | 2<br>IT Rome Milan Naples<br>ES Madrid Barcelona Valencia<br>3<br>Madrid<br>Rome<br>Naples | ES<br>IT<br>IT |
| 4   | 4<br>AU Sydney Melbourne Brisbane<br>NZ Auckland Wellington Christchurch<br>BR Rio Sao Paulo Brasilia<br>AR Buenos Aires Cordoba Rosario<br>2<br>Sydney<br>Rio | AU<br>BR |

### Note:
This exercise tests the ability to work with dictionaries and look up values based on keys in Python.

<!-- 566 -->

## Exercise 15: Count Repeated Characters - Medium 🔥 (Est. Time: 10-15 mins | Points: 20)

**Problem:** Write a program to count the repeated characters in the given string.

### Input:
- A single line of text.

### Output:
- Each character and its count in the format: character count. Only characters that repeat should be included in the output.

### Examples:

| No. | Inputs                             | Outputs                           |
| --- | ---------------------------------- | --------------------------------- |
| 1   | the quick brown fox jumps over the lazy dog | t 2<br>h 2<br>e 3<br>  8<br>u 2<br>r 2<br>o 4 |
| 2   | hello world                        | l 3<br>o 2                        |
| 3   | aabbccdd                           | a 2<br>b 2<br>c 2<br>d 2          |
| 4   | python programming                 | p 2<br>r 2<br>o 2<br>m 2          |

### Note:
This exercise tests the ability to count characters and filter repeated ones in Python.

<!-- 572 -->

## Exercise 15: Football Match Summary Table - Hard 🥵 (Est. Time: 20-30 mins | Points: 40)

**Problem:** Write a program that accepts a list of football match results and outputs a summary table of all match results. The format of the input is as follows: the first line indicates the integer `n` - the number of completed games. After that, `n` lines follow, which record the results of the game in the following format: `team1;score1;team2;score2`. For a win, the team is awarded 3 points, for a loss - 0, for a draw - 1.

### Input:
- An integer `n` indicating the number of games.
- `n` lines with the match results in the format
```
team1;score1;team2;score2
```

### Output:
- A summary table of the results in the format: `Team: Total_Games Wins Draws Losses Total_Points`.

### Examples:

| No. | Inputs                                        | Outputs |
| --- | --------------------------------------------- | ------- |
| 1   | 3<br>TeamA;3;TeamB;1<br>TeamA;2;TeamC;2<br>TeamB;1;TeamC;2 | TeamA: 2 1 1 0 4<br>TeamB: 2 0 0 2 0<br>TeamC: 2 1 1 0 4 |
| 2   | 2<br>TeamX;1;TeamY;1<br>TeamX;0;TeamZ;3       | TeamX: 2 0 1 1 1<br>TeamY: 1 0 1 0 1<br>TeamZ: 1 1 0 0 3 |
| 3   | 1<br>Team1;2;Team2;2                          | Team1: 1 0 1 0 1<br>Team2: 1 0 1 0 1 |
| 4   | 4<br>Alpha;2;Beta;3<br>Gamma;1;Beta;1<br>Alpha;0;Gamma;0<br>Beta;2;Gamma;1 | Alpha: 2 0 1 1 1<br>Beta: 3 2 1 0 7<br>Gamma: 3 0 1 2 1 |

### Note:
This exercise tests the ability to process multiple inputs and generate a summary table based on conditions in Python.

<!-- 574 -->

## Exercise 16: Substitution Cipher Encryption/Decryption - Hard 🥵 (Est. Time: 20-30 mins | Points: 40)

**Problem:** Write a program that can encrypt and decrypt using a substitution cipher. The program takes two lines of equal length as input, with the first line containing the characters of the initial alphabet and the second line containing the characters of the final alphabet (substitution cipher). After that, a line that needs to be encrypted using the provided substitution cipher and another line that needs to be decrypted are given. For example, the program input is:

### Input:
- Two lines of equal length, with the first line being the initial alphabet and the second line being the substitution alphabet.
- A line to be encrypted.
- A line to be decrypted.

### Output:
- The encrypted line.
- The decrypted line.

### Examples:

| No. | Inputs                | Outputs               |
| --- | --------------------- | --------------------- |
| 1   | abcd<br>*d%#<br>abacabadaba<br>#*%*d*% | *d*%*d*#*d*<br>dacabac |
| 2   | abcdef<br>uvwxyz<br>abcabc<br>vuvwuv | uvwuvw<br>abcabc |
| 3   | xyz<br>abc<br>xyzxyz<br>abcabc | abcabc<br>xyzxyz |
| 4   | mnopqr<br>stuvwx<br>mnop<br>stuv | stuv<br>mnop |

### Note:
This exercise tests the ability to use substitution ciphers for both encryption and decryption in Python.

<!-- 574 -->

## Exercise 17: Substitution Cipher Encryption/Decryption - Hard 🥵 (Est. Time: 20-30 mins | Points: 40)

**Problem:** Write a program that can encrypt and decrypt using a substitution cipher. The program takes two lines of equal length as input, with the first line containing the characters of the initial alphabet and the second line containing the characters of the final alphabet (substitution cipher). After that, a line that needs to be encrypted using the provided substitution cipher and another line that needs to be decrypted are given.

### Input:
- Two lines of equal length, with the first line being the initial alphabet and the second line being the substitution alphabet.
- A line to be encrypted.
- A line to be decrypted.

### Output:
- The encrypted line.
- The decrypted line.

### Examples:

| No. | Inputs                | Outputs               |
| --- | --------------------- | --------------------- |
| 1   | abcd<br>*d%#<br>abacabadaba<br>#*%*d*% | *d*%*d*#*d*<br>dacabac |
| 2   | abcdef<br>uvwxyz<br>abcabc<br>vuvwuv | uvwuvw<br>abcabc |
| 3   | xyz<br>abc<br>xyzxyz<br>abcabc | abcabc<br>xyzxyz |
| 4   | mnopqr<br>stuvwx<br>mnop<br>stuv | stuv<br>mnop |

### Note:
This exercise tests the ability to use substitution ciphers for both encryption and decryption in Python.

<!-- 581 -->

## Exercise 18: Count Word Frequencies - Hard 🥵 (Est. Time: 20-30 mins | Points: 40)

**Problem:** Given a string of text where words are separated by spaces, print all the words that appear in the text and their frequencies as shown in the output data.

### Input:
- A string of text with words separated by spaces.

### Output:
- A list of tuples where each tuple contains a word and its frequency, sorted by the words.

### Examples:

| No. | Inputs                             | Outputs                                                   |
| --- | ---------------------------------- | --------------------------------------------------------- |
| 1   | one two three one four five seven ten seven one | ('one', 3) ('four', 1) ('seven', 2) ('ten', 1) ('three', 1) ('two', 1) ('five', 1) |
| 2   | apple orange apple banana          | ('apple', 2) ('banana', 1) ('orange', 1)                  |
| 3   | hello world hello python           | ('hello', 2) ('python', 1) ('world', 1)                   |
| 4   | cat dog cat bird                   | ('bird', 1) ('cat', 2) ('dog', 1)                         |

### Note:
This exercise tests the ability to count word frequencies and sort words in Python.

# Problems in Order of Difficulty According to ChatGPT

The exercises provided range from understanding conditional statements to implementing complex branching logic. Here's a summary of the exercises ordered by difficulty, starting with the easiest and moving to more challenging problems.

## Easy 😊
Total: 6

## Medium 🔥
Total: 8

## Hard 🥵
Total: 4

Each exercise is designed to challenge different aspects of problem-solving, from simple arithmetic to complex logical reasoning. The estimated completion time for the exercises ranges from 5 minutes for the simplest tasks to 25 minutes for the most complex ones. This gives an average expected time of approximately 10-15 minutes per exercise, depending on the student's prior knowledge and experience.


# Checking Your Score with Autograder 📝

GitHub Classroom's autograder provides immediate feedback on your exercises. Each exercise is worth points based on its complexity, with a total of `90` points available across all exercises. 

When you commit and push your solution, GitHub Actions will run tests on your code. If all tests for an exercise pass, you will be awarded the full points for that exercise. If some tests fail, partial points may be awarded. 

The workflow will run all tests, even if some fail. The total score will be shown in the workflow output as `points scored/total points available`. For example, if you see `10/90`, it means you've successfully completed the first problem worth `10` points.

Please note that the workflow will show as failed if any test fails, even if you've successfully solved some problems. Look for the points tally in the output to see your score.

Remember, practice makes perfect! If you don't pass all tests the first time, review your code, make improvements, and try again. You can push new changes as many times as you need.

# Running Your Code and Tests Locally 🖥️

To run your code and tests locally, you can use the following commands:

1. Run the code:
```bash
python exercises/exercise_1.py
```

2. Run the tests:

To run the tests for an exercise, you'll use the pytest framework. First, make sure you have pytest installed: 

```bash
pip install pytest
```

Then, you can run the tests for a specific exercise using the following command:

```bash
python -m unittest tests/test_exercise_1.py
```

And for more beautiful output, you can use:

```bash
pytest --color=yes -vv tests/test_exercise_1.py
```

or to run only failed test from a specific file:

```bash
pytest --color=yes --failed-first -x tests/test_exercise_1.py
```

Replace `exercise_1` with the exercise you're working on (e.g., `exercise_2`, `exercise_3`, etc.) and `test_exercise_1` with the corresponding test file.
