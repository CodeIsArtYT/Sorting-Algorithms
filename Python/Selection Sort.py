def selection_sort(arr):
	"""
	Selection Sort algorithm to sort a list of integers in ascending order.

	Args:
	- arr (list): List of integers to be sorted.

	Returns:
	None
	"""

	# Traverse through all array elements
	for i in range(len(arr)):

		# Find the minimum element in remaining unsorted array
		min_idx = i # Assign i to min_idx
		for j in range(i + 1, len(arr)):
			if arr[min_idx] > arr[j]:
				min_idx = j  # Assign j to min_idx

		# Swap the found minimum element with the first element
		arr[i], arr[min_idx] = arr[min_idx], arr[i]


# Example usage:
# Create an unsorted array
arr = [64, 34, 25, 12, 22, 11, 90]
# Print the original array
print("Original array:", arr)
# Sort the array using selection_sort function
selection_sort(arr)
# Print the sorted array
print("Sorted array:", arr)
