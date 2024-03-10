def print_text_to_console(text: str) -> None:
    """
    Prints given text to console

    Parameters:
        - text (str): Text to be printed
    """
    print(text)


def write_to_file_builtin(filepath: str, text: str) -> None:
    """
    Writes given text to file using built-in file handling

    Parameters:
        - filepath (str): Path to file where text will be written
        - text (str): Text to be written to file
    """
    with open(filepath, 'w') as file:
        file.write(text)
