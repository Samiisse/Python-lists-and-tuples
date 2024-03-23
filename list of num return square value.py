#Implement a function that takes a list of numbers and returns a new list with the squared values

def square_values(numbers):
    """
    Create a new list with the squared values of the numbers from the given list.

    Parameters:
        numbers (list): The list of numbers.

    Returns:
        list: A new list containing the squared values of the numbers.
    """
    # Use list comprehension to generate a new list with squared values
    squared_values = [num ** 2 for num in numbers]
    return squared_values

# Example usage:
original_list = [1, 2, 3, 4, 5]
squared_list = square_values(original_list)
print("Original list:", original_list)
print("List with squared values:", squared_list)
