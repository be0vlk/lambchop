# Lambchop is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or any later version.
#
# Lambchop is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Lambchop. If not, see <https://www.gnu.org/licenses/>.

from lambchop import generator
from lambchop.utils import printc, print_banner


def clear_screen():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    try:
        print_banner()
        printc("\n[*] 1. Generate new profile")
        printc("[*] 2. Generate social media content")
        printc("[*] 3. Exit")
        while True:
            selection = input("> ")

            if selection == "1":
                country = input("Country: ")
                lang = input("Language: ")
                style = input("Style: ")

                # Only pass values that are not empty
                kwargs = {}
                if country:
                    kwargs["country"] = country
                if lang:
                    kwargs["language"] = lang
                if style:
                    kwargs["style"] = style

                generator.main(**kwargs)
                break
            elif selection == "2":
                printc("[!] That one is a work in progress...")
            elif selection == "3":
                printc("[!] Exiting...")
                exit(0)
            else:
                printc("[!] Invalid choice. Please select a valid option.")
    except KeyboardInterrupt:
        printc("[!] Exiting...")
        exit(0)


if __name__ == "__main__":
    main()
