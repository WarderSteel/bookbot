def get_num_words(text):
     word = text.split()
     num_of_words = len(word)
     return num_of_words

def num_char(text):
     char = {}
     file_contents = text.lower()
     for character in file_contents:
         if character.isalpha():
             char[character] = char.get(character, 0) + 1
     return char

def sort_on(d):
    return d["num"]

def get_char_list(char_counts_dict):
    char_list = []
    for char, count in char_counts_dict.items():
        if char.isalpha():
            char_list.append({"char": char, "num": count})
    char_list.sort(reverse=True, key=sort_on)
    return char_list
