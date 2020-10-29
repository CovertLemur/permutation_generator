import argparse
import string
import pathlib
from itertools import product

def permutation_generator(chars, repeat=None):
    return [''.join(perm) for perm in product(chars, repeat=repeat)]

def run(args):
    if args.custom_mode:
        permutations = permutation_generator(args.custom_mode, args.string_length)
    else:
        all_characters = string.ascii_letters + string.digits
        permutations = permutation_generator(all_characters, args.string_length)

    if args.file_mode:
        f_handle = pathlib.Path('./{}'.format(args.file_mode)).absolute()
        with f_handle.open("w") as output_file:
            for permutation in permutations:
                output_file.write('{}\n'.format(permutation))
    else:
        for permutation in permutations:
            print(permutation)

if __name__ == "__main__": 
    parser = argparse.ArgumentParser(description='Script to make permutations of a string.')
    parser.add_argument('-l', '--string-length', metavar= '', type=int, help='The length of the strings to be generated.', required=True, dest="string_length")
    parser.add_argument('-o', '--output-file', metavar='', help='The file to output strings to.', dest="file_mode")
    parser.add_argument('-c', '--characters', metavar='', help='The characters you want permutated.', dest='custom_mode')
    args = parser.parse_args()
    run(args)