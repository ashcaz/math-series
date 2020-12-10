def fibonacci(n):
  if n < 2:
    return n
  else:
    fibonacci_list = [0,1]
    for x in range(2,(n + 1)):
      fibonacci_sum = fibonacci_list[x-1]+ fibonacci_list[x-2]
      fibonacci_list.append(fibonacci_sum)
    
    return fibonacci_list[n]
