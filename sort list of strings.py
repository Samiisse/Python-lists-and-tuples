#Create a function that takes a list of strings and returns the list sorted by the length of the strings

def sort_by_length(string_list):
    """
    Sort a list of strings by the length of the strings.

    Parameters:
        string_list (list): The list of strings.

    Returns:
        list: A new list containing strings sorted by length.
    """
    # Sort the list of strings based on their lengths
    sorted_list = sorted(string_list, key=len)
    return sorted_list

# Example usage:
input_list = ["apple", "banana", "kiwi", "orange", "grape"]
sorted_list = sort_by_length(input_list)
print("Sorted list by length:", sorted_list)
