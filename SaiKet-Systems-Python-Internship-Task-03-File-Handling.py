"""
SaiKet Systems - Python Development Internship
Task 3: Basic File Handling

Description:
Reads data from a text file, performs find-and-replace operations on
specific words, and saves the modified content back to the file.
Includes exception handling for file-related errors.

Skills demonstrated: File Input/Output in Python, String Manipulation,
Exception Handling
"""

import os


def read_file(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied while reading '{filepath}'.")
    except Exception as e:
        print(f"Unexpected error while reading file: {e}")
    return None


def write_file(filepath, content):
    try:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Changes saved successfully to '{filepath}'.")
    except PermissionError:
        print(f"Error: Permission denied while writing to '{filepath}'.")
    except Exception as e:
        print(f"Unexpected error while writing file: {e}")


def find_and_replace(content, old_word, new_word):
    count = content.count(old_word)
    updated_content = content.replace(old_word, new_word)
    return updated_content, count


def create_sample_file_if_missing(filepath):
    """Creates a sample text file so the script can be tested immediately."""
    if not os.path.exists(filepath):
        sample_text = (
            "SaiKet Systems is a great place to learn Python.\n"
            "Python helps you build automation tools.\n"
            "Learning Python is fun and rewarding.\n"
        )
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(sample_text)
        print(f"Sample file '{filepath}' created for demonstration.\n")


def main():
    filepath = "sample.txt"
    create_sample_file_if_missing(filepath)

    print("===== BASIC FILE HANDLING TOOL =====")
    content = read_file(filepath)

    if content is None:
        return

    print("\nOriginal file content:\n" + "-" * 30)
    print(content)
    print("-" * 30)

    old_word = input("\nEnter the word you want to find: ").strip()
    new_word = input("Enter the word you want to replace it with: ").strip()

    if not old_word:
        print("Search word cannot be empty.")
        return

    updated_content, count = find_and_replace(content, old_word, new_word)

    if count == 0:
        print(f'\nNo occurrences of "{old_word}" were found. File left unchanged.')
        return

    print(f'\nFound {count} occurrence(s) of "{old_word}". Replacing with "{new_word}"...')
    write_file(filepath, updated_content)

    print("\nUpdated file content:\n" + "-" * 30)
    print(read_file(filepath))
    print("-" * 30)


if __name__ == "__main__":
    main()
