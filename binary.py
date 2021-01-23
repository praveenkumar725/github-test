def binarySearch(numbers, first, last, searchElement):
    found = False 
    while first<=last and not found: 
        mid = int((first+last)//2)
        if numbers[mid]==searchElement:
            found = True 
            break 
        elif numbers[mid] > searchElement:
            first=mid+1
        else:
            last=mid-1 
            return found
N = int(input("enter the number of element:"))
numbers = list(map(int, input().split()[:N]))
searchElement = int(input("enter the search element:"))
first = 0
last = N-1
if(binarySearch(numbers, first, last, searchElement)):
    print("YES")
else:
    print("NO")

