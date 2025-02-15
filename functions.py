def url_categorize(url):
    """
    Returns whether a URL represents a business, a non-profit, or another type of organization.
    
    Examples:
    >>> url_categorize("example.com")
    'business'
    >>> url_categorize("charity.org")
    'non-profit'
    >>> url_categorize("university.edu")
    'other'
    """
    url = url.lower()
    if url.endswith('com'):
        return 'business'
    elif url.endswith('org'):
        return 'non-profit'
    else:
        return 'other'

def is_palindrome(s):
    """
    Checks whether the given string is a palindrome or not.
    Ignores case, spaces, and punctuation.
    
    Examples:
    >>> is_palindrome("racecar")
    True
    >>> is_palindrome("A man a plan a canal Panama")
    True
    >>> is_palindrome("hello")
    False
    """
    import re
    s = re.sub(r'[^a-zA-Z0-9]', '', s.lower())  # Remove non-alphanumeric characters
    return s == s[::-1]

def digit_count(s):
    """
    Counts the number of digits in a string, ignoring non-digit characters.
    
    Examples:
    >>> digit_count("Hello123")
    3
    >>> digit_count("2024 is the year!")
    4
    >>> digit_count("No digits here!")
    0
    """
    return sum(c.isdigit() for c in s)

def dsmvwl(string):
    """
    Removes vowels from a string. 'Y' is not considered a vowel.
    
    Examples:
    >>> dsmvwl("Disemvowel this string!")
    'Dsmvwl ths strng!'
    >>> dsmvwl("Hello World!")
    'Hll Wrld!'
    """
    vowels = "aeiouAEIOU"
    return ''.join(c for c in string if c not in vowels)

def calculate(expr):
    """
    Evaluates a simple arithmetic expression.
    
    The expression must be in the format "operand1 operator operand2" where:
    - operands are one-digit integers
    - operator is one of: +, -, *, /, %
    
    Returns None if the expression is invalid or if division/modulo by zero occurs.
    
    Examples:
    >>> calculate("3 + 5")
    8
    >>> calculate("9 / 3")
    3.0
    >>> calculate("4 % 0")
    None
    """
    try:
        operand_1, operator, operand_2 = expr.split()
        number1, number2 = int(operand_1), int(operand_2)
        
        if operator == "+":
            return number1 + number2 
        elif operator == "-":
            return number1 - number2 
        elif operator == "*":
            return number1 * number2
        elif operator == "/":
            return None if number2 == 0 else number1 / number2 
        elif operator == "%":
            return None if number2 == 0 else number1 % number2 
    except (ValueError, ZeroDivisionError):
        return None
    return None