#!/bin/bash

: '
Bash script to generate permutations from a string to an output file.
Current string is staticly set, with the regex values of [a-zA-Z0-9].

Can be modified to take an argument with specific string by
modifying the `str` variable to the third argument ($3).

	ex: str=$3

The character length is limited to 9, but can be modified
by adding additional regex to the case statement.

	ex: [1-9]|1[0-9]) break;;

CAUTION: Permutation lists get large incredibly quickly, take caution
when modifying the amount of allowable character length.

The script will output to a file. This can be output to the terminal
by modifying the last line of the script.

	ex: eval echo $bracestring | tr " " "\n"

CAUTION: Permutation lists can be very large, this might take a while.
'

# Initial string
#str="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
str="abc"
# Help menu and input handling
while :; do
    case $1 in
        -h|--help) echo "Usage: $(basename $0) [Character Length] [Output File]"; exit;;
        [1-9]) break;;
        *) echo "error: $1"; exit 1;;
    esac
done

char_length=$1
bracestring=$(printf "{$(echo "$str" | fold -w1 | paste -sd,)}%.0s" $(seq 1 $char_length))

eval echo $bracestring | tr " " "\n" > $2