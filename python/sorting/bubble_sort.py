'''
Bubble sorting:
    取相邻2个item比较，大则交换，直到最后。最大的值移动到了队尾
    对去掉队尾的队列重复这个过程
    O(n^2)
'''

def bubble_sort(A):
    for i in range(0, len(A)-1):
        for j in range(0, len(A)-1-i):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
