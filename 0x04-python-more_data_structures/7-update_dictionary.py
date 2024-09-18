#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    # Update or add key-value pairs at the top level
    def update(d, k, v):
        if k in d:
            d[k] = v
        else:
            d[k] = v

    # Use map and lambda to update the dictionary
    def update_recursive(d, k, v):
        # If the dictionary has the key at the top level
        if k in d:
            update(d, k, v)
        else:
            for sub_key in d:
                if isinstance(d[sub_key], dict):
                    # Recursively update nested dictionaries
                    update_recursive(d[sub_key], k, v)
            # If not found in nested dictionaries, add it at the top level
            update(d, k, v)

    update_recursive(a_dictionary, key, value)
    return a_dictionary
