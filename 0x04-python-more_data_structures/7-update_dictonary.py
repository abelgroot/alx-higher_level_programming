#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    # Use lambda and map to handle key update or addition
    updated_dict = dict(
        map(
            lambda item: (item[0], value) if item[0] == key else item,
            a_dictionary.items(),
        )
    )
    if key not in updated_dict:
        updated_dict[key] = value
    return updated_dict
