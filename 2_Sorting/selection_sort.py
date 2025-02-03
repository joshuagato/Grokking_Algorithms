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

print(find_smallest_index([5, 4, 3, 2, 1, 9, 0, 6, 8]))
print(find_smallest([5, 4, 3, 2, 1, 9, 0, 6, 8]))