def merge_sort(arr):
	"""
	Merge Sort algorithm to sort a list of integers in ascending order.

	Args:
	- arr (list): List of integers to be sorted in place.

	Returns:
	None
	"""
	
	# Define a helper function to merge two sorted lists
	def merge(left, right):
		"""
		Helper function to merge two sorted lists into a single sorted list.

		Args:
		- left (list): Left half of the list to be merged.
		- right (list): Right half of the list to be merged.

		Returns:
		list: Merged and sorted list.
		"""
		# Initialize pointers for left, right, and merged lists
		i, j, k = 0, 0, 0
		# Compare the elements in the left and right lists and add them to the merged list in ascending order
		while i < len(left) and j < len(right):
			if left[i] <= right[j]:
				arr[k] = left[i]
				i += 1
			else:
				arr[k] = right[j]
				j += 1
			k += 1
		# Add any remaining elements in the left list to the merged list
		while i < len(left):
			arr[k] = left[i]
			i += 1
			k += 1
		# Add any remaining elements in the right list to the merged list
		while j < len(right):
			arr[k] = right[j]
			j += 1
			k += 1
	
	# If the list has more than one element, divide it into two sub-lists
	if len(arr) > 1:
		mid = len(arr) // 2
		left = arr[:mid]
		right = arr[mid:]
		
		# Recursively sort the left and right sub-lists
		merge_sort(left)
		merge_sort(right)
		
		# Merge the sorted left and right sub-lists
		merge(left, right)


# Example usage:
# Create an unsorted list
arr = [64, 34, 25, 12, 22, 11, 90]
print("Original array:", arr)
# Sort the list using merge_sort() function
merge_sort(arr)
# Print the sorted list
print("Sorted array:", arr)
