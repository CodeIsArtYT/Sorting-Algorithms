def cocktail_sort(arr):
	"""
	Cocktail Sort algorithm to sort a list of integers in ascending order.

	Args:
	- arr (list): List of integers to be sorted.

	Returns:
	None
	"""
	
	n = len(arr)
	swapped = True
	start = 0
	end = n - 1
	
	while (swapped == True):
		
		# Reset the swapped flag
		swapped = False
		
		# Move the largest item to the end
		for i in range(start, end):
			if arr[i] > arr[i + 1]:
				arr[i], arr[i + 1] = arr[i + 1], arr[i]
				swapped = True
		
		# If nothing moved, array is sorted
		if (swapped == False):
			break
		
		# Otherwise, reset the swapped flag and move the smallest item to the beginning
		swapped = False
		end = end - 1
		
		for i in range(end - 1, start - 1, -1):
			if arr[i] > arr[i + 1]:
				arr[i], arr[i + 1] = arr[i + 1], arr[i]
				swapped = True
		
		start = start + 1


# Example usage:
# Create an unsorted array
arr = [64, 34, 25, 12, 22, 11, 90]
# Print the original array
print("Original array:", arr)
# Sort the array using cocktail_sort function
cocktail_sort(arr)
# Print the sorted array
print("Sorted array:", arr)
