#!/usr/bin/env python3 

import argparse
def options():
    parser = argparse.ArgumentParser(description='This program is used to find the average quality score at each position of a FASTQ file.')
    parser.add_argument('-f', '--file_name', metavar='', type=str, required=True, help = 'Select a file name')
    return parser.parse_args()

args = options()
file = args.file_name

import gzip
import numpy as np 
mean_lane1 = np.zeros(101)

def convert_phred(letter):
    """Converts a single character into a phred score"""
    letter = ord(letter) - 33  
    return(letter)

# finding the average quality score per position
with gzip.open(file, "rt") as fh:
    i = 1
    LN = 0
    for line in fh:
        position = 0
        line = line.strip("\n")
        if i % 4 == 0:

            while position < len(line):
                mean_lane1[position] += (convert_phred(line[position]))
                position += 1

        LN += 1 # this should be under the if loop to capture all quality lines, and then updating it. 
        i += 1
    mean_lane1 = mean_lane1 / (LN * 1/4)

print("BP", "Mean Q_Score")
x = 0
count = 1
for score in mean_lane1:
    print(count, score)
    x += 1
    count += 1