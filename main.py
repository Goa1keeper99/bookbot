from stats import get_num_words
from stats import get_num_unique_characters
from stats import chars_dict_to_sorted_list

def get_book_text(book_path):
    with open(book_path, 'r', encoding='utf-8') as file:
        return file.read()

def main():
    #header
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)  # Read the file first
    
    # Get word count
    num_words = get_num_words(text)
    print(f"Found {num_words} total words")
    
    print("--------- Character Count -------")

    # Get character counts
    char_counts = get_num_unique_characters(text)  # Pass the text, not the path

    # Get sorted character list
    sorted_char_list = chars_dict_to_sorted_list(char_counts)
    for item in sorted_char_list:
        print(f"{item['char']}: {item['num']}")   
    
    print("============= END ===============")
    

main()