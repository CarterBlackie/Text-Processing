def url_categorize(url):
    """ Returns whether a url represents a business, a non-profit, or another type of organization. """
    url = url.lower()
    if url.endswith('com'):
        return 'business'
    elif url.endswith('org'):
        return 'non-profit'
    else:
        return 'other'

def is_palindrome(s):
    """ Checks whether the given string is palindrome or not. """
   

def digit_count(s):
    """ Counts the number of digits in a string. """
    

def dsmvwl(string):
    """ Disemvowels a string. """
    

def calculate(expr):
    """ Evaluates a simple arithmetic expression. """
    