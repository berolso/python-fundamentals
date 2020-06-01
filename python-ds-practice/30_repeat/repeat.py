def repeat(phrase, num):
    """Return phrase, repeated num times.

        >>> repeat('*', 3)
        '***'

        >>> repeat('abc', 2)
        'abcabc'

        >>> repeat('abc', 0)
        ''

    Ignore illegal values of num and return None:

        >>> repeat('abc', -1) is None
        True

        >>> repeat('abc', 'nope') is None
        True
    """

    if isinstance(num,int) and num >= 0:
        return ''.join([phrase for n in range(num)])
    else:
        return None


    # provided solution doesn't pass test
    
    # if not isinstance(num, int) or num < 1:
    #     return None
    # return phrase * num
