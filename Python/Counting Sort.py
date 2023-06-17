def counting_sort(arr):
	"""
	Counting Sort algorithm to sort a list of integers in ascending order.

	Args:
	- arr (list): List of integers to be sorted. Assumes that the input list contains only non-negative integers.

	Returns:
	None
	"""
	# Determine the range of input values
	max_val = max(arr)
	min_val = min(arr)
	range_val = max_val - min_val + 1
	
	# Initialize the count array with zeros
	count = [0] * range_val
	output = [0] * len(arr)
	
	# Count the occurrences of each value in the input array
	for i in range(len(arr)):
		count[arr[i] - min_val] += 1
	
	# Calculate the running sum of counts
	for i in range(1, len(count)):
		count[i] += count[i - 1]
	
	# Place the values in the output array in sorted order
	for i in range(len(arr) - 1, -1, -1):
		output[count[arr[i] - min_val] - 1] = arr[i]
		count[arr[i] - min_val] -= 1
	
	# Copy the sorted output array back to the input array
	for i in range(len(arr)):
		arr[i] = output[i]


# Example usage:
arr = [64, 34, 25, 12, 22, 11, 90]  # Input list
print("Original array:", arr)
counting_sort(arr)  # Call counting_sort() function to sort the list
print("Sorted array:", arr)  # Print the sorted list
