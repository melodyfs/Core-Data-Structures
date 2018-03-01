#!python

def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement contains here (iteratively and/or recursively)

    if find_index(text, pattern) != None:
        return True
    return False


def find_index(text, pattern, t_index=0, p_index=0):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_index here (iteratively and/or recursively)

    if pattern == '':
        return 0
    # all characters in pattern are found, return the index a match first occurs
    if (p_index == len(pattern)):
        return t_index - len(pattern)
    # reaches the end of text without matching any character
    if (t_index == len(text)):
        return None
    # one character is matched, try matching the next character
    if text[t_index] == pattern[p_index]:
        return find_index(text, pattern, t_index + 1, p_index + 1)
    # searching text and see if the first character in pattern matches a character in text
    if p_index == 0:
        return find_index(text, pattern, t_index + 1, 0)
    # pattern partially matches text (Failed), reset to try matching pattern[0] again
    else:
        return find_index(text, pattern, t_index - p_index + 1, 0)


def find_all_indexes(text, pattern, t_index=0, p_index=0, indexes=None):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_all_indexes here (iteratively and/or recursively)

    if indexes is None:
        indexes= []
    if pattern == '':
        if t_index >= len(text):
            return indexes
        indexes.append(t_index - len(pattern))
        return find_all_indexes(text, pattern, t_index + 1, 0, indexes)
    if p_index >= len(pattern):
        indexes.append(t_index - len(pattern))
        return find_all_indexes(text, pattern, t_index - len(pattern) + 1, 0, indexes)
    if t_index >= len(text):
        return indexes
    if text[t_index] == pattern[p_index]:
        return find_all_indexes(text, pattern, t_index + 1, p_index + 1, indexes)
    if p_index == 0:
        return find_all_indexes(text, pattern, t_index + 1, 0, indexes)
    else:
        return find_all_indexes(text, pattern, t_index, 0, indexes)


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
