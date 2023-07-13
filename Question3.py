def next_permutation(nums):
  """
  Finds the next lexicographical greater permutation of nums.

  Args:
    nums: An integer array of length n.

  Returns:
    None. The input array is modified in-place.
  """

  i = len(nums) - 2
  while i >= 0 and nums[i] >= nums[i + 1]:
    i -= 1

  if i < 0:
    nums.reverse()
  else:
    j = len(nums) - 1
    while j > i and nums[j] <= nums[i]:
      j -= 1

    nums[i], nums[j] = nums[j], nums[i]
    nums[i + 1:] = nums[i + 1:][::-1]


if __name__ == "__main__":
  nums = [1, 2, 3]
  next_permutation(nums)
  print(nums)