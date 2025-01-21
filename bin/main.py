# bin/main.py
import argparse
import os

from src.splitter import split_words_by_first_letter
from src.verify_words import verify_words
from src.summarize_first_words import summarize_first_words
from src.summarize_priority_diverse import summarize_priority_diverse_words

def main():
    parser = argparse.ArgumentParser(
        description="Utility for splitting a list of 5-letter words, verifying them, or creating summaries."
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Subcommand: split
    parser_split = subparsers.add_parser("split", help="Split words by first letter.")
    parser_split.add_argument("input_file", help="Path to an input file of words.")
    parser_split.add_argument("--output-dir", default="output", help="Directory to store split files.")

    # Subcommand: verify
    parser_verify = subparsers.add_parser("verify", help="Verify that output_dir matches the input_file.")
    parser_verify.add_argument("input_file", help="Path to original input file.")
    parser_verify.add_argument("--output-dir", default="output", help="Directory of the split files.")

    # Subcommand: summarize
    parser_summarize = subparsers.add_parser("summarize", help="Take the first word from each file.")
    parser_summarize.add_argument("--output-dir", default="output", help="Directory to summarize.")

    # Subcommand: priority-diverse
    parser_priority_diverse = subparsers.add_parser("priority-diverse",
        help="Pick the 'most diverse' word from each file, minimizing letter-position conflicts."
    )
    parser_priority_diverse.add_argument("--output-dir", default="output", help="Directory to process.")

    args = parser.parse_args()

    if args.command == "split":
        split_words_by_first_letter(args.input_file, args.output_dir)
        print(f"Words split into '{args.output_dir}'.")

    elif args.command == "verify":
        if not os.path.isdir(args.output_dir):
            print(f"Error: '{args.output_dir}' does not exist.")
            return
        verify_words(args.input_file, args.output_dir)

    elif args.command == "summarize":
        if not os.path.isdir(args.output_dir):
            print(f"Error: '{args.output_dir}' does not exist.")
            return
        summarize_first_words(args.output_dir)

    elif args.command == "priority-diverse":
        if not os.path.isdir(args.output_dir):
            print(f"Error: '{args.output_dir}' does not exist.")
            return
        summarize_priority_diverse_words(args.output_dir)

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
