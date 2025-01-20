# bin/main.py

import argparse
import os
import string

from src.splitter import split_words_by_first_letter

def verify_words(input_file, output_dir):
    """
    Verify that the words in output_dir match exactly the words in input_file.
    Assumes the output_dir contains files like 'a.txt', 'b.txt', etc.
    """

    # Read all words from input_file into a set
    with open(input_file, "r", encoding="utf-8") as f:
        input_words = set(line.strip() for line in f if line.strip())

    # Read all words from the files in output_dir into another set
    output_words = set()
    for letter in string.ascii_lowercase:
        path = os.path.join(output_dir, f"{letter}.txt")
        if os.path.isfile(path):
            with open(path, "r", encoding="utf-8") as of:
                for line in of:
                    word = line.strip()
                    if word:
                        output_words.add(word)

    # Compare the two sets
    if input_words == output_words:
        print("✅ The words in the output directory EXACTLY match the input file.")
    else:
        # If they differ, show what’s missing or extra
        missing_in_output = input_words - output_words
        extra_in_output = output_words - input_words

        if missing_in_output:
            print("❌ The following words are in the input file but not in the output directory:")
            for w in missing_in_output:
                print("  ", w)

        if extra_in_output:
            print("❌ The following words are in the output directory but not in the input file:")
            for w in extra_in_output:
                print("  ", w)

        print("Verification failed. The sets of words do not match.")