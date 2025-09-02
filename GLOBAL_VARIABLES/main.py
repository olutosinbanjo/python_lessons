"""
main file for calling subfile and using global variables
"""

import settings
import add

settings.init()     # call global variables once

def main():

    y = add.add()

    print(f"A = {settings.A}\n")
    print(f"B = {settings.B}\n")
    print(f"{settings.A} + {settings.B} =  {y}")


if __name__ == "__main__":

    try:

        main()

    except ValueError as e:
        print(f"Error: {e}")
