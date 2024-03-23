#Given a list of numbers, find the sum and average using built-in functions.

def calculate_sum_and_average(numbers):
    """
    Calculate the sum and average of a list of numbers.

    Parameters:
        numbers (list): The list of numbers.

    Returns:
        tuple: A tuple containing the sum and average of the numbers.
    """
    # Calculate the sum of the numbers using the sum() function
    total_sum = sum(numbers)
    # Calculate the average of the numbers
    # Average = sum / number of elements
    average = total_sum / len(numbers)
    return total_sum, average

# Example usage:
number_list = [10, 20, 30, 40, 50]
total_sum, average = calculate_sum_and_average(number_list)
print("Sum of numbers:", total_sum)
print("Average of numbers:", average)



"""
#In this code:

#We define a function calculate_sum_and_average that takes a list of numbers as input.
We use the sum() function to calculate the sum of all numbers in the list.
We use the len() function to find the number of elements in the list, which we use to calculate the average.
Finally, we return a tuple containing the sum and average of the numbers.
We call the function with a sample list of numbers and print the results.

"""
