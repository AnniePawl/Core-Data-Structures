#!python


def factorial(n):
    """factorial(n) returns the product of the integers 1 through n for n >= 0,
    otherwise raises ValueError for n < 0 or non-integer n"""
    # check if n is negative or not an integer (invalid input)
    if not isinstance(n, int) or n < 0:
        raise ValueError('factorial is undefined for n = {}'.format(n))
    # implement factorial_iterative and factorial_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return factorial_iterative(n)
    # return factorial_recursive(n)


def factorial_iterative(n):
    """factorial_iterative(n) returns product of the integers 1 thru n """
    factorial = 1
    for i in range(n):
        # Multiply updated factorial by consecutive num until n is reached
        factorial = factorial * (i + 1)
    return factorial


def factorial_iterative1(n):
    factorial = 1
    for i in range(1, n+1):
        factorial = factorial * (i + 1)


def factorial_recursive(n):
    # Kind of like passing the buck / asking for help
    # 3! - 3*2*1 same as 3*2!
    # check if n is one of the base cases
    # base case stops recursion
    if n == 0 or n == 1:
        return 1
    # check if n is an integer larger than the base cases
    # Recurssive case
    elif n > 1:
        # call function recursively
        return n * factorial_recursive(n - 1)

# Is the number one?
# If so , return one
# If the number is more than one,
# return number * number- 1


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 1:
        num = int(args[0])
        result = factorial(num)
        print('factorial({}) => {}'.format(num, result))
    else:
        print('Usage: {} number'.format(sys.argv[0]))


if __name__ == '__main__':
    main()
    print(factorial_iterative(6))
    print(factorial_iterative(5))
