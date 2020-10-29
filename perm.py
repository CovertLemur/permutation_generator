"""
TODO: permutation_generator needs to return a list to write it to a file.
TODO: clean up run() 
"""

import argparse
import string
from itertools import permutations

def args():
    parser = argparse.ArgumentParser(description='Script to make permutations of a string.')
    parser.add_argument('-l', '--string-length', metavar= '', type=int, help='The length of the strings to be generated.', required=True, dest="string_length")
    parser.add_argument('-o', '--output-file', metavar='', help='The file to output strings to.', dest="file_mode")
    parser.add_argument('-c', '--characters', metavar='', help='The characters you want permutated.', dest='custom_mode')
    args = parser.parse_args()
    return args

def permutation_generator(string, length):
    for perms in list(permutations(string, length)):
        print(''.join(perms))

def file_create():
    if args().file_mode:
        f = open(args().file_mode, "w")
        return f

def run():
    print(permutation_generator(args().custom_mode, int(args().string_length)))
    if args().custom_mode:
        print("1")
        if args().file_mode:
            print("2")
            print(args().file_mode)
            file_create().write(permutation_generator(args().custom_mode, int(args().string_length)))
        else:
            print("3")
            print(permutation_generator(args().custom_mode, int(args().string_length)))
    else:
        print("4")
        if args().file_mode:
            print("5")
            all_characters = string.ascii_letters + string.digits
            file_create().write(permutation_generator(all_characters, int(args().string_length)))
        else:
            print("6")
            print(permutation_generator(all_characters, int(args().string_length)))

if __name__ == "__main__": 
    run()