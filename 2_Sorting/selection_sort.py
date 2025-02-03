def find_smallest_index(array):
    smallest = array[0]
    smallest_index = 0

    for i in range(1, len(array)):
        if array[i] < smallest:
            smallest = array[i]
            smallest_index = i

    return smallest_index

def find_smallest(array):
    smallest = array[0]
    smallest_index = 0

    for i in range(1, len(array)):
        if array[i] < smallest:
            smallest = array[i]
            smallest_index = i

    return smallest

print('find_smallest_index: ', find_smallest_index([5, 4, 10, 3, 2, 11, 1, 9, 0, 6, 8]))
print('find_smallest: ', find_smallest([5, 4, 10, 3, 2, 11, 1, 9, 0, 6, 8]))

def selection_sort(array):
    new_array = []

    for i in range(len(array)):
        smallest = find_smallest_index(array)
        new_array.append(array.pop(smallest))

    return new_array

print('selection_sort: ', selection_sort([5, 4, 10, 3, 2, 11, 1, 9, 0, 6, 8]))