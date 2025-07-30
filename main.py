from stats import get_word_count, get_character_count, sort_characters
import sys

# main function
def main():
    # verifying input
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    # reading book and calculating data
    book = get_book_text(sys.argv[1])
    word_count = get_word_count(book)
    character_counts = get_character_count(book)
    character_counts = sort_characters(character_counts)
    # outputing report
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