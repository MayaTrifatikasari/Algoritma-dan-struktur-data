data = [38, 27, 43, 3, 9]

# Shell Sort
shell = data.copy()
gap = len(shell) // 2
while gap > 0:
    for i in range(gap, len(shell)):
        temp = shell[i]
        j = i
        while j >= gap and shell[j - gap] > temp:
            shell[j] = shell[j - gap]
            j -= gap
        shell[j] = temp
    gap //= 2
print("Shell Sort :", shell)

# Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    return sorted(merge_sort(arr[:mid]) + merge_sort(arr[mid:]))

print("Merge Sort :", merge_sort(data.copy()))

# Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    return quick_sort([x for x in arr[1:] if x < pivot]) + \
           [pivot] + \
           quick_sort([x for x in arr[1:] if x >= pivot])

print("Quick Sort :", quick_sort(data.copy()))
