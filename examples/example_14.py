# Example 14: Latin-English Dictionary
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
print("
".join(output))
