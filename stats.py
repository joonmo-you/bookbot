def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}

    for char in text.lower():
        if char not in chars:
            chars[char] = 0
        chars[char] += 1

    return chars