#!/usr/bin/env python3
# Author ID: bsundedo

def read_file_string(file_name):
    # Takes file_name as a string for a file name, returns its entire contents as a string
    try:
        with open(file_name, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "The file does not exist."

def read_file_list(file_name):
    # Takes file_name as a string for a file name,
    # returns its entire contents as a list of lines without new-line characters
    try:
        with open(file_name, 'r') as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return "The file does not exist."

def append_file_string(file_name, string_of_lines):
    # Takes two strings: the first is a file name, the second is data to append
    # Appends the data to the end of the file specified by file_name
    try:
        with open(file_name, 'a') as file:
            file.write(string_of_lines)
    except FileNotFoundError:
        return "The file does not exist."

def write_file_list(file_name, list_of_lines):
    # Takes a file name and a list of lines
    # Writes each line from the list to the file, each on a new line
    try:
        with open(file_name, 'w') as file:
            file.writelines([line + '\n' for line in list_of_lines])
    except FileNotFoundError:
        return "The file does not exist."

def copy_file_add_line_numbers(file_name_read, file_name_write):
    # Takes two file paths: the first to read from, the second to write to
    # Reads data from the first file and writes to the second, prepending line numbers to each line without a space after the colon
    try:
        with open(file_name_read, 'r') as read_file:
            lines = read_file.readlines()
        with open(file_name_write, 'w') as write_file:
            for index, line in enumerate(lines):
                # Remove space after colon to satisfy the specific output format requirement
                write_file.write(f"{index + 1}:{line}")
    except FileNotFoundError:
        return "The file does not exist."


if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']

    append_file_string(file1, string1)
    print("Contents of file1 after appending:")
    print(read_file_string(file1))
    
    write_file_list(file2, list1)
    print("Contents of file2 after writing list:")
    print(read_file_string(file2))
    
    copy_file_add_line_numbers(file2, file3)
    print("Contents of file3 after copying and adding line numbers:")
    print(read_file_string(file3))
