import argparse
import os
from src.splitter import split_words_by_first_letter

def main():
    parser = argparse.ArgumentParser(description="Split 5-letter words into files by first letter.")
    parser.add_argument("input_file", help="Path to the input file containing words.")
    parser.add_argument("--output-dir", default="output", help="Directory to store the splitted files.")
    args = parser.parse_args()
    
    # Call the function
    split_words_by_first_letter(args.input_file, args.output_dir)
    print(f"Words have been split and saved to the '{args.output_dir}' directory.")

if __name__ == "__main__":
    main()
