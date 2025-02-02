def binary_search(array, target):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = array[mid]

        if guess == target:
            return mid

        if guess > target:
            high = mid - 1

        else:
            low = mid + 1

    return -1


item_index = binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 5)

print(item_index)