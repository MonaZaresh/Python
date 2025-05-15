import random

# Sample vocabulary for Entry Level 3
word_bank = {
    "hungry": "wanting food",
    "quick": "fast",
    "difficult": "not easy",
    "friendly": "kind and helpful",
    "large": "big"
}

# Shuffle and prepare options
words = list(word_bank.keys())
definitions = list(word_bank.values())
random.shuffle(definitions)

# Game loop
score = 0
for word in words:
    print(f"\nWhat is the meaning of: '{word}'")
    options = random.sample(definitions, 3)
    if word_bank[word] not in options:
        options[random.randint(0, 2)] = word_bank[word]  # Ensure correct answer is present
    random.shuffle(options)

    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    choice = input("Enter the number of the correct meaning: ")
    if options[int(choice) - 1] == word_bank[word]:
        print("✅ Correct!")
        score += 1
    else:
        print(f"❌ Wrong! The correct answer was: {word_bank[word]}")

print(f"\nYour score: {score}/{len(words)}")
