def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = get_words(text)
    chars = char_count(text)
    print(chars)

    print(words)

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

main()