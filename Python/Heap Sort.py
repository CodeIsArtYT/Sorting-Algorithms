def heap_sort(arr): 
	""" 
	Heap Sort algorithm to sort a list of integers in ascending order. 

	Args: 
	- arr (list): List of integers to be sorted in place. 

	Returns: 
	None 
	""" 
	def heapify(n, i): 
		""" 
		Helper function to maintain max heap property. 

		Args: 
		- n (int): Size of the heap. 
		- i (int): Index of the current root of the subtree. 

		Returns: 
		None 
		""" 
		largest = i 
		left = 2 * i + 1 
		right = 2 * i + 2 

		if left < n and arr[left] > arr[largest]: 
			largest = left 

		if right < n and arr[right] > arr[largest]: 
			largest = right 

		if largest != i: 
			arr[i], arr[largest] = arr[largest], arr[i] 
			heapify(n, largest) 

	# Build max heap 
	n = len(arr) 
	for i in range(n // 2 - 1, -1, -1): 
		heapify(n, i) 

	# Extract elements from the heap and place them at the end of the array 
	for i in range(n - 1, 0, -1): 
		arr[0], arr[i] = arr[i], arr[0] 
		heapify(i, 0) 
# Example usage: 
arr = [64, 34, 25, 12, 22, 11, 90]  # Input list 
print("Original array:", arr) 
heap_sort(arr)  # Call heap_sort() function to sort the list 
print("Sorted array:", arr)  # Print the sorted 

