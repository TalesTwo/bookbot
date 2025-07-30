from stats import get_word_count, get_character_count, sort_characters

# main function
def main():
    book = get_book_text("books/frankenstein.txt")
    word_count = get_word_count(book)
    character_counts = get_character_count(book)
    character_counts = sort_characters(character_counts)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("---------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for character in character_counts:
        print(f"{character["char"]}: {character["num"]}")
    print("============= END ===============")
    
# grabs the text from a file and returns it as a string
def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

main()