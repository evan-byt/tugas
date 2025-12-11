# Algoritma Tingkat Lanjut
# 1.Shell Sort
arr = [5, 3, 8, 4, 2]
gap = len(arr) // 2

while gap > 0:
    for i in range(gap, len(arr)):
        temp = arr[i]
        j = i
        while j >= gap and arr[j-gap] > temp:
            arr[j] = arr[j-gap]
            j -= gap
        arr[j] = temp
    gap //= 2

print("Shell Sort:", arr)
# 2.Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]; i += 1
            else:
                arr[k] = R[j]; j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]; i += 1; k += 1

        while j < len(R):
            arr[k] = R[j]; j += 1; k += 1

arr = [5, 3, 8, 4, 2]
merge_sort(arr)
print("Merge Sort:", arr)
# 3.Quick Sort
def quick(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    kiri = [x for x in arr[1:] if x < pivot]
    kanan = [x for x in arr[1:] if x >= pivot]
    return quick(kiri) + [pivot] + quick(kanan)

arr = [5, 3, 8, 4, 2]
print("Quick Sort:", quick(arr))