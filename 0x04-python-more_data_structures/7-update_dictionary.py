#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    # Use filter to find if the key exists
    existing_keys = list(filter(lambda k: k == key, a_dictionary.keys()))

    # Update or add the key-value pair
    updated_dict = dict(
        map(
            lambda item: (item[0], value) if item[0] == key else item,
            a_dictionary.items(),
        )
    )

    # If the key doesn't exist, add it
    if not existing_keys:
        updated_dict[key] = value

    return updated_dict
