def get_word_count(text):
    words = text.split()
    return len(words)

def get_character_count(text):
    lower_case_text = text.lower()
    letter_count = {}
    for letter in lower_case_text:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return letter_count

def sort_characters(letters):
    character_list = []
    for char in letters:
        if char.isalpha():
            character_list.append({"char": char, "num": letters[char]})
    character_list.sort(reverse=True, key=sort_on)
    return character_list
    
def sort_on(items):
    return items["num"]            