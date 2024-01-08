#comp
def sum_of_digits(number):
    """
    Calculates the sum of digits of a given number.

    Parameters:
    - number (int): The input number.

    Returns:
    int: The sum of digits of the input number.
    """
    return sum(int(digit) for digit in str(abs(number)))

# put var = num 
num = 365
result_sum_of_digits = sum_of_digits(num) #func for results 
print(f"The sum of digits of {num} is: {result_sum_of_digits}")

def is_palindrome(number):
    """
    Checks if a given number is a palindrome.

    Parameters:
    - number (int): The input number.

    Returns:
    bool: True if the number is a palindrome, False otherwise.
    """
    num_str = str(abs(number))
    return num_str == num_str[::-1]

# Example usage:
num_palindrome = 323 
result_is_palindrome = is_palindrome(num_palindrome)
print(f"{num_palindrome} is a palindrome: {result_is_palindrome}")
