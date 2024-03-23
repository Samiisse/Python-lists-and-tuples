#Given a list of names, remove all duplicate names and print the unique names

def remove_duplicates(names):
    """
    Remove duplicate names from a list of names.

    Parameters:
        names (list): The list of names.

    Returns:
        list: A new list containing unique names.
    """
    # Use set to remove duplicates and preserve the order
    unique_names = list(set(names))
    return unique_names

# Example usage:
name_list = ["Alice", "Bob", "Charlie", "Alice", "David", "Bob"]
unique_names = remove_duplicates(name_list)
print("Unique names:", unique_names)
