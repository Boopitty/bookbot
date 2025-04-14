from stats import get_book_text
from stats import count
from stats import sorted_letters
import sys

# The sys module allows the program to take a string as input.
# The string is the path to the book file.(ex. "books/frankenstein.txt")
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

# prints the entire text of the book
def main(file_path):
    book_text = get_book_text(file_path)
    print(book_text)
    return

# sys.argv is a list. [main.py, path_to_book]
# sys.argv is being called here to count the words in the chosen book.
print(f"Found {count(sys.argv[1])} total words")
# Prints the results of sorted_letters consecutively
for object in sorted_letters(sys.argv[1]):
    print(object)