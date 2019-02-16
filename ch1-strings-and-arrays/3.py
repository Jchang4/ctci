# URLify: Write a method to replace all spaces in a string with '%20: You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given the "true" length of the string. (Note: If implementing in Java, please use a character array so that you can perform this operation in place.)


def urlify(s, trueLen):
    """ Keep two pointers - the current index and the current "true index"
        Whenever we encounter a space, the next three slots become ['%', '2', '0']
        For example:
            "Mr John Smith    "
                         ^ true index
                             ^ current index
        Time Complexity: 
            O(N)
    """
    s = list(s)
    i = len(s) - 1
    t = trueLen - 1
    while i >= 0:
        if s[t] == " ":
            s[i] = "0"
            s[i - 1] = "2"
            s[i - 2] = "%"
            i -= 3
        else:
            s[i] = s[t]
            i -= 1
        t -= 1
    return "".join(s)


if __name__ == "__main__":
    print(urlify("Mr John Smith    ", 13))
    print(urlify("Hello world how are you        ", 23))
