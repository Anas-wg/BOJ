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
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    return arr


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)


arr = [12, 7, 13, 5, 6, 11]
arr_sorted = merge_sort(arr)
print("Merge Sorted random array is:", arr_sorted)

almost_arr = [5, 6, 7, 11, 13, 12]
almost_arr_sorted = merge_sort(almost_arr)
print("Merge Sorted almost array is:", almost_arr_sorted)

# arr = [12, 7, 13, 5, 6, 11]
# arr_sorted = quick_sort(arr)
# print("Quick Sorted random array is:", arr_sorted)

# almost_arr = [5, 6, 7, 11, 13, 12]
# almost_arr_sorted = quick_sort(almost_arr)
# print("Quick Sorted almost array is:", almost_arr_sorted)
