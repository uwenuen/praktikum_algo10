def bubblesort_rekursif(h, n):
    if n == 1:
        return

    for i in range(n - 1):
        if h[i] > h[i + 1]:
            h[i], h[i + 1] = h[i + 1], h[i]

    bubblesort_rekursif(h, n - 1)

def caribinary(arr, start, end, h):
    if end >= start:
        mid = start + (end - start) // 2
        if arr[mid] == h:
            return mid
        elif arr[mid] > h:
            return caribinary(arr, start, mid - 1, h)
        else:
            return caribinary(arr, mid + 1, end, h)
    else:
        return -1

array = [87, 56, 34,23, 89, 15, 2, 200, 28, 31]

print("sebelum list di sorting:", array)

bubblesort_rekursif(array, len(array))
print("setelah list di sorting:", array)