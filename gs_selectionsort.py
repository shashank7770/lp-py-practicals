def selectionSort(arr):
	n = len(arr)
	
	for i in range(n):
		min_index = 1
		
		for j in range(i +1, n):
			if arr[j] < arr[min_index]:
				min_index = j
				
		arr[i], arr[min_index] = arr[min_index], arr[i]
		
	return arr
	
	n = int(input("Enter the number of elements: "))
	arr = []
	for i in range(n):
		num = int(input(f"Enter element {i+1}: "))
		arr.append(num)
		
	print("Original array: ",arr)
	print("Sorted array: ", selectionSort(arr))
