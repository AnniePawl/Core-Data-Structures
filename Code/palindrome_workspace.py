#!python


def is_palindrome_iterative(text):
    """is_palindrome_iterative return True if input text is a palindrome, and false if not"""
    # Start at either end of the word, work towards middle
    left_index = 0
    right_index = len(text)-1
    # Ensure middle hasn't been surpased
    while left_index <= right_index:
        if text[left_index] != text[right_index]:
            return False
        else:
            left_index += 1
            right_index -= 1
    return True


def is_palindrome_recursive(text, left=None, right=None):
    if left is None:
        left = 0
        right = len(text)-1
    if left >= right:
        return True
    if text[right] == text[left]:
        return is_palindrome_recursive(text, left + 1, right - 1)
    else:
        return False


print("Testing Iterative Function")
print(is_palindrome_iterative("anna"))  # True
print(is_palindrome_iterative("cow"))  # False
print(is_palindrome_iterative("racecar"))  # True
print(is_palindrome_iterative("butter"))  # False
print(is_palindrome_iterative(""))  # True
print("Testing Recursive Function")
print(is_palindrome_iterative("anna"))  # True
print(is_palindrome_iterative("cow"))  # False
print(is_palindrome_iterative("racecar"))  # True
print(is_palindrome_iterative("butter"))  # False
print(is_palindrome_iterative(""))  # True
