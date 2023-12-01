# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 20:28:39 2023

@author: Gwen
"""

def binarysearch(arr, start, end, x):
    if end >= start:
        mid = start + (end - start) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarysearch(arr, start, mid - 1, x)
        else:
            return binarysearch(arr, mid + 1, end, x)
    else:
        return -1

def bubblesort(x):
    for i in range(len(x)-1):
        for j in range(0, len(x)-i-1):
            if x[j] > x[j+1]:
                x[j], x[j+1] = x[j+1], x[j]

    c = int(input("Masukkan angka yang dicari: "))
    print("Sesudah di sorting:", x)
    result = binarysearch(x, 0, len(x)-1, c)

    if result != -1:
        print(f"terdapat Angka {c} di urutan ke : {result}")
    else:
        print(f"Angka {c} tidak ditemukan dalam list")

array = [87, 54, 34, 23, 89, 15, 2, 200, 28, 31]
bubblesort(array)