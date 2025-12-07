import sys
from stats import count_words, count_characters, sorted_count

def get_book_text(filepath):
    file_contents = ""
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents

def sort_on(items):
    return items["num"]

def print_report(list_report):
    for line in list_report:
        if not line["char"].isalpha():
            continue
        else:
            print(f"{line['char']}: {line['num']}")

def print_usage():
    print("Usage: python3 main.py <path_to_book>")

def main():
    if len(sys.argv) < 2:
        print_usage()
        sys.exit(1)

    content = get_book_text(sys.argv[1])
    num_words = count_words(content)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    num_chars = count_characters(content)
    sorted_chars = sorted_count(num_chars)
    sorted_chars.sort(reverse=True, key=sort_on)
    print_report(sorted_chars)

main()