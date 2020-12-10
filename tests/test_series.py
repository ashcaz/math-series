from math_series.series import fibonacci

def test_fibonacci_zero():
  actual = fibonacci(0)
  expected = 0
  assert actual == expected

def test_fibonacci_one():
  actual = fibonacci(1)
  expected = 1
  assert actual == expected

def test_fibonacci_four():
  actual = fibonacci(4)
  expected = 3
  assert actual == expected

def test_fibonacci_twenty():
  actual = fibonacci(20)
  expected = 6765
  assert actual == expected