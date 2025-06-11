# Input sentence
sentence = "Today is Good Day"

# Step 1: Split sentence into words (assuming space-separated)
words = sentence.split()

# Step 2: List to store capitalized words
capital_words = []

# Step 3: Loop through each word
for word in words:
    # Check if the first character's ASCII value is between 65 and 90 (A-Z)
    if 65 <= ord(word[0]) <= 90:
        capital_words.append(word)

# Step 4: Print the result
print(capital_words)