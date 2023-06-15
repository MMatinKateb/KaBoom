import os
import sys
from PrintIntro import print_intro
from RunKaboom import run_kaboom

# Colors
RED = '\033[31m'
GREEN = '\033[32m'
RESET = '\033[0m'

def check_root():
    is_not_root = not (os.getuid() == 0)
    if is_not_root:
        print(RED + "[!!!]" + RESET + " Must run as root.")
        sys.exit(0)


def main():
    print_intro()
    check_root()

    print(f"{RED}WARNING!!! running this tool means the death of your OS.{RESET}")
    opt = input(f"> Are you sure that you want to run this tool on this system? (y/n): ")

    while True:
        try:
            if opt == 'y' or opt == 'Y':

                opt2 = input(f"{RED}You sure?? (y/n): ")
                if opt2 == 'y' or opt2 == 'Y':
                    run_kaboom()

                elif opt2 == 'n' or opt2 == 'N':
                    print(f"{RED}[-]{RESET}Cancelling operation...")
                    break

                else:
                    raise Exception

            elif opt == 'n' or opt == 'N':
                print(f"{RED}[-]{RESET}Cancelling operation...")
                break

            else:
                raise Exception
        
        except:
            print("Invalid input.")
            continue

    sys.exit(1)

    

if __name__ == "__main__":
    main()