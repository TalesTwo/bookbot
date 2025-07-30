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