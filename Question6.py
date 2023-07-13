def single_number(nums):
  """
  Finds the single element in nums where every other element appears twice.

  Args:
    nums: An integer array.

  Returns:
    The single element in nums.
  """

  result = 0
  for num in nums:
    result ^= num
  return result


if __name__ == "__main__":
  nums = [2, 2, 1]
  print(single_number(nums))