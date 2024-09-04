# Type all gray letters inside the quotes
gray_letters = ""

# For each letter type yellow letters lowercase & green letters uppercase
info = ["","","","",""]



word_list = []
invalid_words = []

with open("words.txt", "r") as words:
    for line in words:
        word_list.append(line.strip())

def remove_words():
    for word in invalid_words:
        if word in word_list:
            word_list.remove(word)



for letter in gray_letters:
    for word in word_list:
        if letter.lower() in word:
            invalid_words.append(word)
remove_words()

for letter in range(5):
    if len(info[letter]) < 1:
        continue

    for rule in info[letter]:
        for word in word_list:
            if rule == rule.upper():
                if word[letter] != rule.lower():
                    invalid_words.append(word)
            else:
                if word[letter] == rule.lower():
                    invalid_words.append(word)
                if rule.lower() not in word:
                    invalid_words.append(word)

    remove_words()

print(", ".join(word_list))