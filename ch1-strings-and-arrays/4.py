"""
Palindrome Permutation: 
    Given a string, write a function to check if it is a permutation of a 
    palindrome. A palindrome is a word or phrase that is the same forwards 
    and backwards. A permutation is a rearrangement of letters. The 
    palindrome does not need to be limited to just dictionary words.
EXAMPLE
    Input: Tact Coa
    Output: True (permutations: "taco cat". "atco cta". etc.)
"""


def is_palindrome(s):
    """ Create a Freq Table. If we have more than one odd frequency,
        then it is not a palindrome. Otherwise it is!

        First note that any even number of characters will result in a 
        valid palindrome. i.e. 'aa' 'bb' 'cc' 'aabb' can all be valid 
        palindromes. 

        The problem, then, is focused on odd number of characters. If 
        we only have 1 character with an odd count and the others are even,
        then we can create a valid palindrome; otherwise we cannot.
        i.e. 'aabbcce' -> 'abcecba'    VALID
             'aaabbcc' -> 'abcacba'    VALID
             'abcc'    -> 'cabc'       INVALID
             'aaabbbcc' -> 'abcabcba'  INVALID


        Complexity: 
            Time: O(N)
            Space: O(N)
        
        ------------------------------------------------------------------
        There is also a Time Complexity Nlog(N) solution.
        Sort the string and keep track of whether we've seen a character
        with an odd count already. Once we encounter two characters with
        odd counts, we know we cannot create a valid palindrome.

        Since we are using a string, we cannot sort in-place which means 
        we must use N space.

        If the string is provided as an array instead, we can use no extra 
        space by using QuickSort to sort in-place. This leaves us with a:
            Time: Nlog(N)
            Space: 1
    """
    s = s.lower()
    freq_table = {}
    for c in s:
        if c == " ":
            continue

        if freq_table.get(c):
            freq_table[c] += 1
        else:
            freq_table[c] = 1

    num_odd_chars = 0
    for count in freq_table.values():
        if count % 2 != 0:
            num_odd_chars += 1
        if num_odd_chars > 1:
            return False

    return True


if __name__ == "__main__":
    assert is_palindrome("Tact Coa") == True
    assert is_palindrome("aba") == True
    assert is_palindrome("abba") == True
    assert is_palindrome("aaaccddee") == True
    assert is_palindrome("abccbaa") == True
    assert is_palindrome("abced decba") == True
    assert is_palindrome("aaabbb") == False
    assert is_palindrome("aaabbbccc") == False
    assert is_palindrome("this is a test") == False
