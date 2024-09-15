# -*- coding: utf-8 -*-
"""
Created on  Sun Sep 15 02:49:55 2024

@author: hp
"""

import time
import csv
from funcs import ShuffleArray

# Insertion Sort algorithm
def insertion_sort(arr):
    """Sorts an array using the insertion sort algorithm."""
    n = len(arr)
    for i in range(1, n):
        temp = arr[i]
        j = i - 1
        while j >= 0 and temp < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp

# Merge Sort algorithm
def merge_sort(arr):
    """Sorts an array using the merge sort algorithm."""
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

# Measure runtime of a sorting function
def measure_time(sort_function, arr):
    """Measures the runtime of a sorting function."""
    start_time = time.time()
    sort_function(arr.copy())  # Use a copy to avoid modifying the original array
    end_time = time.time()
    return end_time - start_time

# Read words from file
def read_words(filename):
    """Reads words from a text file into a list."""
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines()]

# Main function
def main():
    filename = 'words.txt'
    words = read_words(filename)

    # Measure runtime for original array
    print("Sorting original array...")
    insertion_time_original = measure_time(insertion_sort, words)
    merge_time_original = measure_time(merge_sort, words)
    
    print(f"Original Insertion Sort runtime: {insertion_time_original:.6f} seconds")
    print(f"Original Merge Sort runtime: {merge_time_original:.6f} seconds")
    
    # Shuffle array
    print("Shuffling array...")
    ShuffleArray(words, 0, len(words))
    
    # Measure runtime for shuffled array
    print("Sorting shuffled array...")
    insertion_time_shuffled = measure_time(insertion_sort, words)
    merge_time_shuffled = measure_time(merge_sort, words)
    
    print(f"Shuffled Insertion Sort runtime: {insertion_time_shuffled:.6f} seconds")
    print(f"Shuffled Merge Sort runtime: {merge_time_shuffled:.6f} seconds")

    # Compare and write results to a CSV file
    with open('SortingResults.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Type', 'Original Insertion Sort (seconds)', 'Shuffled Insertion Sort (seconds)', 
                         'Original Merge Sort (seconds)', 'Shuffled Merge Sort (seconds)'])
        writer.writerow(['Runtime', insertion_time_original, insertion_time_shuffled, 
                         merge_time_original, merge_time_shuffled])

    print("Results saved to SortingResults.csv.")

