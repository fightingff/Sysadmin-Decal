#! python

import sys
import os

PHONEBOOK_ENTRIES = "python_phonebook_entries"


def main():
    if len(sys.argv) < 2:
        exit(1)

    elif sys.argv[1] == "new":
        # YOUR CODE HERE #
        if len(sys.argv) < 4:
            print("Usage: new <name> <phone number>")
            exit(1)
        name = sys.argv[2]
        number = sys.argv[3]
        with open(PHONEBOOK_ENTRIES, 'a') as f:
            f.write(name + " " + number + "\n")
        print("Saved successfully")

    elif sys.argv[1] == "list":
        if not os.path.isfile(PHONEBOOK_ENTRIES) or os.path.getsize(
                PHONEBOOK_ENTRIES) == 0:
            print("phonebook is empty")
        else:
            # YOUR CODE HERE #
            with open(PHONEBOOK_ENTRIES, 'r') as f:
                print(f.read())
    
    elif sys.argv[1] == "lookup":
        # YOUR CODE HERE #
        name = " ".join(sys.argv[2:])
        with open(PHONEBOOK_ENTRIES, 'r') as f:
            lookup = "".join(filter(lambda line: name in line, f.readlines()))
            print(lookup)

    elif sys.argv[1] == "remove":
        name = " ".join(sys.argv[2:])
        # YOUR CODE HERE #
        with open(PHONEBOOK_ENTRIES, 'r') as f:
            lines = f.readlines()
        with open(PHONEBOOK_ENTRIES, 'w') as f:
            for line in lines:
                if name not in line:
                    f.write(line)

    elif sys.argv[1] == "clear":
        # YOUR CODE HERE #
        os.remove(PHONEBOOK_ENTRIES)

    else:
        name = " ".join(sys.argv[1:])
        with open(PHONEBOOK_ENTRIES, 'r') as f:
            lookup = "".join(filter(lambda line: name in line, f.readlines()))
            # YOUR CODE HERE #
            print(lookup)

if __name__ == "__main__":
    main()
