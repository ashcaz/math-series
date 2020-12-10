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