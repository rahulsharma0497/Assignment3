def closest_sum(nums, target):
  """
  Finds the three integers in nums whose sum is closest to target.

  Args:
    nums: An integer array of length n.
    target: An integer.

  Returns:
    The sum of the three integers that is closest to target.
  """

  closest_sum = float("inf")
  for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
      for k in range(j + 1, len(nums)):
        current_sum = nums[i] + nums[j] + nums[k]
        if abs(current_sum - target) < abs(closest_sum - target):
          closest_sum = current_sum
  return closest_sum


if __name__ == "__main__":
  nums = [-1, 2, 1, -4]
  target = 1
  print(closest_sum(nums, target))