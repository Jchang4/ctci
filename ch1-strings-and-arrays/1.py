# Is Unique: Implement an algorithm to determine if a string has all unique characters.
#
# What if you cannot use additional data structures?


def is_unique(s):
    """ Use a freq table to keep track of seen letters 
        Once we've seen a letter more than once, return False

        Time Complexity:
            O(N) where N is the length of the string
    """
    freq_table = {}
    for c in s:
        if freq_table.get(c):
            return False
        freq_table[c] = 1
    return True


def is_unique_no_extra_data_structures(s):
    """ We can sort the string and ensure the next character
        does not match the current one

        Time Complexity:
            Nlog(N) because we must sort the string using merge / quick sort
    """
    s = sorted(s)
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return False
    return True


if __name__ == "__main__":
    correct = ["abcd", "ldje", "laskjdf"]
    incorrect = ["aaaa", "fkdjf", "lalalala", "labwelabel"]

    for c in correct:
        if not is_unique(c):
            raise Exception(f"Incorrect solution for: {c}. Should be True.")

    for i in incorrect:
        if is_unique(i):
            raise Exception(f"Incorrect solution for: {i}. Should be False.")

    print("is_unique is correct!")

    for c in correct:
        if not is_unique_no_extra_data_structures(c):
            raise Exception(f"Incorrect solution for: {c}. Should be True.")

    for i in incorrect:
        if is_unique_no_extra_data_structures(i):
            raise Exception(f"Incorrect solution for: {i}. Should be False.")

    print("is_unique_no_extra_data_structures is correct!")
