def add(first, second):
    """
    :param first: an integer
    :param second: an integer
    :returns: The sum of the two numbers
    """
    result = first + second
    return result


def power(number, exponent):
    """
    :param number: a positive integer
    :param exponent: a positive integer
    :returns: The power of the number to the exponent
    """
    if number < 0 or exponent < 0:
        raise TypeError
    else:
        result = number ** exponent
    return result
