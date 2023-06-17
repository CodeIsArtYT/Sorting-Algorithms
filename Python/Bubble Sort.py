def bubble_sort(arr):
	"""
	Bubble Sort algorithm to sort a list of integers in ascending order.

	Args:
	- arr (list): List of integers to be sorted.

	Returns:
	None
	"""
	
	n = len(arr)
	
	# Traverse through all array elements
	for i in range(n):
		
		# Last i elements are already in place
		for j in range(0, n - i - 1):
			
			# Traverse the array from 0 to n-i-1
			# Swap if the element found is greater than the next element
			if arr[j] > arr[j + 1]:
				arr[j], arr[j + 1] = arr[j + 1], arr[j]


# Example usage:
# Create an unsorted array
arr = [64, 34, 25, 12, 22, 11, 90]
# Print the original array
print("Original array:", arr)
# Sort the array using bubble_sort function
bubble_sort(arr)
# Print the sorted array
print("Sorted array:", arr)
