#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
Line #9: 0(1) or Constant time
Line #10: O(n) or Linear time
Line #11: 0(1) or Constant time

Summary:
Time = 1 + n + 1
O(n)

b)
Line #16: O(1) or Constant time
Line #17: O(n) or Linear time
Line #18: O(1) or Constant time
Line #19: O(n) or Linear time
Line #20: O(1) or Constant time
Line #21: O(1) or Constant time

Summary:
Time = 1 + n + 1 + n + 1 + 1
O(n2)

c)
Line #25: O(1) or Constant time
Line #26: O(1) or Constant time
Line #27: O(1) or Constant time
Line #29: O(n) or Linear time

Summary:
Time = 1 + 1 + 1 + n
O(n)

## Exercise II

Question break down:
1. Building = n-story(height).
2. Number of eggs = x(plenty).
3. Egg Durability = f floor high or lower.
4. Possible masked keyword = "Devise" which is likely implying divide.

Summarized question:
1. Find the value of f using a method that will minimize the number of broken eggs.

The process would involve: (Binary Search Method)
1. Pulling the complete number of floors by finding the first and last index of the floors then dividing the floors by two.
2. Checking if floor f is on the right or the left side side of the divided list.
3. The side tha does not contain or is greater than f would be eliminated.
4. This process can be repeated until f is found and returned.