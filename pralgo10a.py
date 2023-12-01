# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 20:36:35 2023

@author: user
"""

def binarysea(arr, start, end, n):
    if end >= start:
        mid = start + (end - start)//2
        if arr[mid] == n:
            return mid
        elif arr[mid] > n:
            return binarysea(arr, start, mid - 1, n)
        else:
            return binarysea(arr, mid + 1, end, n)
    else:
        return - 1
def bubblesort(n):
    for i in range(len(n)-1):
        for j in range(0, len(n) - i - 1):
            if n[j] > n[j+1]:
                n[j], n[j+1] = n[j+1], n[j]
    nyariangka = int(input("Masukkan angka yang akan dicari: "))
    print("setelah di sorting: ", n)
    hasil = binarysea(n, 0, len(n) - 1 , nyariangka)
    
    if hasil != -1:
        print(f"ada Angka {nyariangka} di urutan ke : {hasil}")
    else:
        print(f"Angka {nyariangka} tidak ditemukan dalam list")

array = [87, 54, 34, 23, 89, 15, 2, 200, 28, 31]
bubblesort(array)
