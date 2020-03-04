def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

def partition(arr, start, end):
    pivot = arr[start]
    j = start+1

    for i in range(start+1, end+1):
        if arr[i] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    
    j -= 1
    arr[start], arr[j] = arr[j], arr[start]

    return j

def quick_sort(arr, start, end):
    if left < right:
        split = partition(arr, start, end)

        quick_sort(arr, start, split-1)
        quick_sort(arr, split+1, end)
