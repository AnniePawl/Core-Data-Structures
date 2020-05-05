#!python


def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    # Reference find_index function to confirm if pattern exists
    if find_index(text, pattern) != None:
        return True
    else:
        return False


def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

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
    while text_index != len(text):
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


def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    main()
