import pandas
from pandas import DataFrame

def read_text_from_console() -> str:
    """
    Reads text input from console

    Returns:
        str: Text entered by user
    """
    return input("Enter text: ")


def read_from_file_builtin(filepath: str) -> str:
    """
    Reads content from file using built-in capabilities

    Parameters:
        - filepath (str): Path to file to be read

    Returns:
        str: File content
    """
    with open(filepath, 'r') as file:
        return file.read()


def read_from_file_pandas(filepath: str) -> DataFrame:
    """
    Reads content from file using pandas library

    Parameters:
        - filepath (str): Path to file to be read

    Returns:
        DataFrame: DataFrame containing the file data
    """
    return pandas.read_csv(filepath)
