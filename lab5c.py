#!/usr/bin/env python3
# Author ID: [seneca_id]

def add(number1, number2):
    # Add two numbers together, attempt to convert them to integers, return the result, if error return string 'error: could not add numbers'
    try:
        return int(number1) + int(number2)
    except ValueError:
        return 'error: could not add numbers'

def read_file(filename):
    # Read a file, return a list of all lines, if error return string 'error: could not read file'
    try:
        with open(filename, 'r') as file:
            return file.readlines()
    except Exception as e:  # Catching any exception related to file access
        return 'error: could not read file'

if __name__ == '__main__':
    print(add(10,5))                        # should output 15
    print(add('10',5))                      # should output 15
    print(add('abc',5))                     # should output 'error: could not add numbers'
    print(read_file('seneca2.txt'))         # works if the file exists
    print(read_file('file10000.txt'))       # returns error message if the file does not exist
