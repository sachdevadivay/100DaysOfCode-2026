# Given an sorted integer array and a target value, count the number of occurrences of the target in the array and return the result.

def countOccurrences(arr, target):
    count = 0

    for num in arr:
        if num == target:
            count += 1

    return count

arr = list(map(int, input().split()))
target = int(input())

print(countOccurrences(arr, target))
