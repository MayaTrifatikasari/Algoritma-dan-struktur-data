# DATA AWAL
data = [5, 3, 8, 2, 1]


# 1. Bubble Sort
bubble = data.copy()
n = len(bubble)

for i in range(n):
    for j in range(0, n - i - 1):
        if bubble[j] > bubble[j + 1]:
            bubble[j], bubble[j + 1] = bubble[j + 1], bubble[j]

print("Bubble Sort    :", bubble)


# 2. Selection Sort
selection = data.copy()

for i in range(len(selection)):
    min_idx = i
    for j in range(i + 1, len(selection)):
        if selection[j] < selection[min_idx]:
            min_idx = j
    selection[i], selection[min_idx] = selection[min_idx], selection[i]

print("Selection Sort :", selection)


# 3. Insertion Sort
insertion = data.copy()

for i in range(1, len(insertion)):
    key = insertion[i]
    j = i - 1
    while j >= 0 and insertion[j] > key:
        insertion[j + 1] = insertion[j]
        j -= 1
    insertion[j + 1] = key

print("Insertion Sort :", insertion)
