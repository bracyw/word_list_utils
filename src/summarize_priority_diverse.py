# src/summarize_priority_diverse.py

import os

def summarize_priority_diverse_words(output_dir):
    """
    From each .txt file in output_dir, select exactly ONE word that
    *minimizes* letter-position conflicts with the already chosen words.

    The chosen words are written into 'priority_diverse_summary_of_words'
    in the same output_dir.

    "Conflict" is defined as matching any letter at the same index.
    We do NOT skip a file if all words have conflicts; we just pick the
    word that has the fewest matching positions overall.
    """

    summary_path = os.path.join(output_dir, "diverse_sample_summary.txt")

    # Gather all .txt files
    txt_files = sorted(
        f for f in os.listdir(output_dir)
        if f.endswith(".txt") and os.path.isfile(os.path.join(output_dir, f))
    )

    chosen_words = []  # We'll pick exactly one word per file

    def conflict_count(word_a, word_b):
        """
        Returns how many positions match between word_a and word_b.
        e.g. conflict_count("abcde", "abzzz") = 2 (matches at index 0,1).
        """
        count = 0
        for i in range(min(len(word_a), len(word_b))):
            if word_a[i] == word_b[i]:
                count += 1
        return count

    for txt_file in txt_files:
        file_path = os.path.join(output_dir, txt_file)

        # Collect all valid words in the file
        file_words = []
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                candidate = line.strip()
                # Basic validation - adjust as needed for your use case
                if len(candidate) == 5 and candidate.isalpha() and candidate.islower():
                    file_words.append(candidate)

        if not file_words:
            print(f"⚠️  No valid 5-letter words found in {txt_file}. Skipping.")
            # (You could continue with next file or decide how to handle no valid words.)
            continue

        # For each candidate, calculate total conflict with the chosen set so far
        best_candidate = None
        best_conflict_score = None

        for candidate in file_words:
            # Sum up conflict counts with every chosen word
            total_conflict = 0
            for chosen in chosen_words:
                total_conflict += conflict_count(candidate, chosen)

            # We want the candidate with the LOWEST total_conflict
            if best_candidate is None or total_conflict < best_conflict_score:
                best_candidate = candidate
                best_conflict_score = total_conflict

        # "best_candidate" is the word with minimal conflict
        chosen_words.append(best_candidate)

    # Write all chosen words to file
    with open(summary_path, "w", encoding="utf-8") as outfile:
        for word in chosen_words:
            outfile.write(word + "\n")

    print(f"✅ Priority-diverse summary complete! {len(chosen_words)} words chosen.")
    print(f"File saved to: {summary_path}")
