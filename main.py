from stats import words_in_book, count_chars, get_book_text, chars_dict_to_sorted_list
import sys

def main():
    if len(sys.argv) !=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    number_of_words = words_in_book(book_path)
    dictionary_characters = count_chars(text)
    char_list = chars_dict_to_sorted_list(dictionary_characters)
    
    # Printing The Frame
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {number_of_words} total words")
    print("--------- Character Count -------")
    
    # Printing The Enteries
    for char_dict in char_list:
        char = char_dict["char"]
        count = char_dict["num"]
        
        # Only Use Alphabetical Characters
        if char.isalpha():
            print(f"{char}: {count}")
    
    print("============= END ===============")

main()