def quick_sort(arr):
	"""
	Sort an array of integers using the quick sort algorithm.

	Parameters:
	arr (list of int): Unsorted array of integers

	Returns:
	list of int: Sorted array of integers
	"""

	# Base case: if the array has 1 or 0 elements, it is already sorted
	if len(arr) <= 1:
		return arr # return original array

	# Choose a pivot element as the middle element of the array
	pivot = arr[len(arr) // 2]

	# Divide the array into three sub-arrays: left, middle, and right
	# Left contains all elements smaller than the pivot
	# Middle contains all elements equal to the pivot
	# Right contains all elements greater than the pivot
	left = [x for x in arr if x < pivot]
	middle = [x for x in arr if x == pivot]
	right = [x for x in arr if x > pivot]

	# Recursively call the quick_sort function on the left and right sub-arrays
	# and concatenate the sorted left sub-array, middle sub-array, and right sub-array
	return quick_sort(left) + middle + quick_sort(right)


# Example usage:
# Create an unsorted array
arr = [64, 34, 25, 12, 22, 11, 90]
# Print the original array
print("Original array:", arr)
# Sort the array using quick_sort function
arr = quick_sort(arr)
# Print the sorted array
print("Sorted array:", arr)
