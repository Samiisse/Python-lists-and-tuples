#Given a list of words, find the word with the maximum length and its length

def find_longest_word(words):
    """
    Find the word with the maximum length in a list of words and its length.

    Parameters:
        words (list): The list of words.

    Returns:
        tuple: A tuple containing the longest word and its length.
    """
    # Initialize variables to store the longest word and its length
    longest_word = ""
    max_length = 0
    # Iterate through each word in the list
    for word in words:
        # Check if the current word has a greater length than the previous maximum
        if len(word) > max_length:
            longest_word = word
            max_length = len(word)
    return longest_word, max_length

# Example usage:
word_list = ["apple", "banana", "orange", "grapefruit", "kiwi"]
longest_word, length = find_longest_word(word_list)
print("Longest word:", longest_word)
print("Length of longest word:", length)
