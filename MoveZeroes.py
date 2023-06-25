def moveZerosToEnd(nums):
    # Count the number of non-zero elements
    count = 0
    for num in nums:
        if num != 0:
            nums[count] = num
            count += 1

    # Fill the remaining elements with zeros
    while count < len(nums):
        nums[count] = 0
        count += 1

# Example usage:
nums = [0, 1, 0, 3, 12]
moveZerosToEnd(nums)
print(nums)  # Output: [1, 3, 12, 0, 0]
