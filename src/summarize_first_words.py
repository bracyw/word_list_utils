import argparse
import os

from src.splitter import split_words_by_first_letter
from src.verify_words import verify_words

def summarize_first_words(output_dir):
    """
    Reads each .txt file in output_dir, grabs the first line (word),
    and writes all those first words into a new file named 'summary_of_words'
    in that same directory.
    """
    summary_path = os.path.join(output_dir, "summary_of_words.txt")

    # Sort the files for a consistent ordering (optional)
    txt_files = sorted(
        f for f in os.listdir(output_dir) 
        if f.endswith(".txt") and os.path.isfile(os.path.join(output_dir, f))
    )

    with open(summary_path, "w", encoding="utf-8") as summary_file:
        for txt_file in txt_files:
            file_path = os.path.join(output_dir, txt_file)
            # Read only the first line
            with open(file_path, "r", encoding="utf-8") as f:
                first_line = f.readline().strip()
                if first_line:  # If there's a word in the first line
                    summary_file.write(first_line + "\n")

    print(f"Summary of first words saved to: {summary_path}")
