"""Project Euler, Problem 1
IF we list all the natural numbers below 10 that are multiples of 3 or 5, we
get 3, 5, 6, 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000."""

""" No REPEATS!!"""

try:
    upper_bound = int(input("Enter the upper bound: "))
except ValueError:
    print("You must enter a natural integer!")
else:
    # Determine all multiples of 3.
    multiple_3_list = []
    multiple_3_sum = 0
    print("Multiples of 3: ")
    for multiple_3 in range(0, upper_bound, 3):
        multiple_3_sum += multiple_3
        multiple_3_list.append(multiple_3)
    print(multiple_3_list)
    print("Number of multiples: " + str(len(multiple_3_list)))
    print("Sum: " + str(multiple_3_sum))
    print("--------------------")

    # Determine all multiples of 5
    multiple_5_list = []
    multiple_5_sum = 0
    print("Multiples of 5: ")
    for multiple_5 in range(0, upper_bound, 5):
        multiple_5_sum += multiple_5
        multiple_5_list.append(multiple_5)
    print(multiple_5_list)
    print("Number of multiples: " + str(len(multiple_5_list)))
    print("Sum: " + str(multiple_5_sum))
    print("--------------------")

    # Print the final total

    # Concatenate the two lists
    combined_list = multiple_3_list + multiple_5_list
    # Sort the result in ascending order (for my own sanity)
    combined_list.sort()
    # Print the sorted list
    print(combined_list)
    # Number of elements in the sorted list
    print("Number of elements: " + str(len(combined_list)))
    # Uniquify the list
    unique_combined_list = set(combined_list)
    # Print uniquified list
    print(unique_combined_list)
    # Number of elements in uniquified list
    print("Number of elements: " + str(len(unique_combined_list)))
    # Element difference
    difference = len(combined_list) - len(unique_combined_list)
    print("Element difference: " + str(difference))

    final_sum = 0
    # Sum the uniquified elements
    for element in unique_combined_list:
        final_sum += element

    print("Final Summation: " + str(final_sum))

