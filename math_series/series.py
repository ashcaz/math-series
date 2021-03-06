def fibonacci(n):
  if n < 2:
    return n
  else:
    fibonacci_list = [0,1]
    for x in range(2,(n + 1)):
      fibonacci_sum = fibonacci_list[x-1]+ fibonacci_list[x-2]
      fibonacci_list.append(fibonacci_sum)
    
    return fibonacci_list[n]

def lucas(n):
  lucas_list = [2,1]
  if n < 2:
    return lucas_list[n]
  else:
    for x in range(2,(n + 1)):
      lucas_sum = lucas_list[x-1]+ lucas_list[x-2]
      lucas_list.append(lucas_sum)

  return lucas_list[n]

def sum_series(n, value_one=0, value_two=1):
  sum_list = [value_one, value_two]
  if n < 2:
    return sum_list[n]
  else:
    for x in range(2,(n + 1)):
      sum_series_sum = sum_list[x-1]+ sum_list[x-2]
      sum_list.append(sum_series_sum)
  
  return sum_list[n]