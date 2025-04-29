"""
homework_directory_manager.py

This module provides utilities for managing student homework directories in a structured format.
It supports the following main functionalities:

- Creating directory structures for students' homework tasks.
- Automatically generating `__init__.py` files in each directory.
- Checking if homework directories contain any files beyond `__init__.py`.
- Printing a visual (color-coded) status of which homework tasks are completed.

Classes:
    BColors: ANSI escape sequences for colored terminal output.

Functions:
    get_directory_paths(nicknames, base_dir): Generate full paths for student homework directories.
    create_directories_from_paths(directory_paths): Create directories and __init__.py files if missing.
    check_for_non_init_files(paths): Check if homework folders contain additional files.
    print_homework_status(homework_data): Print formatted status of homework completion per student.

Usage:
    Run this script directly to create/check homework folders for a predefined list of students.
"""

import re
import os
import logging
from typing import List, Dict

# Set up logging configuration
logging.basicConfig(
    level=logging.INFO, format="%(levelname)s - %(funcName)s - %(message)s"
)


class BColors:
    """
    ANSI escape sequences for terminal text coloring.
    Useful for adding visual cues (e.g., green for success, red for failure).
    """

    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def get_directory_paths(
    nicknames: Dict[str, str], base_dir: str = "hw"
) -> Dict[str, List[str]]:
    """
    Generate absolute directory paths for each student's homework folders.

    Args:
        nicknames: Dictionary mapping GitHub nicknames to student names.
        base_dir: Base directory name for homeworks (default is 'hw').

    Returns:
        A dictionary mapping each student's name to a list of their homework directory paths.
    """
    directory_paths = {}
    for nickname, name in nicknames.items():
        user_paths = []
        for hw_num in range(2, 16):
            hw_dir = os.path.join(base_dir, f"hw{hw_num:02d}")
            user_dir = os.path.join(hw_dir, nickname)
            absolute_user_dir = os.path.abspath(user_dir)
            user_paths.append(absolute_user_dir)
        directory_paths[name] = user_paths
    logging.debug("Result get_directory_paths: %s", directory_paths)
    return directory_paths


def create_directories_from_paths(directory_paths: Dict[str, List[str]]) -> None:
    """
    Create homework directories and `__init__.py` files if they don't already exist.

    Args:
        directory_paths: Dictionary mapping student names to their homework paths.
    """
    for _, user_paths in directory_paths.items():
        for user_dir in user_paths:

            if not os.path.exists(user_dir):
                os.makedirs(user_dir)
                logging.info("Created directory: %s", user_dir)
            else:
                logging.debug("Directory already exists: %s", user_dir)

            init_file_path = os.path.join(user_dir, "__init__.py")

            if not os.path.exists(init_file_path):
                with open(init_file_path, "w", encoding="utf-8") as _:
                    pass
                logging.info("Created file: %s", init_file_path)
            else:
                logging.debug("File already exists: %s", init_file_path)


def check_for_non_init_files(paths: Dict[str, List[str]]) -> Dict[str, Dict[str, bool]]:
    """
    Check whether directories contain any files other than `__init__.py`.

    Args:
        paths: Dictionary mapping student names to lists of their homework directory paths.

    Returns:
        A nested dictionary where each student's name maps to another dictionary
        of homework numbers and boolean values indicating presence of non-init files.
    """
    result = {}
    regex = re.compile(r"(hw\d{2})")
    for name, user_paths in paths.items():
        result[name] = {}
        for directory in user_paths:
            has_non_init_files = False
            for _, _, files in os.walk(directory):
                for file in files:
                    if file != "__init__.py":
                        has_non_init_files = True
                        break
                if has_non_init_files:
                    break
            result[name][regex.findall(directory)[0]] = has_non_init_files
    return result


def print_homework_status(homework_data: Dict[str, Dict[str, List[bool]]]) -> None:
    """
    Print a color-coded summary of students' homework completion status.

    Args:
        homework_data: A nested dictionary mapping student names to homework IDs
                       and booleans indicating if the homework contains non-init files.
    """
    author_column_width = 25
    print(f"{'Author':<{author_column_width}} | Tasks")
    print("-" * (author_column_width + 74))
    for author, tasks in homework_data.items():
        row = f"{author:<{author_column_width}} | "
        for task, status in tasks.items():
            row += (
                f" {BColors.OKGREEN}{task}{BColors.ENDC}"
                if status
                else f" {BColors.FAIL}{task}{BColors.ENDC}"
            )
        print(row)

