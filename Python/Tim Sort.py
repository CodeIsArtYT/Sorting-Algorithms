def tim_sort(arr):
	# Set the minimum run length
	min_run = 32
	n = len(arr)

	# Sort individual subarrays of size min_run using insertion sort
	for i in range(0, n, min_run):
		insertion_sort(arr, i, min((i + min_run - 1), n - 1))

	# Double the size of the current run until the entire array is sorted
	size = min_run
	while size < n:
		for start in range(0, n, size * 2):
			mid = start + size - 1
			end = min((start + size * 2 - 1), (n - 1))
			merge(arr, start, mid, end)
		size *= 2


# Helper function to perform insertion sort on subarrays
def insertion_sort(arr, left, right):
	for i in range(left + 1, right + 1):
		key_item = arr[i]
		j = i - 1
		while j >= left and arr[j] > key_item:
			arr[j + 1] = arr[j]
			j -= 1
		arr[j + 1] = key_item


# Helper function to merge subarrays
def merge(arr, start, mid, end):
	if mid == end:
		return  # if reached end return empty to end reccursion
	merged_arr = []
	left_idx = start
	right_idx = mid + 1
	while left_idx <= mid and right_idx <= end:
		if arr[left_idx] < arr[right_idx]:
			merged_arr.append(arr[left_idx])
			left_idx += 1
		else:
			merged_arr.append(arr[right_idx])
			right_idx += 1
	while left_idx <= mid:
		merged_arr.append(arr[left_idx])
		left_idx += 1
	while right_idx <= end:
		merged_arr.append(arr[right_idx])
		right_idx += 1
	for i, sorted_item in enumerate(merged_arr):
		arr[start + i] = sorted_item  # final step


# Example usage:
# Create an unsorted array
arr = [64, 34, 25, 12, 22, 11, 90]
# Print the original array
print("Original array:", arr)
# Sort the array using tim_sort function
tim_sort(arr)
# Print the sorted array
print("Sorted array:", arr)
