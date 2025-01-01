#!/usr/bin/python3


def best_score(a_dictionary):
    """Returns the key with the biggest integer value."""
    if not a_dictionary:
        return None
    return max(a_dictionary.items(), key=lambda item: item[1])[0]
