#Given two lists of numbers, concatenate them into a single list

def concatenate_lists(list1, list2):
    """
    Concatenate two lists into a single list.

    Parameters:
        list1 (list): The first list.
        list2 (list): The second list.

    Returns:
        list: The concatenated list.
    """
    # Concatenate the two lists using the + operator
    concatenated_list = list1 + list2
    return concatenated_list

# Example usage:
list_1 = [1, 2, 3, 4, 5]
list_2 = [6, 7, 8, 9, 10]
concatenated_list = concatenate_lists(list_1, list_2)
print("Concatenated list:", concatenated_list)




