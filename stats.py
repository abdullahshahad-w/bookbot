def word_count(book_content: str) -> int:
    return len(book_content.split())

def character_count(file_contents: str) -> dict[str, int]:
    count_dict = {}

    for char in file_contents:
        count_dict[char.lower()] = count_dict.get(char.lower(), 0) + 1

    return count_dict

def sort_helper(char_count: tuple[str, int]) -> int:
    return char_count[1]

def char_dict_to_sorted_list(char_dict: dict[str, int]) -> list[tuple[str, int]]:
    tup_list = []

    for key in char_dict:
        tup_list.append((key, char_dict[key]))

    sorted_list = sorted(tup_list, reverse=True, key=sort_helper)

    return sorted_list