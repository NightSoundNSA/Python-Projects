def convert_to_snake_case(pascal_or_camel_cased_string):
    """
    Converts a PascalCase or camelCase string into snake_case.
    """

    # Create a list where uppercase letters are converted to lowercase and prefixed with '_'
    # Lowercase letters remain unchanged.
    snake_cased_char_list = [
        '_' + char.lower() if char.isupper()  # Convert uppercase letters and add '_'
        else char  # Keep lowercase letters as they are
        for char in pascal_or_camel_cased_string  # Iterate through each character
    ]

    # Join the list into a string and remove leading underscore if present
    return ''.join(snake_cased_char_list).strip('_')

def main():
    """
    Runs the conversion function and prints the result.
    """
    print(convert_to_snake_case('IAmAPascalCasedString'))  # Example input

main()
