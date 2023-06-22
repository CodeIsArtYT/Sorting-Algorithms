def shellSort(arr):
	n = len(arr)
	gap = n // 2  # initialize the gap size

	# loop over the gap sizes from largest to smallest
	while gap > 0:
		# perform insertion sort on each sublist
		for i in range(gap, n):
			temp = arr[i]
			j = i # Assign i to j
			# shift elements that are greater than the current element
			# by the gap size to the right
			while j >= gap and arr[j - gap] > temp:
				arr[j] = arr[j - gap]
				j -= gap
			arr[j] = temp
		gap //= 2  # reduce the gap size

# Example usage:
arr = [64, 34, 25, 12, 22, 11, 90]  # Input list
print("Original array:", arr)
shellSort(arr)  # Call shellSort() function to sort the list
print("Sorted array:", arr)  # Print the sorted list
