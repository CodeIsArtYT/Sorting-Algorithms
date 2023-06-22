def stooge_sort(arr):
	"""
	Stooge Sort algorithm to sort a list of integers in ascending order.

	Args:
	- arr (list): List of integers to be sorted.

	Returns:
	None
	"""

	def stooge_helper(arr, i, j):
		# Swap arr[i] and arr[j] if arr[i] > arr[j]
		if arr[i] > arr[j]:
			arr[i], arr[j] = arr[j], arr[i]

		# If there are at least three elements, then recursively sort first two-thirds,
		# then last two-thirds, then first two-thirds again
		if i + 1 >= j:
			return  # return if i + 1 >= j
		k = (j - i + 1) // 3  # Calculate k
		stooge_helper(arr, i, j - k)
		stooge_helper(arr, i + k, j)
		stooge_helper(arr, i, j - k)

	# Call the helper function with initial indices 0 and len(arr) - 1
	stooge_helper(arr, 0, len(arr) - 1)


# Example usage:
# Create an unsorted array
arr = [64, 34, 25, 12, 22, 11, 90]
# Print the original array
print("Original array:", arr)
# Sort the array using stooge_sort function
stooge_sort(arr)
# Print the sorted array
print("Sorted array:", arr)
