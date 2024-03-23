#Write a program that checks if a given list is sorted in ascending order

def is_sorted_ascending(input_list):
    """
    Check if a given list is sorted in ascending order.

    Parameters:
        input_list (list): The input list.

    Returns:
        bool: True if the list is sorted in ascending order, False otherwise.
    """
    # Check if every element is less than or equal to the next element
    return all(input_list[i] <= input_list[i + 1] for i in range(len(input_list) - 1))

# Example usage:
list1 = [1, 2, 3, 4, 5]
list2 = [5, 4, 3, 2, 1]
print("Is list1 sorted in ascending order?", is_sorted_ascending(list1))
print("Is list2 sorted in ascending order?", is_sorted_ascending(list2))
