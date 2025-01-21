import argparse
import os

from src.splitter import split_words_by_first_letter
from src.verify_words import verify_words
from src.summarize_first_words import summarize_first_words

def main():
    parser = argparse.ArgumentParser(
        description="Utility for splitting a list of 5-letter words, verifying the split, or summarizing the first words."
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Subcommand: split
    parser_split = subparsers.add_parser("split", help="Split 5-letter words into files by first letter.")
    parser_split.add_argument("input_file", help="Path to the input file containing words.")
    parser_split.add_argument("--output-dir", default="output", help="Directory to store the split files.")

    # Subcommand: verify
    parser_verify = subparsers.add_parser("verify", help="Verify the words in the output directory match the input file.")
    parser_verify.add_argument("input_file", help="Path to the original input file.")
    parser_verify.add_argument("--output-dir", default="output", help="Directory to check the split files.")

    # Subcommand: summarize
    parser_summarize = subparsers.add_parser("summarize", help="Take the first word from each .txt file and create summary_of_words.")
    parser_summarize.add_argument("--output-dir", default="output", help="Directory from which to gather first words.")

    args = parser.parse_args()

    if args.command == "split":
        split_words_by_first_letter(args.input_file, args.output_dir)
        print(f"Words have been split and saved to '{args.output_dir}'.")
    elif args.command == "verify":
        if not os.path.isdir(args.output_dir):
            print(f"Error: The directory '{args.output_dir}' does not exist.")
            return
        verify_words(args.input_file, args.output_dir)
    elif args.command == "summarize":
        if not os.path.isdir(args.output_dir):
            print(f"Error: The directory '{args.output_dir}' does not exist.")
            return
        summarize_first_words(args.output_dir)
    else:
        # If no subcommand given, print help
        parser.print_help()


if __name__ == "__main__":
    main()
