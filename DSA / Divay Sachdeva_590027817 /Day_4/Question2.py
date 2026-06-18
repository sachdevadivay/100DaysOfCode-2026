# Given an integer array and an integer k, rotate the array to the right by k steps.

def rotateArray(nums, k):
    n = len(nums)
    k = k % n

    nums = nums[-k:] + nums[:-k]
    return nums

nums = list(map(int, input().split()))
k = int(input())

print(rotateArray(nums, k))
