def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[len(array) // 2]
    left = []
    right = []
    equal = []

    for number in array:
        if pivot > number:
            left.append(number)
        elif pivot < number:
            right.append(number)
        else:
            equal.append(number)

    return quick_sort(left) + equal + quick_sort(right)




array = [2, 6, 3, 4, 1, 5, 7]
sortted = quick_sort(array)
print(sortted)

