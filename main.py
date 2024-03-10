import app.io.input as input
import app.io.output as output

def main():
    console_input = input.read_text_from_console()
    builtin_input = input.read_from_file_builtin("./data/input/plain.txt")
    pandas_input = input.read_from_file_pandas("./data/input/pandas.csv")

    output.print_text_to_console(console_input)
    output.print_text_to_console(builtin_input)
    output.print_text_to_console(pandas_input.__str__())
    output.write_to_file_builtin("./data/output/plain.txt", builtin_input)
    output.write_to_file_builtin("./data/output/pandas.txt", pandas_input.__str__())


if __name__ == '__main__':
    main()