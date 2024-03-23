#Write a Python program to count the occurrences of each element in a given list

def count_occurrences(input_list):
    """
    Count the occurrences of each element in a given list.

    Parameters:
        input_list (list): The input list.

    Returns:
        dict: A dictionary containing the count of each element.
    """
    # Initialize an empty dictionary to store the counts
    occurrences = {}
    # Iterate through each element in the list
    for element in input_list:
        # Increment the count of the element in the dictionary
        if element in occurrences:
            occurrences[element] += 1
        else:
            occurrences[element] = 1
    return occurrences

# Example usage:
input_list = [1, 2, 3, 2, 1, 3, 4, 5, 4, 3]
occurrences = count_occurrences(input_list)
print("Occurrences of each element:", occurrences)
