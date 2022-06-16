# BINARY SEARCH
# list must be sorted and should not contain duplicates


def binary_search(list, target):
    # low limit is the first index and the high limit is the last index of the sequence
    low = 0
    high = len(list) - 1

    if target in list:
        while low <= high:
            midpoint = (low + high) // 2
            if list[midpoint] == target:
                return midpoint
            if target > list[midpoint]:
                # it the target search is higher than middle number then the lower limit is changed to midpoint + 1, but the higher limit will be the same
                low = midpoint + 1
            if target < list[midpoint]:
                # it the target search is lower  than middle number then the upper limit is changed to midpoint + 1, but the lower limit will be the same
                high = midpoint - 1
    else:
        print("Not in the list.")


list = [1, 99, 3657, 5415, 21, 684, 574, 3, 68, 41, 45, 121, 101, 96, 9]
list = sorted(list)
target = 99
z = binary_search(list, target)
print(z)