import random

print(random.randint(5, 20))  # line 1
"""
6, 16,17,11,12,20,9,16,20,20
The smallest number is 6 and the biggest number is 20.
"""

print(random.randrange(3, 10, 2))  # line 2
"""
3,5,3,5,7,5,7,3,7,9
The smallest number is 3 and the largest number is 9.
line 2 cannot product number 4. 
"""
print(random.uniform(2.5, 5.5))  # line 3
"""
3.590511377774229,4.267860442684993,3.5951121425484156,5.04274704242155,3.8270535948583486,4.978226498310255,2.9266874220270624
The smallest number is 2.9266874220270624 and the largest number is 5.04274704242155
"""

print(random.randint(0, 100))