# String Compression: Implement a method to perform basic string compression
# using the counts of repeated characters. For example, the string
# aabcccccaaa would become a2b1c5a3. If the "compressed" string would not
# become smaller than the original string, your method should return the
# original string. You can assume the string has only uppercase and lowercase
# letters (a - z).


def string_compression(s):
    """ For each char, compare to the prev char. If they are the same,
        increment a count. Once the current and prev char are different,
        we add them to a string with the count then reset the count to 1.

        Complexity:
            Time: N, this may take slightly longer because we are 
                rebuilding the string every time we add to it. This
                concern can be mitigated by using an array of len(s)
                and keeping track of the last index we added to.
            Space: N, to hold the compressed string
                    Since we early terminate in the for-loop,
                    we should never use more than N space.
    """
    if len(s) < 2:
        return s

    prev_char = s[0]
    count = 1
    compressed = ""

    for i in range(1, len(s)):
        if s[i] == prev_char:
            count += 1
        else:
            compressed += prev_char + str(count)
            prev_char = s[i]
            count = 1

        if len(compressed) > len(s):
            return s

    compressed += prev_char + str(count)
    return compressed if len(compressed) <= len(s) else s


if __name__ == "__main__":
    assert string_compression("aabcccccaaa") == "a2b1c5a3"
    assert string_compression("abcdef") == "abcdef"
    assert string_compression("aabcdef") == "aabcdef"
    assert string_compression("aabbccddeeff") == "a2b2c2d2e2f2"
    assert string_compression("aaaaaaaaaaaabcdef") == "a12b1c1d1e1f1"
    assert string_compression("aaabbbbbbbbbb") == "a3b10"
