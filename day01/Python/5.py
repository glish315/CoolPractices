def quick_sort(output):
    if len(output) <= 1:
        return output

    pivot = output[len(output) // 2]
    left = []
    right = []
    equal = []

    for number in output:
        if pivot > number:
            left.append(number)
        elif pivot < number:
            right.append(number)
        else:
            equal.append(number)

    return quick_sort(left) + equal + quick_sort(right)


array = [2, 6, 3, 4, 1, 5, 7]
sort = quick_sort(array)
print(sort)
