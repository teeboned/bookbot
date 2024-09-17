def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = get_words(text)
    chars = char_count(text)
    print(f"--- Begin report of {book_path} ---\n{words} words found in the document\n\n")
    char_list = [{"name": key, "num": value} for key, value in chars.items()]
    char_list.sort(reverse=True, key=sort_chars)
    for entry in char_list:
        print(f"The '{entry['name']}' character was found {entry['num']} times")
    print(f"--- End Report ---")


def get_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def char_count(text):
    count={}
    lower_text = text.lower()
    for char in lower_text:
        if char.isalpha():
            if char not in count:
                count[char] = 1
            else:
                count[char] += 1
    return count

def sort_chars(chars):
    return chars["num"]


main()