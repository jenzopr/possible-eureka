#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser(description='An example python script, ready for extensions.')
parser.add_argument('--jens', action = 'store_true')

args = parser.parse_args()

print("Hello, Loosolab and students and Rene!")

if(args.mario):
    print("Hello, Mario!")
