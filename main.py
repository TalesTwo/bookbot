from stats import get_word_count, get_character_count

# main function
def main():
    book = get_book_text("books/frankenstein.txt")
    word_count = get_word_count(book)
    character_counts = get_character_count(book)
    print(f"{word_count} words found in the document")
    print(character_counts)
    
# grabs the text from a file and returns it as a string
def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

main()