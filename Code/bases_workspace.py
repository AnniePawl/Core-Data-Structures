import string


def binary_to_decimal(binary):
    """Converts a binary number into a decimal"""
    reversed_binary = binary[::-1]    # i = correct power when reversed
    decimal = 0
    for i, value in enumerate(reversed_binary):
        if value == "0":
            continue  # ignore 0 because no value
        decimal += 2**i  # multiply 2 by i b/c index = power, add this value to decimal variable
    return decimal


def decimal_to_binary(decimal):
    binary_result = ''
    new_decimal = int(decimal)
    while new_decimal > 0:
        remainder = new_decimal % 2
        binary_result = str(remainder) + binary_result
        new_decimal = int(new_decimal / 2)
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
        hex_result = str(remainder) + hex_result
        decimal = int(decimal / 16)
    return hex_result


if __name__ == '__main__':
    # print(binary_to_decimal("101010"))
    print(decimal_to_binary(256))
    # print(hex_to_decimal("FF"))
    # print(decimal_to_hex(255))
