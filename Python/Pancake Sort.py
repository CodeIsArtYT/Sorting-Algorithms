def pancake_sort(arr):
	"""
	Pancake Sort algorithm to sort a list of integers in ascending order.

	Args:
	- arr (list): List of integers to be sorted.

	Returns:
	None
	"""
	
	n = len(arr)
	
	# Function to flip the array from index 0 to index i
	def flip(i):
		for j in range(0, i // 2):
			arr[j], arr[i - j - 1] = arr[i - j - 1], arr[j]
	
	# Traverse through all array elements
	for i in range(n, 1, -1):
		# Find the index of the maximum element in the unsorted subarray
		max_index = arr.index(max(arr[:i]))
		# Flip the array from index 0 to index max_index
		flip(max_index + 1)
		# Flip the array from index 0 to index i
		flip(i)


# Example usage:
# Create an unsorted array
arr = [64, 34, 25, 12, 22, 11, 90]
# Print the original array
print("Original array:", arr)
# Sort the array using pancake_sort function
pancake_sort(arr)
# Print the sorted array
print("Sorted array:", arr)
