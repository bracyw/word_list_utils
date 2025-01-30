import os
import hashlib
import sys
from collections import defaultdict
import csv

def hash_file(file_path, ignore_columns=None):
    """Returns a hash of the file contents, optionally ignoring specified columns."""
    hasher = hashlib.md5()
    rows = []
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        headers = next(reader)  # Read the header row
        ignore_indices = {i for i, col in enumerate(headers) if col in ignore_columns} if ignore_columns else set()

        hasher.update(','.join(headers[i] for i in range(len(headers)) if i not in ignore_indices).encode('utf-8'))

        for row in reader:
            filtered_row = [row[i] for i in range(len(row)) if i not in ignore_indices]
            hasher.update(','.join(filtered_row).encode('utf-8'))
            rows.append(row)
    
    return hasher.hexdigest(), os.path.getsize(file_path), headers, rows, ignore_indices

def compare_files(file_maps):
    """Compares file contents row by row for consistency and reports only the first mismatch."""
    for file_name in file_maps.keys():
        dumps = file_maps[file_name]
        ref_dump, reference = next(iter(dumps.items()))
        ref_hash, ref_size, ref_headers, ref_rows, ref_ignore_indices = reference

        for dump_name, file_info in dumps.items():
            if dump_name == ref_dump:
                continue
            cur_hash, cur_size, cur_headers, cur_rows, cur_ignore_indices = file_info

            if ref_hash != cur_hash:
                print(f"Mismatch detected in {file_name}: {dump_name} compared to {ref_dump}!")
                for row_idx in range(min(len(ref_rows), len(cur_rows))):
                    ref_row, cur_row = ref_rows[row_idx], cur_rows[row_idx]
                    for col_idx in range(min(len(ref_row), len(cur_row))):
                        if col_idx not in ref_ignore_indices and ref_row[col_idx] != cur_row[col_idx]:
                            print(f"First mismatch at Row {row_idx + 1}, Column '{ref_headers[col_idx]}': "
                                  f"'{ref_row[col_idx]}' (in {ref_dump}) vs '{cur_row[col_idx]}' (in {dump_name})")
                            return False
    return True

def collect_files(root_dir, ignore_columns=None):
    """Traverses the given directory and collects file contents for comparison."""
    file_maps = defaultdict(lambda: defaultdict(dict))
    for dump in sorted(os.listdir(root_dir)):
        dump_path = os.path.join(root_dir, dump)
        if not os.path.isdir(dump_path) or not dump.startswith("dump-"):
            continue

        # Track main run.csv and data_type.csv
        for key_file in ["run.csv", "data_type.csv"]:
            file_path = os.path.join(dump_path, key_file)
            if os.path.exists(file_path):
                file_maps[key_file][dump] = hash_file(file_path, ignore_columns)

        # Traverse data/ folder
        data_path = os.path.join(dump_path, "data")
        if os.path.exists(data_path):
            for file in sorted(os.listdir(data_path)):
                if file.startswith("run-") and file.endswith("-data.csv"):
                    file_path = os.path.join(data_path, file)
                    file_maps[file][dump] = hash_file(file_path, ignore_columns)
    
    return file_maps

def main():
    if len(sys.argv) < 2:
        print("Usage: python compare_csv_dumps.py <directory> [ignore_columns]")
        sys.exit(1)
    
    root_dir = sys.argv[1]
    ignore_columns = set(sys.argv[2:]) if len(sys.argv) > 2 else None
    file_maps = collect_files(root_dir, ignore_columns)
    
    for file_name in file_maps.keys():
        print(f"Checking {file_name} across dumps...")
        if not compare_files(file_maps):
            print(f"Inconsistency found in {file_name}! Check logs.")
            sys.exit(1)
    
    print("All files are consistent across dumps.")

if __name__ == "__main__":
    main()
