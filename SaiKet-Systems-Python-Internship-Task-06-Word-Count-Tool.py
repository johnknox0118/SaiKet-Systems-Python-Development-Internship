"""
SaiKet Systems - Python Development Internship
Task 6: Word Count Tool

Description:
Analyzes a text file and reports the number of words, lines, and
characters. Also performs word frequency analysis to find the most
common words, presenting results in a structured format.

Skills demonstrated: File Input/Output in Python, String Manipulation,
Data Analysis
"""

import os
import string
from collections import Counter


def create_sample_file_if_missing(filepath):
    """Creates a sample text file so the script can be tested immediately."""
    if not os.path.exists(filepath):
        sample_text = (
            "SaiKet Systems offers an amazing Python internship program.\n"
            "Python is a powerful and versatile programming language.\n"
            "Interns learn Python, build projects, and grow their skills.\n"
            "Python, Python, Python - practice makes perfect!\n"
        )
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(sample_text)
        print(f"Sample file '{filepath}' created for demonstration.\n")


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


def analyze_text(content):
    lines = content.splitlines()
    num_lines = len(lines)
    num_characters = len(content)

    # Strip punctuation and lowercase words for accurate counting
    translator = str.maketrans("", "", string.punctuation)
    cleaned = content.translate(translator).lower()
    words = cleaned.split()
    num_words = len(words)

    word_frequency = Counter(words)

    return {
        "lines": num_lines,
        "words": num_words,
        "characters": num_characters,
        "frequency": word_frequency,
    }


def display_results(stats, top_n=10):
    print("\n===== WORD COUNT ANALYSIS =====")
    print(f"Total Lines      : {stats['lines']}")
    print(f"Total Words      : {stats['words']}")
    print(f"Total Characters : {stats['characters']}")

    print(f"\nTop {top_n} Most Common Words:")
    print("-" * 30)
    most_common = stats["frequency"].most_common(top_n)
    if not most_common:
        print("No words found.")
    else:
        for rank, (word, count) in enumerate(most_common, start=1):
            print(f"{rank}. {word:<15} -> {count} time(s)")
    print("-" * 30 + "\n")


def main():
    filepath = "sample_wordcount.txt"
    create_sample_file_if_missing(filepath)

    print("===== WORD COUNT TOOL =====")
    use_default = input(
        f"Analyze the sample file '{filepath}'? (y/n, 'n' lets you enter a different path): "
    ).strip().lower()

    if use_default != "y":
        filepath = input("Enter the path of the text file to analyze: ").strip()

    content = read_file(filepath)
    if content is None:
        return

    stats = analyze_text(content)
    display_results(stats)


if __name__ == "__main__":
    main()
