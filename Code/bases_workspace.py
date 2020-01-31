
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


if __name__ == '__main__':
    print(binary_to_decimal(101010))
