def bubble_sort(arr):
	n = len(arr)
	for i in range(n):
		for j in range(n):
			if arr[j] > arr[j+1]:
				arr[j] = arr[j+1]
				arr[j+1] = arr[j]
	return arr

print(bubble_sort([4,3,1,2,6,7,9]))
