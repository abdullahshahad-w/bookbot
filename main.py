import sys
from stats import word_count, character_count, char_dict_to_sorted_list

def get_book_text(file_path: str) -> str:
    with open(file_path) as f:
        return f.read()

def print_report(book_path: str, word_count: int, sorted_list: list[tuple[str, int]]) -> None:
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for tup in sorted_list:
        if tup[0].isalpha():
            print(f"{tup[0]}: {tup[1]}")

    print("============= END ===============")

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]

    file_contents = get_book_text(file_path)
    num_words = word_count(file_contents)
    count_dict = character_count(file_contents)
    sorted_list = char_dict_to_sorted_list(count_dict)

    print_report("books/frankenstein.txt", num_words, sorted_list)

main()