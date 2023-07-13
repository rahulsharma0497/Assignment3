def can_attend_all_meetings(intervals):
  """
  Determines if a person could attend all the meetings in the array of meeting time
  intervals.

  Args:
    intervals: An array of meeting time intervals.

  Returns:
    True if the person could attend all the meetings, False otherwise.
  """

  intervals.sort(key=lambda interval: interval[0])
  for i in range(1, len(intervals)):
    if intervals[i][0] < intervals[i - 1][1]:
      return False
  return True


if __name__ == "__main__":
  intervals = [[0, 30], [5, 10], [15, 20]]
  print(can_attend_all_meetings(intervals))