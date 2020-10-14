# Solution using selection and randomized partition to sort the array. 
# Runtime Complexity: O(n)
# Space Complexity: O(1)

import random
def k_largest_element(arr, k):  
    largest_k = len(arr) - k + 1
    return selection(arr, 0, len(arr)-1, largest_k)

def partition(arr, lo, hi):             # return an index such that everything on left of this index is smaller than everything on right of this index ... this does not mean that array is sorted
    x = arr[hi]
    i = lo - 1
    
    for j in range(lo, hi):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[hi] = arr[hi], arr[i+1]
    return i+1

def randomized_partition(arr, lo, hi):
    rand = random.randint(lo, hi)
    # to reduce complexity of the algorithm, make sure that the array is sorted.
    arr[hi], arr[rand] = arr[rand], arr[hi]
    return partition(arr, lo, hi)

def selection(arr, lo, hi, k ):
    if lo == hi:
        return arr[lo]
    pivot = randomized_partition(arr, lo, hi)
    dist = pivot - lo + 1                               #l-----p------h
    if dist == k:                                       #[dist ]          
        return arr[pivot]
    if dist > k:                                        #l-----k--p---h
        return selection(arr, lo, pivot -1, k)          # reduce size of array  
    else:
        return selection(arr, pivot+1, hi, k-dist)      #l-----p--k---h
                                                        #       l-k'---h


arr = [3,2,1,5,6,4]
k = 2
print(k_largest_element(arr, k))

arr = [3,2,3,1,2,4,5,5,6]
k = 4
print(k_largest_element(arr, k))