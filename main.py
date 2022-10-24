"""Python for Visual Effects.

Assignment #3 - String Methods

Let's work some research. Find 10 string methods and create 10 functions that 
include at least one unique string method.

Example (Don't use the `format` method for your assigment):

def get_fullname(name, lastname):
    return("{} {}".format(name, lastname))

    # Capitalize the first character of name
def get_capitalized_name(name):
    return name.capitalize()

# Check if string contains character returns 1 if exist -1 if not
def string_contains(string, char_to_search):
    return string.find(char_to_search)

# Count the number of times the word comes in string
def count_words(string, word_to_count):
    return string.count(word_to_count)

# Joins the elements of list with character
def join_list(list, character_to_join):
    return character_to_join.join(list)

# Converts String to upper case
def convert_uppercase(string):
    return string.upper()

# Converts String to lower case
def convert_lowercase(string):
    return string.lower()

# Replace words in String
def replace_words(string, word_to_replace, word_to_replace_with):
    return string.replace(word_to_replace, word_to_replace_with)

# Removes Spaces on Left Side of String
def remove_left_spaces(string):
    return string.lstrip()

# Removes Spaces on Right Side of String
def remove_right_spaces(string):
    return string.rstrip()

# Check if string is numeric
def check_numeric(string):
    return string.isnumeric()

print(get_capitalized_name("john"))
print(string_contains("John Doe", "oh"))
print(count_words("This is a book. We read book.", "book"))
print(join_list(["John", "Doe"], " "))
print(convert_uppercase("john"))
print(convert_lowercase("JOHN"))
print(replace_words("I like books", "books", "fruits"))
print(remove_left_spaces("    books"))
print(remove_right_spaces("books    "))
print(check_numeric("12345"))
    
Then print the call to the function to see the final result.

Make sure your code runs and work without error before pushing the code to GitHub.

Documentation: https://docs.python.org/3/library/stdtypes.html#string-methods

"""
