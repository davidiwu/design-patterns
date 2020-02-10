import random
import time
from insertion_sort import *
from bubble_sort import bubble_sort
from selection_sort import selection_sort
from quick_sort import quick_sort
from merge_sort import merge_sort

size = 10000
span = 100000

def timing_sorting(array_need_sorting, sorting_algorithm):
    start_time = time.clock()
    sorting_algorithm(array_need_sorting)
    end_time = time.clock()

    return (end_time-start_time)*1000   # return milliseconds


array_need_sorting = [random.randint(0, span) for _ in range(0, size)]
copy_array_1 = array_need_sorting.copy()
copy_array_2 = array_need_sorting.copy()
copy_array_3 = array_need_sorting.copy()
copy_array_4 = array_need_sorting.copy()

time1 = timing_sorting(array_need_sorting, insertion_sort)

# worst case : reversed alreading sorted array
reverse_array = array_need_sorting.reverse()
time1_1 = timing_sorting(array_need_sorting, insertion_sort)

array_need_sorting.reverse()
time2 = timing_sorting(array_need_sorting, insertion_sort_shifting)

time3 = timing_sorting(copy_array_1, bubble_sort)

time4 = timing_sorting(copy_array_2, selection_sort)

time5 = timing_sorting(copy_array_3, quick_sort)

time6 = timing_sorting(copy_array_4, merge_sort)

print(f'insertion sorting time: normal: {time1} ms, worst case: {time1_1}ms, shifting: {time2} ms ')
print(f'bubble sorting time {time3} ms')
print(f'selection sorting time {time4} ms')
print(f'quick sorting time {time5} ms')
print(f'merge sorting time {time6} ms')