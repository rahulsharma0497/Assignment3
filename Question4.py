def search_insert(nums, target):
  """
  Finds the index where the target would be inserted in nums.

  Args:
    nums: A sorted array of distinct integers.
    target: The target value.

  Returns:
    The index where the target would be inserted.
  """

  low = 0
  high = len(nums) - 1
  while low <= high:
    mid = (low + high) // 2
    if nums[mid] == target:
      return mid
    elif nums[mid] < target:
      low = mid + 1
    else:
      high = mid - 1
  return low


if __name__ == "__main__":
  nums = [1, 3, 5, 6]
  target = 5
  print(search_insert(nums, target))