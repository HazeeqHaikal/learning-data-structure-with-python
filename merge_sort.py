def merge_sort(list):
    # sorts a list in ascending order
    # returns a new sorted list

    # divide: find the midpoint of the list and dvide into sublist
    # conquer: recursively sort the  sublists created in previous step
    # combine: merge the sorted sublists created in previous step
    # run in overall O(n log n)
    
    if len(list) <= 1:
        return list
    
    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(list):

    # Divide the unsorted list at midpoint into sublist
    # Returns two sublists - left and right
    # Takes overall O(log n) time

    mid = len(list) // 2
    left = list[:mid]
    right = list[mid:]

    return left, right

def merge(left, right):

    # merges two list (arrays), sorting them in the process
    # returns a new merged list 
    # runs in overall linear time O(n) time

    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1
    

    while i < len(left):
        l.append(left[i])
        i += 1

    while j < len(right):
        l.append(right[j])
        j += 1
    return l

def verify_sorted(list):
    n = len(list)

    if n == 0 or n == 1:
        return True
    
    return list[0] < list[1] and verify_sorted(list[1:])

alist = [54, 26, 93, 48, 10, 30, 99, 40]
    
l = merge_sort(alist)
print(l)
print(verify_sorted(alist))
print(verify_sorted(l))