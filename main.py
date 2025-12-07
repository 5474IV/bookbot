import sys
from stats import get_book_text
from stats import count_book_words
from stats import count_characters
from stats import sort_dictionary

def main():
	if(len(sys.argv) != 2):
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)

	book = sys.argv[1]
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {book}...")
	print("----------- Word Count ----------")
	print(f"Found {count_book_words(get_book_text(book))} total words")
	character_dictionary = sort_dictionary(count_characters(get_book_text(book)))
	print("--------- Character Count -------")
	for dict in character_dictionary:
		if(dict["char"].isalpha()):
			print(f"{dict['char']}: {dict['num']}")
		else:
			continue
	print("============= END ===============")
main()
