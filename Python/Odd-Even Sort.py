def odd_even_sort(arr):
	"""
	Odd-Even Sort algorithm to sort a list of integers in ascending order.

	Args:
	- arr (list): List of integers to be sorted.

	Returns:
	None
	"""
	
	n = len(arr)  # Get the length of the input array
	sorted = False  # Flag to indicate if the array is sorted or not
	
	while not sorted:  # While the array is not sorted
		sorted = True  # Assume the array is sorted initially
		
		# Perform the odd phase of the algorithm
		for i in range(0, n - 1, 2):
			if arr[i] > arr[i + 1]:  # If the current element is greater than the next element
				arr[i], arr[i + 1] = arr[i + 1], arr[i]  # Swap the elements
				sorted = False  # Set the sorted flag to False to indicate that the array is not sorted
		
		# Perform the even phase of the algorithm
		for i in range(1, n - 1, 2):
			if arr[i] > arr[i + 1]:  # If the current element is greater than the next element
				arr[i], arr[i + 1] = arr[i + 1], arr[i]  # Swap the elements
				sorted = False  # Set the sorted flag to False to indicate that the array is not sorted


# Example usage:
# Create an unsorted array
arr = [64, 34, 25, 12, 22, 11, 90]
# Print the original array
print("Original array:", arr)
# Sort the array using odd_even_sort function
odd_even_sort(arr)
# Print the sorted array
print("Sorted array:", arr)
