def gnome_sort(arr):
	"""
	Gnome Sort algorithm to sort a list of integers in ascending order.

	Args:
	- arr (list): List of integers to be sorted.

	Returns:
	None
	"""

	n = len(arr)  # Get the length of the list
	i = 0  # Initialize a counter

	while i < n:  # Loop through the list
		if i == 0 or arr[i] >= arr[i - 1]:
			# If the current element is greater than or equal to the previous element, move to the next element
			i += 1
		else:  # Otherwise, swap the current and previous elements and move back one position
			arr[i], arr[i - 1] = arr[i - 1], arr[i]
			i -= 1


# Example usage:
# Create an unsorted array
arr = [64, 34, 25, 12, 22, 11, 90]
# Print the original array
print("Original array:", arr)
# Sort the array using gnome_sort function
gnome_sort(arr)
# Print the sorted array
print("Sorted array:", arr)
