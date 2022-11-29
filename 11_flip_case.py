def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    swapped = []

    for char in phrase:
        if char.lower() == to_swap.lower():
            if char.islower():
                swapped.append(char.upper())
            else:
                swapped.append(char.lower())
        else:
            swapped.append(char)
    return "".join(swapped)

