def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_unique_characters(text):
    unique_characters = {}
    for char in text:
        lowered_char = char.lower()
        if lowered_char in unique_characters:
            unique_characters[lowered_char] += 1
        else:
            unique_characters[lowered_char] = 1
    return unique_characters

def chars_dict_to_sorted_list(char_count_dict):
    sorted_list = []
    for key, value in char_count_dict.items():
        if key.isalpha():  # Only include alphabetic characters
            new_dict = {"char": key, "num": value}
            sorted_list.append(new_dict)
    sorted_list.sort(key=lambda x: x["num"], reverse=True)
    return sorted_list