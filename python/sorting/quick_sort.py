'''
Quick Sort:
    1. select a pivot, often, the first item is used for pivot
    2. all other items smaller than the pivot, move to the left side of the list
    3. all other items larger than the pivot, move to the right side of the list
    4. randomly chosen pivots ensure O(nlogn)

    Quick sort is recursive, method that calls itself
    divide and conquer algorithm
    very efficient for large data sets

    worst case is O(n^2)
    average case is O(nlogn)
    performance depends largely on pivot selection

'''

def quick_sort(A):
    _quick_sort_recursive(A, 0, len(A) - 1)

def _quick_sort_recursive(A, low, high):
    if low < high:
        pivot_index = partition(A, low, high)
        _quick_sort_recursive(A, low, pivot_index-1)
        _quick_sort_recursive(A, pivot_index+1, high)

def partition(A, low, high):

    pivot_index = select_pivot(A, low, high)
    pivot_value = A[pivot_index]
    A[low], A[pivot_index] = A[pivot_index], A[low]
    border = low

    for i in range(low, high+1):        
        if A[i] < pivot_value:
            border += 1
            A[i], A[border] = A[border], A[i]
            
    A[low], A[border] = A[border], A[low]

    return border

def select_pivot(A, low, high):
    mid = (high + low) // 2
    pivot = high
    if A[low] < A[mid] and A[mid] < A[high]:
        pivot = mid
    elif A[low] < A[high]:
        pivot = low
    return pivot