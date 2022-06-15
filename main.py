#!/usr/bin/env python3

import os
import sys

# import local modules
import lang.cpp


def gen(lang: str, path: str):
    if lang == "cpp":
        cpp.handle_cpp(path)


def main():
    if sys.argv[1] == "cpp":
        try:
            gen("cpp", sys.argv[2])
        except IndexError:
            print("Project name not defined")

    elif sys.argv[1] == "python":
        raise NotImplementedError("python project management")
    elif sys.argv[1] == "rem":
        os.system(f"rm -rf {sys.argv[2]}")
        print("Done!")
    else:
        print("ERROR: The language binary is not installed on your PC or not in $PATH.\n")
        usage()
        exit(1)


def usage():
    print("USAGE: generate <lang> <path>")
    print("  lang - The language you want to work with. ")
    print("  path - The name of the project that you want to create. ")


if len(sys.argv) < 2:
    usage()
    print("No argumets provided! ")
    exit(1)


if __name__ == "__main__":
    main()
