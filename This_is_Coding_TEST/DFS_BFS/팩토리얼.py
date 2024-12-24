
def factorial_iteraton(n):
  result = 1
  for i in range(1, n + 1):
    result *= i
  return result


def factorial_recursion(n):
  result = 1
  if n <= 1: 
    return 1
  return n * factorial_recursion(n-1)