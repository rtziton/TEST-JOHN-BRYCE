# comp.py
simp_module_called = False

def sum_of_digits(number):
    if not simp_module_called:
        raise Exception("Please call at least one function in simp module first.")
    return sum(int(digit) for digit in str(abs(number)))

# ... (rest of the code remains unchanged)

# simp.py
def add_numbers(x, y):
    global simp_module_called
    simp_module_called = True
    return x + y

def subtract_numbers(x, y):
    global simp_module_called
    simp_module_called = True
    return x - y

# ... (rest of the code remains unchanged)

# Example usage
from simp import add_numbers, subtract_numbers
from comp import sum_of_digits, is_palindrome

num1 = 10
num2 = 5

sum_result = add_numbers(num1, num2)
print(f"{num1} + {num2} = {sum_result}")

difference_result = subtract_numbers(num1, num2)
print(f"{num1} - {num2} = {difference_result}")

# Now calling functions from the "comp" module will not raise an exception
num = 365
result_sum_of_digits = sum_of_digits(num)
print(f"The sum of digits of {num} is: {result_sum_of_digits}")

num_palindrome = 323
result_is_palindrome = is_palindrome(num_palindrome)
print(f"{num_palindrome} is a palindrome: {result_is_palindrome}")
