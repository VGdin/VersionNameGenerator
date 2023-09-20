#!/usr/bin/env python3

import argparse
import csv
import random
import string
import os

def main():
    first_letter: str 
    list_of_files:list 
    first_letter, list_of_files= parse_input()

    # Append random word from each file
    output: str = ''
    first: bool = True
    for file in list_of_files:
        random_word = get_random_word(first_letter=first_letter, list_of_words=parse_csv(file))

        # If no random word, do nothing
        if random_word == '':
            continue

        # Prepend with dash for every word, except first
        if first:
            first = False
        else:
            output += '-'

        output += random_word

    print(output)


def get_random_word(first_letter: str,
                    list_of_words: list):
    """
    Get a random word from a list of words.

    :param first_letter: Letter word should start with
    :return: String with random word
    """
    filered_list: list = list(filter(lambda word: word.startswith(first_letter), list_of_words))

    # If no words start with first letter, return nothing
    if len(filered_list) == 0:
        return ''
    
    return random.choice(filered_list)


def parse_input():
    """
    Parse input and return vars for creating name.

    :return: Tuple[str, list] params based on args
    """ 
    parser = argparse.ArgumentParser(
        prog='VersionNameGenerator',
        description='Generate a version name from provided files.',
        epilog='Example: ./main.py -s s --file example-words/verbs.txt example-words/animals.txt',
        add_help=True
    )
    parser.add_argument('-s', '--start-letter', 
                        help='Letter first word should start with. '
                             'If too many letters only use the first',
                        action='store')
    parser.add_argument('-f', '--files', 
                        help='File with words to use in generating name. '
                             'Can be used several times, picking random '
                             'word from each file in order specified.',
                             nargs='+',
                        action='store')
    args = parser.parse_args()

    # Set first letter
    first_letter: str
    if args.start_letter:
        if args.start_letter not in string.ascii_letters:
            raise ValueError('Input [' + args.start_letter + '] is not a letter.')
        first_letter = args.start_letter.lower()[0:1]
    else:
        first_letter = random.choice(string.ascii_lowercase)

    # Check files exist
    for file in args.files:
        if not os.path.isfile(file):
            raise ValueError('File [' + file + '] does not exist.')

    return first_letter, args.files


def parse_csv(path: str):
    """
    Parse a csv file into an array.

    :param path: path to the csv file
    :return: array with strings
    """ 
    arr = []
    with open(path, 'r') as fd:
        reader = csv.reader(fd, delimiter='\n')
        for row in reader:
            word: str = row[0].lower()
            arr.append(word)
    return arr


if __name__ == '__main__':
    main()