#Todo: InProgress
def generate_markdown_table(homework_data: Dict[str, Dict[str, bool]]) -> str:
    """
    Generates a Markdown table summarizing students' homework completion status.

    Args:
        homework_data: A nested dictionary mapping student names to homework IDs
                       and booleans indicating if the homework contains non-init files.

    Returns:
        A string containing the Markdown table.
    """
    header = ["Author"] + list(homework_data[list(homework_data.keys())[0]].keys())
    header_separator = ["---"] * len(header)
    rows = [header, header_separator]

    for author, tasks in homework_data.items():
        row = [author]
        for status in tasks.values():
            row.append("✅" if status else "❌")
        rows.append(row)

    # Calculate column widths based on content
    column_widths = [0] * len(header)
    for row in rows:
        for i, cell in enumerate(row):
            column_widths[i] = max(column_widths[i], len(str(cell)))

    # Construct the table string
    table_string = ""
    for row in rows:
        for i, cell in enumerate(row):
            table_string += f"{cell:<{column_widths[i]}} | "
        table_string = table_string.rstrip(" |") + "\n"
    return table_string

if __name__ == "__main__":
    students = {
        "alexstoliar": "Oleksandr Stoliar",
        "OAndrikevych": "Oksana Andrikevych",
        "Oleksandr-Ryzhkov22": "Oleksandr Ryzhkov",
        "romanushak": "Roman Ushak",
        "VladMoko": "Vlad Mokosieiev",
        "marynam-1290": "Maryna Mykhailyk",
        "MaksymOleksiv": "Maksym Oleksiv",
        "aurora-tw": "Daria Sheina",
        "i-taras": "Taras Yaremko",
        "anastbond": "Anastasiia Bondarenko",
        "xw1yana": "Yana Hrabar",
        "justvzyt": "Volodymyr Zakolodnyi",
        "shyma27": "Anton Shymko",
        "Yaroslaw-L": "Yaroslav Lukovnykov",
        "ubodn": "Уляна Боднарук",
        "VivianRe": "Viktoriia Remeniuk",
        "Grytsun": "Maryna Grytsun",
        "Olya945": "Olya Petrenko",
        "promm-dd": "Dima Dridze",
        "AnyaDynia": "Anna Dynia",
        "figinspector": "Valentyn Tymofiiv",
        "molimoES": "Salimovskyi Yevhenii",
        "Oksana1-prog": "Oksana Zhuleneva",
        "0999271690alex": "Oleksandr Kolybelkin",
        "pdemchenko31": "Pavlo Demchenko",
        "brokenyvlvintageglasses9": "Kostya Polyakov ",
        "VladSusukailo": "Vlad Susukailo ",
        "Mariia77": "Malyhina Mariia ",
        "dimas1qwerty": "Dima Klymchuk ",
        "i-yevtushenko": "Ihor Yevtushenko ",
        "RichterZEA": "Yevhen Zaichenko",
        "kinash20kk1": "Kinash Roman",
        "YanaBoyko1": "Yana Boiko",
        "Sp1ker2": "Bogdan Prihodko",
        "YanaPasieka": "Yana Pasieka",
        "Hooligan199": "Pustelnyk Davyd",
        "U01FC": "Ivan Vasylkiv",
        "NataliMadriga": "Nataly Madryha",
        "KrasinV": "Viacheslav Krasin",
        "VladaShcherbyna": "Vlada Shcherbyna",
        "theatra": "Lera Pridorohina",
    }
    
    dir_paths = get_directory_paths(students)
    create_directories_from_paths(dir_paths)
    non_init_files_present = check_for_non_init_files(dir_paths)
    print_homework_status(non_init_files_present)
    # markdown_table = generate_markdown_table(non_init_files_present)
    # print(markdown_table)
