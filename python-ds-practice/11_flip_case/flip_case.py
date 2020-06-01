def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    # def flip(x):
    #     return x.lower() if x.isupper() else x.upper()
  
    # return phrase.replace((to_swap.lower() or to_swap.upper()), flip(to_swap))
    # result = ''
    # for char in phrase:
    #     if char.islower() and char == to_swap.lower():
    #         result += char.upper()
    #     elif char.isupper() and char == to_swap.upper():
    #         result += char.lower()
    #     else:
    #         result += char
    # return result

    return ''.join([char.swapcase() if char.lower() == to_swap.lower() else char for char in phrase])
