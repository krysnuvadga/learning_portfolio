def sum_digits3(n):
   r = 0
   while n:
       r, n = r + n % 10, n // 10
   return r
