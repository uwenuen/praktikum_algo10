def caribinary(arr, start, end, n):
    if end >= start:
        mid = start + (end - start) // 2
        if arr[mid] == n:
            return mid
        elif arr[mid] > n:
            return caribinary(arr, start, mid - 1, n)
        else:
            return caribinary(arr, mid + 1, end, n)
    else:
        return -1
        
def bubblesort(arr):
    h = len(arr)
    
    for i in range(h):
        for j in range(0, h - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]     
    
    return arr

array = [87, 56, 34,23, 89, 15, 2, 200, 28, 31]
print(array)
hasil = bubblesort(array)


diurutkan = bubblesort(array)

cari = int(input("angka apa yang ingin dicari: "))
hasil = caribinary(diurutkan, 0, len(diurutkan) -1, cari)

print("setelah disorting\n", diurutkan)

if hasil != -1:
    print(f"Elemen {cari} ditemukan pada indeks {hasil}")
else:
    print(f"Elemen {cari} tidak ditemukan")