from stats import get_num_words, get_chars_dict

def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()


def main():
    filepath = "books/frankenstein.txt"
    text = get_book_text(filepath)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    print(f"{num_words} words found in the document")
    print(chars_dict)


main()