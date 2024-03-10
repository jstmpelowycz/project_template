def print_text_to_console(text):
    """
    Prints given text to console

    Parameters:
        - text (str): Text to be printed
    """
    print(text)


def write_to_file_builtin(filepath, text):
    """
    Writes given text to file using built-in file handling

    Parameters:
        - filepath (str): Path to file where text will be written
        - text (str): Text to be written to file
    """
    with open(filepath, 'w') as file:
        file.write(text)
