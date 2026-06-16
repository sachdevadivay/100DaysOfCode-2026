# Given an integer array, determine the largest element present in the array.

def largestElement(arr):
    largest = arr[0]

    for num in arr:
        if num > largest:
            largest = num

    return largest

arr = list(map(int, input().split()))
print(largestElement(arr))
