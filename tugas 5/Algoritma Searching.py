#Algoritma Searching (Linear & Binary)
#1.Linear Search
data = [5, 8, 2, 9, 1]
cari = 9

for i in range(len(data)):
    if data[i] == cari:
        print("Ketemu di index", i)
        break

#2.Binary Search
data = [1, 2, 3, 4, 5, 6, 7]
cari = 5
low, high = 0, len(data)-1

while low <= high:
    mid = (low + high) // 2
    if data[mid] == cari:
        print("Ketemu di index", mid)
        break
    elif data[mid] < cari:
        low = mid + 1
    else:
        high = mid - 1