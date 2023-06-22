def radix_sort(arr):
	"""
	Radix Sort algorithm to sort a list of integers in ascending order.

	Args:
	- arr (list): List of non-negative integers to be sorted.

	Returns:
	None
	"""

	def counting_sort_exp(arr, exp):
		"""
		Helper function to perform Counting Sort based on a particular digit's value.

		Args:
		- arr (list): List of integers to be sorted.
		- exp (int): Exponent value for the current digit's place value.

		Returns:
		None
		"""
		# Compute the range of values in the input list
		max_val = max(arr)
		min_val = min(arr)
		range_val = max_val - min_val + 1

		# Initialize count and output arrays
		count = [0] * range_val
		output = [0] * len(arr)

		# Count the number of occurrences of each digit in the current place value
		for i in range(len(arr)):
			count[(arr[i] // exp) % 10 - min_val] += 1

		# Compute the cumulative sum of the counts
		for i in range(1, len(count)):
			count[i] += count[i - 1]

		# Place the elements in the output array in sorted order
		for i in range(len(arr) - 1, -1, -1):
			output[count[(arr[i] // exp) % 10 - min_val] - 1] = arr[i]
			count[(arr[i] // exp) % 10 - min_val] -= 1

		# Copy the output array to the input array
		for i in range(len(arr)):
			arr[i] = output[i]

	# Compute the maximum value of the input list
	max_val = max(arr)

	# Iterate from the least significant digit to the most significant digit
	exp = 1
	while max_val // exp > 0:
		counting_sort_exp(arr, exp)
		exp *= 10


# Example usage:
arr = [64, 34, 25, 12, 22, 11, 90]  # Input list
print("Original array:", arr)
radix_sort(arr)  # Call radix_sort() function to sort the list
print("Sorted array:", arr)  # Print the sorted list
