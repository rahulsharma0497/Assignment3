def increment_integer(digits):
  """
  Increments the large integer represented by digits by one.

  Args:
    digits: An integer array representing the large integer.

  Returns:
    The resulting array of digits.
  """

  carry = 1
  for i in range(len(digits) - 1, -1, -1):
    if digits[i] + carry == 10:
      digits[i] = 0
      carry = 1
    else:
      digits[i] += carry
      carry = 0

  if carry == 1:
    digits.insert(0, 1)

  return digits


if __name__ == "__main__":
  digits = [1, 2, 3]
  print(increment_integer(digits))