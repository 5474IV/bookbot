def get_book_text(file_path):
        content  = ""
        with open(file_path) as f:
                content = f.read()

        return content

def count_book_words(text):
        words = text.split()
        return len(words)

def count_characters(text):
	count_dictionary = {}
	for char in text.lower():
		if count_dictionary.get(char) == None:
			count_dictionary[char] = 1
		else:
			count_dictionary[char] = count_dictionary[char] + 1
	return count_dictionary

def sort_on(items):
	return items["num"]

def sort_dictionary(count_dictionary):
	list_of_sorted_chars = []
	for char in count_dictionary:
		list_of_sorted_chars.append({"char": char, "num": count_dictionary[char]})
	list_of_sorted_chars.sort(reverse = True, key = sort_on)
	return list_of_sorted_chars
