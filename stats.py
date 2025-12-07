def count_words(content):
    words = content.split()
    return len(words)

def count_characters(content):
    characters = list(content)
    tally = {}
    for char in characters:
        key = char.lower()
        if key in tally:
            tally[key] += 1
        else:
            tally[key] = 1
    return tally

def sorted_count(dict_chars):
    sorted_list = []
    for char in dict_chars:
        sorted_list.append({"char": char, "num": dict_chars[char]})
    return sorted_list