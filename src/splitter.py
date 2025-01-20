import string
import os

def split_words_by_first_letter(input_file, output_dir):
    """
    Reads a file of 5-letter, lowercase words (one per line),
    and splits them into 26 files (a-z) based on the first letter.
    """
    
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Create a dictionary to hold the file handles for a-z
    file_handles = {}
    for letter in string.ascii_lowercase:
        file_path = os.path.join(output_dir, f"{letter}.txt")
        file_handles[letter] = open(file_path, "w", encoding="utf-8")
    
    # Read the input file and write each word to the correct output file
    with open(input_file, "r", encoding="utf-8") as infile:
        for line in infile:
            word = line.strip()
            # Optional validation checks
            if len(word) == 5 and word.isalpha() and word.islower():
                first_letter = word[0]
                if first_letter in file_handles:
                    file_handles[first_letter].write(word + "\n")
    
    # Close all the output files
    for letter in file_handles:
        file_handles[letter].close()
