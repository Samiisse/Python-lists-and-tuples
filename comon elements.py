#Create a program that finds the common elements between two lists and stores them in a new list

def find_common_elements(list1, list2):
    """
    Find the common elements between two lists and store them in a new list.

    Parameters:
        list1 (list): The first list.
        list2 (list): The second list.

    Returns:
        list: A new list containing the common elements.
    """
    # Convert lists to sets to find common elements efficiently
    set1 = set(list1)
    set2 = set(list2)
    # Find the intersection of the two sets (common elements)
    common_elements = list(set1.intersection(set2))
    return common_elements

# Example usage:
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common_elements = find_common_elements(list1, list2)
print("Common elements between the two lists:", common_elements)
