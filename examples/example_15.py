# Example 15: Language Knowledge
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
print("
".join(output))
