#!/usr/bin/env python3

import argparse

from gendiff.json_diff import generate_diff


def main():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("first_file", help="path to the first file")
    parser.add_argument("second_file", help="path to the second file")
    parser.add_argument("-f", "--format", help="set format of output")
    args = parser.parse_args()

    print("Comparing files:", args.first_file, args.second_file)

    file1_path = "file1.json"
    file2_path = "file2.json"

    diff = generate_diff(file1_path, file2_path)
    print(diff)


if __name__ == "__main__":
    main()


def some_foo(x):
    for i in x:
        if i == 0:
            x[-1] = i


e = [0, 1, 0, 2, 0, 4]
print(some_foo(e))
