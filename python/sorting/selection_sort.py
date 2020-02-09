'''
selection sort:
    找到list里最小的那个item，然后放到list的最前面
    去掉队首的list里，继续这个过程。
    O(n^2)
'''

def selection_sort(A):
    for i in range(0, len(A) -1):
        min_index = i
        for j in range(i+1, len(A)):
            if A[j] < A[min_index]:
                min_index = j
        if min_index != i:
            A[i], A[min_index] = A[min_index], A[i]