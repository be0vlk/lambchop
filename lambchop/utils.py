""" This module contains utility functions used by the lambchop package such as colored output and file operations. """

import builtins
import os
import re
from colorama import init, Fore

# Initialize colorama
init(autoreset=True)

WHITE = Fore.WHITE
CYAN = Fore.CYAN
RED = Fore.RED


def print_banner():
    print("""
█░░ ▄▀█ █▀▄▀█ █▄▄ █▀▀ █░█ █▀█ █▀█
█▄▄ █▀█ █░▀░█ █▄█ █▄▄ █▀█ █▄█ █▀▀
""")


def colorize(message):
    """
    Colorizes a message by replacing specific markers with color codes.

    Args:
        message (str): The message to be colorized.

    Returns:
        str: The colorized message.

    """

    colorized_message = message
    colorized_message = re.sub(r"\[\*]", f"{CYAN}[*]{WHITE}", colorized_message)
    colorized_message = re.sub(r"\[!]", f"{RED}[!]{WHITE}", colorized_message)
    return colorized_message


def printc(*args, **kwargs):
    """
    Colorized version of the print function.

    This function takes the same arguments as the built-in print function and prints the colorized output.

    Args:
        *args: The positional arguments to be printed.
        **kwargs: The keyword arguments to be passed to the built-in print function.

    """

    builtins.print(*(colorize(arg) for arg in args), **kwargs)


def get_output_dir(output_dir=None):
    """
    Returns the output directory in the user's home directory.
    """
    home_dir = os.path.expanduser("~")
    output_dir = os.path.join(home_dir, "lambchop_output")
    return output_dir

def save_to_file(data, full_name, out_dir, extension="json", separator="\n"):
    """
    Saves data to a file based on the provided person's name and extension.

    Args:
        data (str): The data to be saved.
        full_name (str): The full name used to generate the filename.
        out_dir (str): The directory where the file will be saved.
        extension (str): The file extension (default is "json").
        separator (str): The separator used to join data if it's a list (default is "\n").

    Returns:
        str: The path to the saved file.
    """
    os.makedirs(out_dir, exist_ok=True)
    filename = full_name.lower().replace(" ", "_") + f".{extension}"
    output_file_path = os.path.join(out_dir, filename)

    if isinstance(data, list):
        data = separator.join(data)

    with open(output_file_path, "w", encoding="utf-8") as f:
        f.write(data)

    return output_file_path
