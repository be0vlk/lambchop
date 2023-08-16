""" This module contains utility functions used by the lambchop package such as colored output and file operations. """

import builtins
import json
import os
import re
from colorama import init, Fore
import openai

# Initialize colorama
init(autoreset=True)

WHITE = Fore.WHITE
CYAN = Fore.CYAN
RED = Fore.RED


def print_banner():
    print("""
█░░ ▄▀█ █▀▄▀█ █▄▄ █▀▀ █░█ █▀█ █▀█
█▄▄ █▀█ █░▀░█ █▄█ █▄▄ █▀█ █▄█ █▀▀
_______________________________

AI driven sock puppet generator
_______________________________
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


def get_config_options():
    try:
        config_file = os.getenv("LAMBCHOP_CONFIG_FILE")
        with open(config_file, "r", encoding="utf-8") as f:
            j = json.loads(f.read())
            openai.api_key = j["OPENAI_API_KEY"]
            twitter_config = j["twitter"]
            output_dir = j["OUTPUT_DIR"]
    except (FileNotFoundError, TypeError):
        printc("[!] Set the path to your config file using the LAMBCHOP_CONFIG_FILE environment variable.")
        exit(1)

    return output_dir, twitter_config
