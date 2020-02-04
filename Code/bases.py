#!python

import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace


def binary_to_decimal(binary):
    """Converts a binary number(str) into a decimal(int)"""
    reversed_binary = binary[::- 1]
    # i = corresponds to power of 2 when reversed
    decimal = 0  # keep track of sum
    for i, value in enumerate(reversed_binary):
        if value == "0":
            continue  # ignore 0 because no value
        decimal += 2**i  # multiply 2 by i b/c i = exponent
    return decimal


def decimal_to_binary(decimal):
    """Converts a decimal(int) into binary(str)"""
    binary_result = ''
    # new_decimal = int(decimal)
    while decimal > 0:
        remainder = decimal % 2
        binary_result = str(remainder) + binary_result
        decimal = int(decimal / 2)
    return binary_result


def hex_to_decimal(hex_val):
    """Converts hex value(str) to decimal(int)"""
    reversed_hex = hex_val[::-1]  # reverse so power(of 16) = index
    decimal = 0  # keep track of sum
    hex_conversion = string.hexdigits  # access letters a-f
    for i, value in enumerate(reversed_hex):  # index = power
        new_value = hex_conversion.index(value.lower())
        decimal += new_value * (16 ** i)
    return decimal


def decimal_to_hex(decimal):
    """Converts decimal(int) to hex value(str)"""
    hex_result = ''
    hex_conversion = string.hexdigits  # access letters a-f
    while decimal > 0:
        remainder = decimal % 16
        decimal = int(decimal / 16)
    return hex_result


def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)

    decoded_result = 0
    reversed_input = digits[::-1]

    for i, value in enumerate(reversed_input):
        hex_conversion = string.hexdigits
        converted_value = hex_conversion.index(value.lower())
        decoded_result += converted_value * (base ** i)
    return decoded_result


def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)

    encoded_result = ''
    while number > 0:
        remainder = number % base
        number = int(number/base)

        conversion = string.ascii_lowercase
        converted_value = conversion.index()
        encoded_result = converted_value
    return encoded_result


def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)

    number = decode(digits, base1)
    return encode(number, base2)

    # TODO: Convert digits from base 2 to base 16 (and vice versa)
    # ...
    # TODO: Convert digits from base 2 to base 10 (and vice versa)
    # ...
    # TODO: Convert digits from base 10 to base 16 (and vice versa)
    # ...
    # TODO: Convert digits from any base to any base (2 up to 36)
    # ...


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
        print('{} in base {} is {} in base {}'.format(
            digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    main()
    print('binary to decimal:')
    print(binary_to_decimal('101010'))
    print('decimal to binay:')
    print(decimal_to_binary(10))
    print('hex to decimal:')
    print(hex_to_decimal('FF'))
    print('decimal to hex:')
    print(decimal_to_hex(185))
    print("DECODE")
    print(decode('14414', 5))
    print(decode('1010', 2))
    print(decode('B9', 16))
    print("ENCODE")
    print(encode(10, 16))
