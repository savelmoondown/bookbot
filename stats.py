def get_book_text(file_path):
    with open(file_path) as file:
        file_contents = file.read()
    return file_contents

def words_in_book(file_path):
    text_full = get_book_text(file_path)
    words = text_full.split()
    return len(words)

def count_chars(text):
    lower_case = text.lower()
    
    char_dict = {}
    
    for char in lower_case:
        if char in char_dict:
            char_dict[char] += 1
        else: 
            char_dict[char] = 1
    
    return char_dict

def chars_dict_to_sorted_list(char_dict):
    # Need a shell list
    char_list = []
    
    # Paired keys -> counting each
    for char, count in char_dict.items():
        # Formatting
        char_entry = {"char": char, "num": count}
        # Adding to list
        char_list.append(char_entry)
    
    # Sorting on the "num" value
    def sort_on(dict):
        return dict["num"]
    char_list.sort(reverse=True, key=sort_on)
    return char_list