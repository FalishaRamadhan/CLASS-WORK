

numbers = [11,22,33,44,55,66,77,88,99]

key = 77
start = 0
end = len(numbers)
found  = False
for i in (numbers):
    if numbers[i] == key:
        print("Found element")
        break
    else:
        print("Not found")
while start <= end:
    mid = (start + end) // 2
    if numbers[mid] == key:
        print("Found element at position:" , mid)
        found = True
        break
    elif key < numbers[mid] :
        end  = mid - 1
    elif key > numbers[mid]:
        start = mid + 1
if not found:
    print(f"{key} not found in the list")


    #implement recursion
