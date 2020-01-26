#!/usr/bin/env python
# -*- coding: utf-8 -*-

import beautifulsoup4
import selenium
import sys
import argparse

def main():
    """ Main program """
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file")
    parser.add_argument("output_file")
    parser.add_argument("no_duplicates", action="store_true")
    args = parser.parse_args

    return 0

if __name__ == "__main__":
    main()
