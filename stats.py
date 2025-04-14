# Turns the text file into a string
def get_book_text(file_path):
    with open(file_path) as file:
        text = file.read()
    return text

# Counts the number of words in the text
def count(file_path):
    text = get_book_text(file_path).split()
    return len(text)

# Counts the number of each letter/character in the text listed in amount
def letters(file_path):
    amount = {}
    text = get_book_text(file_path).lower()

    for char in text:
        if char.isalpha():
            if char in amount:
                amount[char] += 1
            else:
                amount[char] = 1         
    return amount

# Used for .sort()... it will sort the dictionary by the number of letters
def sort_on(dict):
    return dict['num']

# Turns the dictionary into a list of dictionaries
def letter_list(file_path):
    dict = letters(file_path)
    dict_list = []
    for key in dict:
        dict_list.append({"Key" : key, "num" : dict[key]})
    return dict_list

# Sorts the list of dictionaries by the number of letters and returns a list of strings
# with the letter and the number of times it appears
def sorted_letters(file_path):
    dict_list = letter_list(file_path)
    dict_list.sort(key=sort_on, reverse=True)
    values = []
    for dict in dict_list:
        values.append(f"{dict['Key']}: {dict['num']}")
    return values