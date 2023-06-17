def cycle_sort(arr):
	"""
	Cycle Sort algorithm to sort a list of integers in ascending order.

	Args:
	- arr (list): List of integers to be sorted.

	Returns:
	None
	"""
	
	n = len(arr)
	
	# Traverse through all array elements
	for cycle_start in range(0, n - 1):
		item = arr[cycle_start]
		
		# Find the position where we put the item
		pos = cycle_start # Set pos as cycle_start
		for i in range(cycle_start + 1, n):
			if arr[i] < item:
				pos += 1
		
		# If the item is already there, this is not a cycle
		if pos == cycle_start:
			continue
		
		# Otherwise, put the item there or right after any duplicates
		while item == arr[pos]:
			pos += 1
		arr[pos], item = item, arr[pos]
		
		# Rotate the rest of the cycle
		while pos != cycle_start:
			pos = cycle_start # Set pos as cycle_start
			for i in range(cycle_start + 1, n):
				if arr[i] < item:
					pos += 1
			while item == arr[pos]:
				pos += 1
			arr[pos], item = item, arr[pos]


# Example usage:
# Create an unsorted array
arr = [64, 34, 25, 12, 22, 11, 90]
# Print the original array
print("Original array:", arr)
# Sort the array using cycle_sort function
cycle_sort(arr)
# Print the sorted array
print("Sorted array:", arr)
