def count_even_numbers(start, end):

    list = []
    good_end = end + 1
    while start < good_end:
        if start % 2 == 0:
            list.append(start)
        start += 1

    count = len(list) 
    print(count)



    
count_even_numbers(1, 10)
