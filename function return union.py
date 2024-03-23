#Implement a function that takes two lists and returns their union (all unique elements from both lists).

def find_union(list1, list2):
    """
    Find the union of two lists (all unique elements from both lists).

    Parameters:
        list1 (list): The first list.
        list2 (list): The second list.

    Returns:
        list: A new list containing the union of elements from both lists.
    """
    # Convert lists to sets to remove duplicates
    set1 = set(list1)
    set2 = set(list2)
    # Find the union of the two sets (all unique elements)
    union = list(set1.union(set2))
    return union

# Example usage:
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
union = find_union(list1, list2)
print("Union of the two lists:", union)
