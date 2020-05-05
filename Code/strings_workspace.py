text = "abra cadabra"
pattern = "abra"


def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""

    text_index = 0  # start at beginning of text
    if pattern == "":  # check if pattern contains anything
        return text_index

    # as long as there are still letters to look thru...
    while text_index != len(text)-1:
        for i in range(len(pattern)):
            if text_index + i < len(text):
                # check letter from text again letter from pattern
                if text[text_index + i] != pattern[i]:
                    break  # stop if no match
                if i == len(pattern) - 1:
                    return text_index  # return index where pattern starts
        text_index += 1  # move on to next letter in text


print(find_index(text, pattern))  # 0
print(find_index('abcd', 'cd'))  # 2
