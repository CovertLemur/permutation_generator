# Permutation Generator

## Description

Bash script to generate permutations from a string to an output file.

## Usage

```
perm.sh [Character Length] [Output File]
```

## Prepending string

Currently no way within the script, but can be done after the fact with `sed`.

```
sed -i -e 's/^/prefix/' file
```

Or if you would like to create a new file:

```
sed -e 's/^/prefix/' file > file.new
```

## Appending string

Currently no way within the script, but can be done after the fact with `sed`.

```
sed -i -e 's/$/prefix/' file
```

Or if you would like to create a new file:

```
sed -e 's/$/prefix/' file > file.new
```


## Notes

Current string is staticly set, with the regex values of [a-zA-Z0-9].

Can be modified to take an argument with specific string by
modifying the `str` variable to the third argument ($3).

`ex: str=$3`

The character length is limited to 9, but can be modified
by adding additional regex to the case statement.

`ex: [1-9]|1[0-9]) break;;`

**CAUTION:** Permutation lists get large incredibly quickly, take caution
when modifying the amount of allowable character length.

The script will output to a file. This can be output to the terminal
by modifying the last line of the script.

`ex: eval echo $bracestring | tr " " "\n"`

**CAUTION:** Permutation lists can be very large, this might take a while.
