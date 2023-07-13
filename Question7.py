def find_missing_ranges(nums, lower, upper):
  """
  Finds the shortest sorted list of ranges that covers all the missing numbers in the
  range [lower, upper].

  Args:
    nums: A sorted unique integer array.
    lower: The lower bound of the range.
    upper: The upper bound of the range.

  Returns:
    The shortest sorted list of ranges that covers all the missing numbers in the
    range.
  """

  ranges = []
  current_range = [lower, lower]
  for num in nums:
    if current_range[1] < num:
      ranges.append([current_range[0], current_range[1]])
      current_range = [num, num]
    else:
      current_range[1] = num

  if current_range[1] != upper:
    ranges.append([current_range[0], upper])
  return ranges


if __name__ == "__main__":
  nums = [0, 1, 3, 50, 75]
  lower = 0
  upper = 99
  print(find_missing_ranges(nums, lower, upper))