# Algoritma Pengurutan Data Dasar
# 1.Bubble Sort
arr = [5, 3, 8, 4, 2]

for i in range(len(arr)):
    for j in range(len(arr)-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print("Bubble Sort:", arr)
# 2.Selection Sort
arr = [5, 3, 8, 4, 2]

for i in range(len(arr)):
    min_index = i
    for j in range(i+1, len(arr)):
        if arr[j] < arr[min_index]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]

print("Selection Sort:", arr)
# 3.Insertion Sort
arr = [5, 3, 8, 4, 2]

for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > key:
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = key

print("Insertion Sort:", arr)