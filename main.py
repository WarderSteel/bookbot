import sys
from stats import get_num_words
from stats import num_char
from stats import get_char_list
from stats import sort_on

def get_book_text(file_path):
    try: 
       with open(file_path) as book:
           return book.read()
    except FileNotFoundError:
        print(f"Error: File not found at path: {file_path}")
        sys.exit(1)

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    book =  get_book_text(file_path) 
    num_of_words = get_num_words(book)
    char_counts_dict = num_char(book)
    ordered_list  = get_char_list(char_counts_dict)
    print("============= BOOKBOT ===========")
    print(f"Analyzing book found at {file_path}...")
    print("--------- Word Count ---------")
    print(f"Found {num_of_words} total words")
    print("--------- Character Count ------")
    for item in ordered_list:
        print(f"{item['char']}: {item['num']}")
    print("============== END ============")

main()



