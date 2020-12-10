from math_series.series import fibonacci, lucas


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

def test_lucas_zero():
  actual = lucas(0)
  expected = 2
  assert actual == expected

def test_lucas_one():
  actual = lucas(1)
  expected = 1
  assert actual == expected

def test_lucas_five():
  actual = lucas(5)
  expected = 11
  assert actual == expected

def test_lucas_forty_four():
  actual = lucas(44)
  expected = 1568397607
  assert actual == expected