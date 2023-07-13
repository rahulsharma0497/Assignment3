def four_sum(nums, target):
  """
  Finds all the quadruplets in nums whose sum is equal to target.

  Args:
    nums: An integer array of length n.
    target: An integer.

  Returns:
    A list of all the quadruplets that sum to target.
  """

  quadruplets = []
  for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
      for k in range(j + 1, len(nums)):
        for l in range(k + 1, len(nums)):
          if nums[i] + nums[j] + nums[k] + nums[l] == target:
            quadruplets.append([nums[i], nums[j], nums[k], nums[l]])
  return quadruplets


if __name__ == "__main__":
  nums = [1, 0, -1, 0, -2, 2]
  target = 0
  print(four_sum(nums, target))