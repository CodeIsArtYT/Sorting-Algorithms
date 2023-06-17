def insertion_sort(arr):
	"""
	Insertion Sort algorithm to sort a list of integers in ascending order.

	Args:
	- arr (list): List of integers to be sorted.

	Returns:
	None
	"""
	# Traverse through all array elements
	for i in range(1, len(arr)):
		# Store the current element in a variable
		key = arr[i]
		# Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
		j = i - 1
		while j >= 0 and key < arr[j]:
			arr[j + 1] = arr[j]
			j -= 1
		# Put the stored key value in its correct position in the sorted subarray
		arr[j + 1] = key


# Example usage:
# Create an unsorted array
arr = [64, 34, 25, 12, 22, 11, 90]
# Print the original array
print("Original array:", arr)
# Sort the array using insertion_sort function
insertion_sort(arr)
# Print the sorted array
print("Sorted array:", arr)
