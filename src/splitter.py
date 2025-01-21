import string
import os

def split_words_by_first_letter(input_file, output_dir):
    """
    Reads a file of 5-letter, lowercase words (one per line),
    sorts them alphabetically, then splits them into 26 files (a-z)
    based on the first letter.
    """

    # Make sure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Read and filter valid words
    valid_words = []
    with open(input_file, "r", encoding="utf-8") as infile:
        for line in infile:
            word = line.strip()
            # Optional validation: 5 letters, all alpha, and lowercase
            if len(word) == 5 and word.isalpha() and word.islower():
                valid_words.append(word)
            else:
                print("❌ words in word list are either not 5 letters long, or alphabetic, or lower case, or all three. CHECK YOUR DAMN INPUT!")

    # Sort the words
    valid_words.sort()

    # Prepare output files (a-z)
    file_handles = {}
    for letter in string.ascii_lowercase:
        file_path = os.path.join(output_dir, f"{letter}.txt")
        file_handles[letter] = open(file_path, "w", encoding="utf-8")

    # Write each sorted word to the correct file
    for word in valid_words:
        first_letter = word[0]
        file_handles[first_letter].write(word + "\n")

    # Close all output files
    for handle in file_handles.values():
        handle.close()
