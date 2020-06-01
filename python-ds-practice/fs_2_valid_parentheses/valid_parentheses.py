def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    # dic = {}
    # dic = {char : dic.get(char, 0) + 1 if char == "(" else dic.get(char, 0) - 1 for char in parens}
    # return dic

    # why can't this be done in one pass with a comprehension without using count. is there something similar to .this in python to reference the dictionary that is being constructed in real time?

    # return {char : parens.count(char) for char in parens}

    if parens.startswith(')'):
        return False

    return True if sum([+1 if char == '(' else -1 for char in parens]) == 0 else False


