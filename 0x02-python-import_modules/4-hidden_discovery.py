#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    # Get all the names defined in hidden_4
    names = dir(hidden_4)

    # Filter and print names that don't start with "__", sorted alphabetically
    for name in sorted(names):
        if not name.startswith("__"):
            print(name)
