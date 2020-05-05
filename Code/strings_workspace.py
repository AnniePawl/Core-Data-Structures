text = "abra cadabra"
pattern = "abra"


def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""

    text_index = 0  # start at beginning of text
    if pattern == "":  # check if pattern contains anything
        return text_index

    # as long as there are still letters to look thru...
    while text_index != len(text):
        for i in range(len(pattern)):
            if text_index + i < len(text):
                # check letter from text again letter from pattern
                if text[text_index + i] != pattern[i]:
                    break  # stop if no match
                if i == len(pattern) - 1:
                    return text_index  # return index where pattern starts
        text_index += 1  # move on to next letter in text


def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    indexes = []  # keep track of all starting indexes

    text_index = 0
    # if pattern empty, append indexes for length of text
    if pattern == "":
        for i in range(len(text)):
            indexes.append(i)

    # as long as there are still letters to look thru...
    while text_index != len(text)-1:
        for i in range(len(pattern)):
            if text_index + i < len(text):
                # check letter from text again letter from pattern
                if text[text_index + i] != pattern[i]:
                    break  # stop if no match
                if i == len(pattern) - 1:
                    # return index where pattern starts
                    indexes.append(text_index)
        text_index += 1  # move on to next letter in text
    return indexes


print("Testing Find Index Function")
print(find_index(text, pattern))  # 0
print(find_index('abc', 'c'))  # 2
print(find_index('abcd', 'cd'))  # 2
print(find_index('banana', 'an'))  # 1
print(find_index('banana', 'gran'))  # None
print("Testing Find All Indexes Function")
print(find_all_indexes(text, pattern))  # [0, 8]
print(find_all_indexes('banana', 'an'))  # [1, 3]
print(find_all_indexes('banana', ''))  # [0,1,2,3,4,5]
