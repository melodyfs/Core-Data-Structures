#!python

import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace


def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)

    decimal = 0
    index = 0
    # Decode digits from binary (base 2)
    # if base == 2:
    #     for digit in reversed(digits):
    #         index += 1
    #         decimal += (2 ** (index - 1)) * int(digit)
    #
    # # Decode digits from hexadecimal (base 16)
    # if base == 16:
    #     for digit in reversed(digits):
    #         index += 1
    #         if digit.islower():
    #             decimal += (base ** (index - 1)) * (string.ascii_lowercase.index(digit) + 10)
    #             print(decimal)
    #         elif digit.isupper():
    #             decimal += (base ** (index - 1)) * (string.ascii_uppercase.index(digit) + 10)
    #         else:
    #             decimal += (base ** (index - 1)) * int(digit)


    # Decode digits from any base (2 up to 36)
    if base >= 2 or base <= 36:
        for digit in reversed(digits):
            index += 1
            if digit.islower():
                decimal += (base ** (index - 1)) * (string.ascii_lowercase.index(digit) + 10)
                print(decimal)
            elif digit.isupper():
                decimal += (base ** (index - 1)) * (string.ascii_uppercase.index(digit) + 10)
            else:
                decimal += (base ** (index - 1)) * int(digit)

    return decimal

def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)
    # Encode number in binary (base 2)
    encoded_num = ""
    remainder = 0

    # if base == 2:
    #     while number != 0:
    #         remainder = number % 2
    #         encoded_num += str(remainder)
    #         number = int(number/2)
    #
    # # Encode number in hexadecimal (base 16)
    # if base == 16:
    #     while number != 0:
    #         remainder = number % 16
    #         # print(remainder)
    #         if remainder >= 10:
    #             remainder = string.ascii_lowercase[remainder - 10]
    #             print(remainder)
    #         else:
    #             encoded_num += str(remainder)
    #             number = int(number/16)

    # Encode number in any base (2 up to 36)
    if base >= 2 or base <= 36:
        while number != 0:
            remainder = number % base
            if remainder >= 10:
                remainder = string.ascii_lowercase[remainder - 10]
            encoded_num += str(remainder)
            number = int(number/base)
    # print(encoded_num[::-1])
    return encoded_num[::-1]

def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)

    decimal = decode(digits, base1)
    # Convert digits from base 2 to base 16 (and vice versa)
    # base16 = encode(decimal, 16)
    # decimal2 = decode(base16, 16)
    # base2 = encode(decimal2, 2)

    # Convert digits from base 2 to base 10 (and vice versa)
    # base10 = encode(decimal, 10)
    # decimal3 = decode(base10, 10)
    # base2_2 = encode(decimal3, 2)

    # Convert digits from base 10 to base 16 (and vice versa)
    # base10_2 = encode(decimal, 16)
    # decimal4= decode(base10_2, 16)
    # base2_3 = encode(decimal4, 10)

    # Convert digits from any base to any base (2 up to 36)
    result = encode(decimal, base2)
    return result


def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    main()
