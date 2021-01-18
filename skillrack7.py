#  Accept an integer A as the input. If A is a positive integer then print the first five multiples of the unit digit of A as the output.
#  If A is a negative integer then print the first ten multiples of the unit digit of A as the output.


num = int(input())
if num > 0:
    unit = num%10
for ctr in range(1, 6):
    print(ctr*unit, end = " ")
else:
    unit = (num*-1)%10
for ctr in range(1, 11):
    print(ctr*unit, end = " ")


















